#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

# execfile('/home/feng/meta/header_0903.py')
keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
tks = pyutil.readBaseFile('results/0427__makeTracks-Brachy/tracks.npy').tolist()
# execfile("/home/feng/envs/Fig_Brachy/loadRNA_Bd.py")
# figs = pyutil.collections.OrderedDict()

plt.rcParams['font.size'] = 14.
plt.rcParams['xtick.labelsize'] = 16.
plt.rcParams['axes.titlepad'] = 24.
figsize=[14, 10]
panel_kw = dict(
    figsize=figsize,
    show_axa = 1,
    show_axc = 0,
    showGrid = 0,
    width_ratios = [1,14,0.],
    tickMax=10,
#     title= '',
#     height_ratios = [1,3,3,3,1],
)

NCORE=1


###### [important]
# cluFile = 'results/0129__showCluster__Brachy-RNA-all/clu.csv'
# cluFile = 'results/0216__showCluster__Brachy/clu.csv'
cluFile = 'results/0408-freezerCluster/\
0427-dump-rnapkread-topped-log2-meannormpk/baseDist-vmfDistribution_seed-0/cluc.csv'
# pyutil.localise(pyext.base__file(cluFile))
# cluAUC = pyutil.readBaseFile('results/0205__interpAUC__Brachy/clu.csv')
dClu = pyutil.readBaseFile('results/0216__showCluster__Brachy/cache.npy').tolist()

keyDF['included'] = keyDF.eval('index in @tks.keyDFTrack.index')
keyDFC = keyDF[['BioName','included']].merge(left_index=True,right_index=True,
                 right=dClu['stats'],how='left').sort_values(['included','clu','score'])
keyDFC.to_html('keyDFC.html')

import warnings



# try:
if 1:
    (pyext.base__file('results/0130__callDiffTarg__Brachy-ELF3/DONE'))
    
    chipClu = pyutil.readBaseFile('results/0130__callDiffTarg__Brachy-ELF3/clu.csv')
    chipClu.columns = ['clu']
    peak2gene = pyutil.readBaseFile('results/0130__makePeakWindows__Brachy-ELF3/peak2geneFile.tsv')
    geneDF  = sdio.peak2gene(peak2gene, chipClu)
    indCHIP = rnaIndex = geneDF.query('clu==1').feat_acc.unique() 
    indCHIP = tks.rnaseq.index & indCHIP
    chipTrack = tks.rnaseq.eval("index.isin(@rnaIndex)")


vdf = pd.concat(tks.trackOrders['allRNA'][1:-1],axis=1)
vdf = scount.countMatrix(vdf)
vdf.qc_Avg();
vdf.summary.plot.scatter('per_MSQ','MSQ')
figs['MSQ'] = plt.gcf()
index0 = vdf.summary.query('per_MSQ > 0.6').index


clu = pyext.readBaseFile(cluFile)

res = sjob.job__render__panelPlot(
    clu=clu[['clu']],
    tracks = (
        tks.trackOrders['allRNA']
        + [chipTrack]
             ),
    order = clu[['clu','score']],
#     index = index0,
    index = clu.index,
#     index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= 'withScore__sureClu__withCHIP__allTracks',
    panel_kw=panel_kw,
    figsize=[14,20]
)
figs.update([res])           

index = chipTrack.index[chipTrack.values.ravel()]
name = 'withScore__chipTarg__withCHIP__allTracks'
clu[['clu','score']].reindex(index).to_csv(name+'.csv')
res = sjob.job__render__panelPlot(
    clu=clu[['clu']],
    tracks = (
        tks.trackOrders['allRNA']
        + [chipTrack]
             ),
    order = clu[['clu','score']],
#     index = index0,
    index = index,
#     index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= name,
    panel_kw=panel_kw,
    figsize=[14,20]
)
figs.update([res])           

# pyutil.render__images(figs,exts=['png','svg'])
pyutil.render__images(figs,exts=['png',])

