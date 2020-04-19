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
figsize=[14, 7]
common = dict(
    figsize=figsize,
    show_axa = 1,
    show_axc = 0,
    showGrid = 0,
    width_ratios = [1,14,0.]
#     title= '',
#     height_ratios = [1,3,3,3,1],
    )

def worker( (cluFile, trackOrderName,index,order,prefix)):
    tracks = trackOrder = trackOrders[trackOrderName]
    if not isinstance(cluFile,basestring):
        index = cluFile
    if prefix is None:
        prefix=''
#     if isinstance(index,basestring):
#         index = pyutil.readData(index)
    
#     import maptlotlib.pyplot as plt
#     import synotil.PanelPlot 
    # cluFile = '/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__ppd1__K=40.csv'
    cluName = pyutil.basename(cluFile)
    alias = '{cluName}_{trackOrderName}_{prefix}'.format(**locals())
#     cluFile = pyext.base__file(cluFile)
    clu = scount.countMatrix(pyutil.readData(cluFile,
                                             baseFile = 1
                                            ).get(['clu']))
    if order is None:
        order = clu
    # clu = scount.countMatrix(pyutil.readData('1130__rnaCluster__hpm__ppd1__K=40.csv').get(['clu']))
    # clu = scount.countMatrix(pyutil.readData('1130__rnaCluster__GMM__ppd1.csv').get(['clu']))


    cluTrack = spanel.fixCluster(clu)
    cluTrack.height = 0.3
    tracks = pyext.list__realise(tracks,locals())

    ##### Output genes as standardised accessions
    cluc  = sutil.tidyBd(clu)
    cluFile_clean = 'clean_%s.csv' % alias
    cluc.to_csv(cluFile_clean)
    pyutil.MDFile(cluFile_clean)
    figs = []

    ##### Output heatmap
    pp = spanel.panelPlot(tracks,**common)
    pp.compile(
        order=clu,
        how='left',
#         index=index,
              )
#     fig = pp.render();
#     figs += [('heatmap__' + cluName,fig )]
    
    ####
#     clu = pyutil.readData(cluFile)
    cluCount = pyutil.get_cluCount(clu)
    if not cluCount.query('clu==-1').empty:
        cluSmall = cluCount.query('clu != -1')
    else:
        cluSmall = cluCount.query('count < 2000')
    pp = spanel.panelPlot(tracks,**common)
    pp.compile(order=order,how='left',
               index=pd.DataFrame(clu).query("clu in @cluSmall.clu").index,
              )
#     fig2 = pp.render();
    fig = pp.render();
    figs += [('heatmapForSmallClu__' + alias,fig )]
    
    ####
    ci = clu.loc['Bradi1g48830.v3.1'].values[0]
    cluc = pd.DataFrame(clu).query("clu==@ci")
    pp = spanel.panelPlot(tracks,**common)
    pp.compile(order=clu,how='left',
               index=cluc.index
              )
    fig = pp.render();
#     figs += [('heatmapForFTCluster__' + alias,fig )]
    
#     clu.query("index=='Bradi1g48830.v3.1'")
    
    return figs
#     figs['heatmap__' + cluName] = fig
#     return fig

NCORE=1

trackOrders = {
    'order1':[
        'cluTrack',
#         chipTrack,
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
        tks.rnaseq_wk4ldphyc_wk4ldwt,
#         rnaseq_wk3ldppd1_wk3ldwt,
#         rnaseq_wk3ld_wk2ld,
#         rnaseq_wk3ld_elf3ko,
        tks.keyDFTrack,
    ],
    'order2':[
        'cluTrack',
#         chipTrack,
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
#         tks.rnaseq_wk4ldphyc_wk4ldwt,
#         rnaseq_wk3ldppd1_wk3ldwt,
#         rnaseq_wk3ld_wk2ld,
#         rnaseq_wk3ld_elf3ko,
        tks.keyDFTrack,
    ],    
    'order3':[
        'cluTrack',
#         chipTrack,
        tks.rnaseq_wk2wt,
#         rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
#         rnaseq_wk4ldphyc_wk4ldwt,
#         rnaseq_wk3ldppd1_wk3ldwt,
        tks.rnaseq_wk3ld_wk2ld,
#         rnaseq_wk3ld_elf3ko,
        tks.keyDFTrack,
    ],        
}
trackOrders['currentOrder'] = trackOrders['order2']

cluFiles = '''
results/0129__showCluster__Brachy-RNA-all/clu.csv
#lists/0129__cluster__Brachy-RNA-all.csv
#/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__WT__K=40.csv
#/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__allSamples__K=60.csv
#/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__wk3ldsd_wk2ldsd_wk3wk2ld__K=40.csv
#/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__ppd1__K=40.csv
'''.strip().splitlines()
cluFiles = [x for x in cluFiles if not x.startswith('#')]

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))

# cluFile = cluFiles[0]
dClu = pyutil.readBaseFile('results/0129__showCluster__Brachy-RNA-all/cache.npy').tolist()
dClu = pyutil.util_obj(**dClu)
it = (
#     ('/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__WT__K=40.csv', 'order3', chipTarg),
    (cluFiles[0], 'currentOrder',None, dClu.stats,None),
    (cluFiles[0], 'currentOrder',None, None,'unordered'),
    (cluFiles[0], 'order1',None, dClu.stats,None),
#     ('/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__WT__K=40.csv', 'currentOrder',None),
#     ('/home/feng/envs/Fig_Brachy/1130__rnaCluster__hpm__WT__K=40.csv', 'order1',None),
)
res = pyutil.mp_map(worker,
                    it,
                    n_cpu=NCORE)
res  = sum(res,[])
figs = pyutil.collections.OrderedDict(res)
# keyDF.to_html('keyDF.html')

if 0:
    peak2gene = pyutil.readData('/home/feng/envs/Fig_Brachy/peak2gene.tsv')    
    chipDB = pyutil.readData('/home/feng/envs/Fig_Brachy/score__1024__chipTarg__ELF3.csv')
    chipDB['isTarg'] = chipDB['score__chipDiff-GT-0dot5andsd__chip-GT-0dot45']
    geneDF  = sdio.peak2gene(peak2gene,chipDB)
    indCHIP = geneDF.query('isTarg').feat_acc.unique()
    chipTrack = scount.countMatrix(rnaseq.eval('index.isin(@indCHIP)').astype(float),
                                   look='tick',
    #                                look='line',

                                  )
    
clu = pyutil.readData(cluFiles[0],baseFile=1)
keyDF= keyDF.merge(clu,left_index=True,right_index=True)
keyDF['included'] = keyDF.eval('index in @tks.keyDFTrack.index')
keyDF = keyDF.sort_values(['included','clu'],ascending=False)
keyDF.to_html('keyDF.html')



dpi = 160
pyutil.render__images(figs,exts=['png','svg'])