#!/usr/bin/env python
# -*- coding: utf-8 -*-

NCORE = 10
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



dClu = pyutil.readBaseFile('results/0129__showCluster__Brachy-RNA-all/cache.npy').tolist()

vdf = pd.concat(tks.trackOrders['currentOrder'][1:-1],axis=1)
vdf = scount.countMatrix(vdf).qc_Avg()
index0  = vdf.summary.query('per_MSQ>0.2').index
index0 = vdf.index

res = sjob.job__render__panelPlot(
    clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
    tracks = tks.trackOrders['currentOrder'],
    order=dClu['stats'],
    baseFile=1,
    index='clu.query("clu!=-1").index & index0',
    aliasFmt='withScore__sureClu',
    panel_kw=panel_kw,
    extra = dict(index0=index0),
)
figs.update([res])

res = sjob.job__render__panelPlot(
    clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
    tracks = tks.trackOrders['currentOrder'],
#     order=dClu['stats'],
    baseFile=1,
    index='clu.query("clu!=-1").index & index0',
    aliasFmt='noScore__sureClu',
    panel_kw=panel_kw,
    extra= dict(index0=index0),
)
figs.update([res])

res = sjob.job__render__panelPlot(
    clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
    tracks = tks.trackOrders['allRNA'],
#     order=dClu['stats'],
    baseFile=1,
    index='clu.query("clu!=-1").index & index0',
    aliasFmt='withScore__sureClu__allRNA',
    panel_kw=panel_kw,
    extra= dict(index0=index0),
)
figs.update([res])

keyDF['included'] = keyDF.eval('index in @tks.keyDFTrack.index')
keyDFC = keyDF[['BioName','included']].merge(left_index=True,right_index=True,
                 right=dClu['stats'],how='left').sort_values(['included','clu','score'])
keyDFC.to_html('keyDFC.html')

import warnings

# cluAUC = pyutil.readBaseFile('results/0205__interpAUC__Brachy/clu.csv')

# try:
#     (pyext.base__file('results/0130__callDiffTarg__Brachy-ELF3/DONE'))
    
#     chipClu = pyutil.readBaseFile('results/0130__callDiffTarg__Brachy-ELF3/clu.csv')
#     chipClu.columns = ['clu']
#     peak2gene = pyutil.readBaseFile('results/0130__makePeakWindows__Brachy-ELF3/peak2geneFile.tsv')
#     geneDF  = sdio.peak2gene(peak2gene, chipClu)
#     indCHIP = rnaIndex = geneDF.query('clu==1').feat_acc.unique() 
#     indCHIP = tks.rnaseq.index & indCHIP
#     chipTrack = tks.rnaseq.eval("index.isin(@rnaIndex)")

#     res = sjob.job__render__panelPlot(
#         clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
#         tracks = trackOrders['currentOrder'][:-1] + [
#             tks.rnaseq_wk3ld_wk2ld,
# #             keyDF[['BioName']],
#             tks.keyDFTrack,
#             chipTrack],
#         order=dClu['stats'],
#         baseFile=1,
#         index='clu.query("clu!=-1").index',
#         aliasFmt='withScore__sureClu__withCHIP',
#         panel_kw=panel_kw,
#     )
#     figs.update([res])
    
#     res = sjob.job__render__panelPlot(
#         clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
#         tracks = trackOrders['currentOrder'][:-1] + [
#             tks.rnaseq_wk3ld_wk2ld,
# #             keyDF[['BioName']],
#             tks.keyDFTrack,
#             chipTrack],
#         order=dClu['stats'],
#         baseFile=1,
#         aliasFmt='withScore__allClu__withCHIP',
#         panel_kw=panel_kw,
#     )
#     figs.update([res])


#     res = sjob.job__render__panelPlot(
#         clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
#         tracks = trackOrders['currentOrder'][:-1] + [
#             tks.rnaseq_wk3ld_wk2ld,
#             keyDF[['BioName']],
# #             tks.keyDFTrack,
# #             chipTrack
#         ],
#         order=dClu['stats'],
#         index = indCHIP,
#         baseFile=1,
#         aliasFmt='withScore__chipTarget__withCHIP',
#         panel_kw=panel_kw,
#         figsize=[14,12]
#     )
#     figs.update([res])
    

#     res = sjob.job__render__panelPlot(
#         clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
#         tracks = (
#             ['cluTrack'] + 
#             tks.rnaUniq + 
#             [keyDF[['BioName']],
#             chipTrack]
#                  ),
#         order=dClu['stats'],
# #         index = indCHIP,
#         baseFile=1,
#         aliasFmt='withScore__allClu__withCHIP__allTracks',
#         panel_kw=panel_kw,
#         figsize=[14,20]
#     )
#     figs.update([res])    

#     alias  = 'withScore__sureClu__withCHIP__allTracks'
#     pp = sjob.job__render__panelPlot(
#         clu='results/0129__showCluster__Brachy-RNA-all/clu.csv',
#         tracks = (
#             ['cluTrack'] + 
#              tks.rnaUniq + 
#             [
#                 keyDF[['BioName']],
#             chipTrack,
#             cluAUC.ppd1__up,
#             cluAUC.ppd1__down,
#             ]),
#         order=dClu['stats'],
#         index='clu.query("clu!=-1").index',
#         baseFile=1,
#         aliasFmt=alias,
#         panel_kw=panel_kw,
#         figsize=[14,20],
#         debug=1,
#     )
#     pp.bigTable.to_csv('%s.csv' % alias)
#     fig = pp.render()
#     res = (alias, fig)
#     figs.update([res])        
    
# except Exception as e:
#     warnings.warn(str(e))

pyutil.render__images(figs,exts=['png','svg'])
pyutil.sys.exit()


