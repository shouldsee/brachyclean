#!/usr/bin/env python

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

# execfile('/home/feng/meta/header_0903.py')
keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
tks = pyext.readBaseFile('results/0427B__makeTracks-Brachy/tracks.npy').tolist()
# tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
# execfile("/home/feng/envs/Fig_Brachy/loadRNA_Bd.py")
# figs = pyutil.collections.OrderedDict()

plt.rcParams['font.size'] = 12.
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


RANDOM_SEED = 1101
###### [important]
cluFile = 'results/0129__showCluster__Brachy-RNA-all/clu.csv'
clu  = pyext.readBaseFile(cluFile)
cluTrack = spanel.fixCluster(clu)
cluTrack['clu'] = cluTrack['clu'].astype('str')# cluAUC = pyutil.readBaseFile('results/0205__interpAUC__Brachy/clu.csv')
dClu = pyutil.readBaseFile('results/0129__showCluster__Brachy-RNA-all/cache.npy').tolist()

pyext.np.random.seed(RANDOM_SEED)
stats = dClu['stats']
stats.insert(1,'randomScore',pyext.np.random.random(size=len(stats)))
#### randomise the genes


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
    chipTrack.columns = ['ChIP']


    

################## main figure
res = sjob.job__render__panelPlot(
    clu=cluFile,
    tracks = (
        [cluTrack] + 
        tks.trackOrders['main'][1:]
        + [chipTrack]
             ),
    order=dClu['stats'],
    index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= 'sureClu__mainFigure',
    panel_kw=panel_kw,
    figsize=[14,10],
    returnPanel=1,
)
pp = res[-1]; name = res[0]; pp.bigTable[[]].to_csv('%s.csv'%name)
figs.update([res[:2]]) 

############## supplement figure
res = sjob.job__render__panelPlot(
    clu=cluFile,
    tracks = (
        [cluTrack] + 
        tks.trackOrders['allRNA'][1:]
        + [chipTrack]
             ),
    order=dClu['stats'],
    index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= 'sureClu__supplementFigure',
    panel_kw=panel_kw,
    figsize=[14,20],
    returnPanel=1,
)
pp = res[-1]; name = res[0]; pp.bigTable[[]].to_csv('%s.csv'%name)
figs.update([res[:2]]) 


#######################  chipTargets-main
res = sjob.job__render__panelPlot(
    clu=cluFile,
    tracks = (
        [cluTrack] + 
        tks.trackOrders['main'][1:-1] 
        + [ tks.keyDFTrack2 ]
        + [chipTrack]
             ),
    order=dClu['stats'],
    index = indCHIP,
#     index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= 'sureClu__mainFigure__chipTarget',
    panel_kw=dict(panel_kw.items() + [('title','')] ),
    figsize=[14,10],
    returnPanel=1,
)
pp = res[-1]; name = res[0]; pp.bigTable[[]].to_csv('%s.csv'%name)
# fig = res[1]
# fig.axes[1].set_title('')

figs.update([res[:2]])  


####################### chipTargets-supp
res = sjob.job__render__panelPlot(
    clu=cluFile,
    tracks = (
        [cluTrack] + 
        tks.trackOrders['allRNA'][1:-1] 
        + [ tks.keyDFTrack2 ]
        + [chipTrack]
             ),
    order=dClu['stats'],
    index = indCHIP,
#     index='clu.query("clu!=-1").index',
    baseFile=1,
    aliasFmt= 'sureClu__suppFigure__chipTarget',
    panel_kw=dict(panel_kw.items() + [('title','')] ),
    figsize=[14,20],
    returnPanel=1,
)
pp = res[-1]; name = res[0]; pp.bigTable[[]].to_csv('%s.csv'%name)
figs.update([res[:2]])  



# res = sjob.job__render__panelPlot(
#     clu=cluFile,
#     tracks = (
#         [        
# #             'cluTrack',
#             cluTrack,
#             tks.rnaseq_wk3wt,
#             tks.rnaseq_wk3elf3ld_wk3elf3sd ,
#             tks.keyDFTrack,
#             chipTrack,
#         ]
#      ),
#     order=dClu['stats'],
#     index='clu.query("clu!=-1").index',
#     baseFile=1,
#     aliasFmt= 'withScore__sureClu__withCHIP__wk3ldsd-elf3ldsd',
#     panel_kw=panel_kw,
#     figsize=[14,7]
# )
# figs.update([res])  

pyutil.render__images(figs,exts=['png','svg'])