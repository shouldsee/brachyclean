#!/usr/bin/env python
# -*- coding: utf-8 -*-
NCORE=6
import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
lst = []
for rna in [
    tks.rnaseq_wk2wt,
    tks.rnaseq_wk2sd,
    tks.rnaseq_wk2ld_phycko,
    tks.rnaseq_wk3sd,
    tks.rnaseq_wk3ldppd1_wk3ldwt
]:
    
    
    dfcc = rna.relabel('ZTime_int')
    dfcc.columns = dfcc.columns.astype(float)
    M_time = pyutil.interp_bytime(dfcc).mean(axis=1)
    M_time.columns = [M_time.name]
#     M_time.columns = [' '.join(M_time.name.split('_')[-2:])]
    lst += [M_time]
    
#     rna.heatmap(figsize=[12,6])
#     figs[M_time.name] = plt.gcf()
    
    plt.title(rna.name)

    
dfTimeAvg = df_timeAvg = pd.concat(lst,axis=1)
# rnaseq_wk2sd.heatmap()

# rnaseq_wk3sd

xlab = 'SD_Wk2_elf3-1/wt'
ylab = 'LD_Wk2_phyC-4/wt'
xs,ys = df_timeAvg[xlab],df_timeAvg[ylab]

fig = plt.figure(figsize=[10,10])
ax = plt.subplot(111)
axs = [None,ax,None,None]
axs=  pyvis.qc_2var(xs,ys,
              xlim=[-4,4],ylim = [-3,3],
             clu = sutil.tidyBd(df_timeAvg).index.isin(keyDF.index)
                    ,nMax=50000,
                   axs=axs)
pyvis.add_text(xs=xs,
               ys=ys,
               labs=keyDF.BioName,ax=axs[1])
xlab = 'logFC(%s)'%xlab
ylab = 'logFC(%s)'%ylab
plt.xlabel(xlab);plt.ylabel(ylab)
plt.title('logFC averaged over time')

figs['scatter'] = fig


fig = plt.figure()
resp = xs + -1.*ys
per = pyutil.dist2ppf(resp)
plt.plot(per,resp,'o')
# plt.xlim(0.9,1.05)
plt.grid(1)
# pyvis.add_text(per[per>0.9],
#                resp,keyDF.BioName)

figs['ppf'] = plt.gcf()


score = pd.concat([resp, per],axis=1)
# score.index = pyutil.paste0([xs.index,['.v3.1']])
score.columns = ['score__rnaseq__AUC',
                 'per__rnaseq__AUC']
score.to_csv('score__rnaseq__AUC.csv')
dfTimeAvg.to_csv('dfTimeAvg.csv')


# dfTimeAvg = pyutil.readBaseFile('results/0205__interpAUC__Brachy/dfTimeAvg.csv')
clu = pd.DataFrame()
ys = dfTimeAvg['LD_Wk3_ppd1/wt']
clu['ppd1__up'] = ys > 0.5
clu['ppd1__down'] = ys < -0.5
clu.to_csv('clu.csv')

pyutil.render__images(figs,exts=['png'],)