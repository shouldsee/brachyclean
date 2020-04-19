#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymisca.header as pyhead
pyhead.execBaseFile('headers/header__import.py')
figs = pyutil.collections.OrderedDict()

figsize=[5.5, 4]
# figsize = [5,3]
buf ='''
	ELF3 protein levels			rubisco	ELF3/rubisco	ELF3/rubisco
WT	144.506	0.198	1	1748.669	0.082637709023263	0.082637709023263
ZT12	4801.095	6.588	2	2091.012	2.29606286334081	2.29606286334081
ZT16	10202.359	13.999	3	1879.82	5.42730633784086	5.42730633784086
ZT20	14909.38	20.458	4	1909.477	7.80809614360372	7.80809614360372
ZT0	17212.966	23.618	5	1939.719	8.87394823683224	8.87394823683224
ZT0.5	15226.865	20.893	6	1844.012	8.25746524426088	8.25746524426088
ZT1	5540.267	7.602	7	1934.426	2.86403667030944	2.86403667030944
ZT4	4841.853	6.644	8	1699.79	2.84850069714494	2.84850069714494
'''

pyvis.mpl_header()

dfc = pyutil.read__buffer(buf,ext='tsv')
# dfc
dfc = dfc.drop(index='WT')
# dfc['ZTime'] = dfc.index
dfc['ZTime_num'] = dfc.index.str.strip('ZT').astype(float)
vals = dfc['ZTime_num'].values

vals = dfc['ZTime_num'].values
vals = (vals - vals[0]) % 24
dfc['x'] = vals 


fig, ax = plt.subplots(1,1,figsize=figsize)

xcol  ='x'
xlab = ''
ycol = 'ELF3/rubisco'
ylab = ycol
dfc.plot(x=xcol,
         y=ycol,
         rot='vertical',marker='o',
         legend=False,
         ax=ax
        )

ax =  plt.gca()

tickDF = dfc.drop(index='ZT0.5')
ax.set_xticks(tickDF[xcol])
ax.set_xticklabels(tickDF.index)


ax.set_ylim([0,None])
# ax.set_xlim(-1,24)
pyvis.abline(x0=12.0,color='black')
ax.set_xlabel(xlab)
# plt.
ax.set_ylabel(ylab)
ax.grid(1)

figs['ELF3_WB'] = ax.figure


buf = '''
	light	ZTime				rubisco	ELF3/rubisco
	label	ZT16					
	label	ZT20					
	label	ZT0					
	label	ZT4					
	label	ZT8					
SD ZT20	SD	ZT20	1	22429.56	1	16755.037	1.33867564720985
SD ZT0	SD	ZT0	2	22107.43	2	15271.602	1.44761695596834
SD ZT4	SD	ZT4	3	2216.163	3	17072.501	0.129808924890384
LD ZT20	LD	ZT20	4	10005.388	4	21653.141	0.462075594483036
LD ZT0	LD	ZT0	5	13618.782	5	24843.128	0.54819111345399
LD ZT4	LD	ZT4	6	1203.305	6	21513.643	0.05593218219713
LL ZT20	LL	ZT20	7	6360.246	7	13980.258	0.454944822906702
LL ZT0	LL	ZT0	8	1228.82	8	15790.087	0.07782224379131
LL ZT4	LL	ZT4	9	1207.305	9	12064.48	0.100071034972083
20h/12h ZT0	20h/12h	ZT0	10	15180.539	10	15560.283	0.975595302476182
20h/12h ZT4	20h/12h	ZT4	11	4013.104	11	17322.645	0.231668085329925

'''

# figsize=[5.5, 4]

dfc0 = dfc = pyutil.read__buffer(buf,ext='tsv')

# dfc
# dfc = dfc.drop(index='WT')
# dfc['ZTime'] = dfc.index
vals = dfc['ZTime_num'] = dfc.ZTime.str.strip('ZT').astype(float)
offset = vals[0]
xfunc= lambda x:(vals - offset) % 24
vals = xfunc(vals)
vals = (vals -vals[0])

dfc['x'] = vals 
dfc.sort_values(['x'])
dfc = dfc.pivot_table(index='x',columns='light',
#                       sort=False,
                      aggfunc=lambda x:x,
#                       values=dfc.columns.tolist()
                     )



fig, ax = plt.subplots(1,1,figsize=figsize)

xs = dfc.index
pyvis.linePlot4DF(df=dfc[ylab].T,xs=xs,marker='o',ax=ax)
ax = plt.gca()
ax.legend(title='Photoperiod')

ax.set_ylim([0,None])
ax.set_xlim(0,16)


tickSer = dfc['ZTime']['label']
ax.set_xticks(tickSer.index)
ax.set_xticklabels(tickSer.values)

ax.set_xlabel(xlab)
ax.set_ylabel(ylab)
ax.grid(1)
pyvis.abline(x0=dfc0.query('ZTime=="ZT0"').dropna().x[0],color='black')


figs['WB_ELF3-photo'] = ax.figure

pyutil.render__images(figs,exts=['png','svg'])