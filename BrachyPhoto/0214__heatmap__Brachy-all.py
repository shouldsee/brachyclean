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
    width_ratios = [1,14,0.5],
    tickMax=10,
#     title= '',
#     height_ratios = [1,3,3,3,1],
)

NCORE=1


###### [important]
cluFile = 'results/0129__showCluster__Brachy-RNA-all/clu.csv'

cluAUC = pyutil.readBaseFile('results/0205__interpAUC__Brachy/clu.csv')
dClu = pyutil.readBaseFile('results/0129__showCluster__Brachy-RNA-all/cache.npy').tolist()

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



pyutil.localise(cluFile,baseFile=1)
res = sjob.job__render__panelPlot(
    clu=cluFile,
    tracks = (
        tks.trackOrders['allRNA']
        + [chipTrack]
             ),
    order=dClu['stats'],
    index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= 'withScore__sureClu__withCHIP__allTracks',
    panel_kw=panel_kw,
    figsize=[14,20]
)
figs.update([res])  



res = sjob.job__render__panelPlot(
    clu=cluFile,
    tracks = (
        [        
            'cluTrack',
            tks.rnaseq_wk3wt,
            tks.rnaseq_wk3elf3ld_wk3elf3sd ,
            tks.keyDFTrack,
            chipTrack,
        ]
     ),
    order=dClu['stats'],
    index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= 'withScore__sureClu__withCHIP__wk3ldsd-elf3ldsd',
    panel_kw=panel_kw,
    figsize=[14,7]
)
figs.update([res])  

pyutil.render__images(figs,exts=['png','svg'])
