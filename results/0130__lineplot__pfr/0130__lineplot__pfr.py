#!/usr/bin/env python
# -*- coding: utf-8 -*-



buf = '''
time			0	0	4	4	8	8	12	12
valueName			Pfr/Ptot	Ptot	Pfr/Ptot	Ptot	Pfr/Ptot	Ptot	Pfr/Ptot	Ptot
header	genotype	rep								
BdphyC/AtphyAB #1 (het)	BdphyC/AtphyAB	1	87	6.23	52.7	4.08	38.4	4.45		
BdphyC/AtphyAB #1 (het)	BdphyC/AtphyAB	2	87	5.83	55.3	3.78	34.96	3.87		
BdphyC/AtphyAB #5 (het)	BdphyC/AtphyAB	3	87	13.5	65.45	9.06	45.9	7.84	34.7	9.96
BdphyC/AtphyAB #5 (het)	BdphyC/AtphyAB	4	87	12.12	70.9	10.88	63.68	10.26	38.1	9.85
BdphyC/AtphyAB #5 (het)	BdphyC/AtphyAB	5	87	9.07	85.9	10.34	51.56	10.16	40.36	9.88
BdphyC/AtphyAB #5 (het)	BdphyC/AtphyAB	6	87	12.67	82.3	9.58	78.5	10.3	46.5	10.09
BdphyC/AtphyAB #5 (het)	BdphyC/AtphyAB	7			84.93	10.2	80.9	8.89	38.8	9.62
BdphyC/BdWT	BdphyC/BdWT	1	87	203.98	60.92	127.92	35.5	160.35	20.8	151.71
BdphyC/BdWT	BdphyC/BdWT	2	87	156	58.46	116.84	51	123.36	27	156.54
BdphyC/BdWT	BdphyC/BdWT	3	87	184.56	47.4	119.09	63.1	172.81	28.8	190.86
BdphyC/BdWT	BdphyC/BdWT	4	87	139.75	76.79	154.15	47	105.67	32.1	181.33
BdphyC/BdWT	BdphyC/BdWT	5	87	216.94	81.1	239.22	48.9	198.94	53.5	156.49
BdphyC/BdWT	BdphyC/BdWT	6	87	271.4	85.4	268.06	67.9	236.41		
BdphyC/BdWT	BdphyC/BdWT	7	87	182.53	73.66	236.99	51.9	196.45		
'''.strip()


import pymisca.ext as pyext
pyext.execBaseFile('headers/header__import.py')
figs = pyutil.collections.OrderedDict()

import StringIO
dfc0 = pd.read_table(StringIO.StringIO(buf),header=[0,1],index_col=[0,1,2],)
pyext.index__set_level_dtype( dfc0.columns,0,int,inplace=True)


pyvis.mpl_header()
# plt.rcParams['font.size'] = 14.
# plt.rcParams['xtick.labelsize'] = 16.
# plt.rcParams['axes.titlepad'] = 24.

# dfc.columns  = dfc.columns.set_names([x[-1] for x in dfc.columns.levels])
# dfc
# dfc.index.name = dfc.iloc[0,0]
# dfc = dfc.drop(index=dfc.index[0])

dfc = dfc0.reindex(columns=['Pfr/Ptot'],level='valueName')
level=0
# dfc0.columns = pyext.index__sortFactor(dfc0.columns, level=0,dtype=int)



# dfc = dfc.apply(np.log2)

def plotter(dfc):
    # dfcc  = scount.countMatrix(dfcc)
    # dfcc.heatmap()
    # dfc = dfc0.reindex(columns=['Pfr/Ptot'],level='valueName')

    dfcc = dfc.T.reset_index().melt(id_vars=['time','valueName']).pivot_table(index=['genotype','time',],columns='rep')
    dfcc = dfcc.sort_index()
    dfcc = scount.countMatrix(dfcc).qc_Avg()
    dfcc.summary

    

    # dfcc.summary['M']
    # summ = dfcc.summary
    # ax = plt.gca()
    fig,ax= plt.subplots(1,1,figsize=[5,4])
    summ = dfcc.summary.pivot_table(index='time',columns=['genotype'])
    # summ['err'] = summ['SD']

    
    M = summ.M
    err = summ['SE']
    pyvis.linePlot4DF(df= M.T - err.T,
                    y2= M.T + err.T,which='fill_between',alpha=0.25,ax=ax,)
        
#     LCs = plt.rcParams['axes.prop_cycle'].by_key()['color']
    LCs = cmap = plt.get_cmap('Set1')
    mapper = {}
    for i,( gtype, dfcc) in enumerate(dfc.groupby(level='genotype',axis=0)):
        color = cmap(i)
        x = dfcc.columns.get_level_values('time')[None,:]
    #     x = np.arange(len(dfc.columns))[None,:]
        y = dfcc.values
        coef = pyext.arr__polyFit(x,y,1)
        eqn = pyvis.eqn_lm(coef)
#         plt.title(pyvis.eqn_lm(coef))

        x = np.arange(len(dfcc.columns))[None,:]
        lcoef = pyext.arr__polyFit(x,y,1)
        pyvis.abline(*lcoef,color=color)
        
        newLab = '{gtype}\n{eqn}'.format(**locals())
        mapper[gtype] = newLab
    #### Add equation to label
    summ =  summ.rename(columns=mapper, level=1)
        

    res = pyvis.linePlot4DF(df= summ.M.T ,which='plot',alpha=1.0,ax=ax,
                            marker='o',
                            linewidth=0)
    plt.legend(*pyvis.line__getLegends(sum(res,[])))
        
    ax.set_ylim(4,7)
    ax.set_xlabel('time in darkness (h)')
    return fig

valueName = 'Pfr/Ptot'
dfc = dfc0.reindex(columns=[valueName],level='valueName')
dfc = dfc.apply(np.log2)
plotter(dfc)
plt.ylabel(r'$\log_2( {{{valueName}}} \cdot 100 )$'.format(**locals()))
figs['plot1'] = plt.gcf()

dfc = dfc0.reindex(columns=[valueName],level='valueName')
dfc = dfc.apply(lambda x: (100.-x))
dfc = dfc.apply(np.log2)
plotter(dfc);
plt.ylabel('log2(100 - {valueName} )'.format(**locals()))
figs['plot2'] = plt.gcf()

pyutil.render__images(figs)