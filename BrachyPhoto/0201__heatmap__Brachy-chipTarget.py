#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

# execfile('/home/feng/meta/header_0903.py')
keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
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

tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
# tks.rnaseq.shape
cluFile = 'results/0129__showCluster__Brachy-RNA-all/clu.csv'
clu = pyutil.readBaseFile(cluFile).reindex(tks.rnaseq.index).fillna(-1);
dClu = pyutil.readBaseFile('results/0129__showCluster__Brachy-RNA-all/cache.npy').tolist()
chipClu = pyutil.readBaseFile('results/0130__callDiffTarg__Brachy-ELF3/clu.csv')
chipClu.columns = ['clu']
peak2gene = pyutil.readBaseFile('results/0130__makePeakWindows__Brachy-ELF3/peak2geneFile.tsv')
geneDF  = sdio.peak2gene(peak2gene, chipClu)
indCHIP = rnaIndex = geneDF.query('clu==1').feat_acc.unique() 
indCHIP = tks.rnaseq.index & indCHIP
chipTrack = tks.rnaseq.eval("index.isin(@rnaIndex)")
tks.keyDFTrack.height = 4

res = sjob.job__render__panelPlot(
    clu=clu,
    tracks = tks.trackOrders['currentOrder'][:-1] + [
        tks.rnaseq_wk3ld_wk2ld,
        scount.countMatrix(keyDF[['BioName']],
                           height=4),
        
#             tks.keyDFTrack,
#             chipTrack
    ],
    order=pd.concat([clu,dClu['score']],axis=1).fillna(0.),
    index = indCHIP,
    baseFile=1,
    aliasFmt='withScore__chipTarget__withCHIP',
    panel_kw=panel_kw,
    figsize=[14,12]
)
figs.update([res])
pyutil.render__images(figs,exts=['png','svg'])
pyutil.sys.exit()