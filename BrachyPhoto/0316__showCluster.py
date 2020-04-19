#!/usr/bin/env python
import pymisca.header as pyheader
pyheader.execBaseFile('headers/header__import.py')
figs = pyext.collections.OrderedDict()

np.random.seed(0)

tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
tdf = tks.rnaseq
tdf = scount.countMatrix(tdf)

rnaCurr = pyext.readBaseFile('results/0130__makeTracks-Brachy/rnaCurr.csv')
tdf = tdf.filter(axis=1,items=rnaCurr.query('Age=="Wk3"').index)

# tdf = pyext.readBaseFile('results/0314__prefiltering/out.csv')

dfc = tdf.copy()
dfc = dfc.astype('float')

def dropByNonZeroCount(dfc,threshold = 2, inplace=0):
    SUM = (dfc!=0).sum(axis=1)
    toDrop = SUM.to_frame('SUM').query('SUM<%d' % threshold).index
    dfc = dfc.drop(index=toDrop,inplace=inplace)
    return dfc
    

dfc = tdf = dropByNonZeroCount(dfc,2,inplace=False)
# dfc = tks.
# dfc = tks.rnaseq_wk3ld_elf3ko.reindex(dfc.index).dropna()

# def prefilter(dfc):
# #     dfc = dfc.apply(pyutil.log2p1)
# #     dfc = dfc.setDF(dfc.values / pyutil.l2norm(dfc.values,axis=1,keepdims=1))
# #     dfc = dfc.dropna()
#     dfc = sutil.stdNorm(dfc.copy())
#     return dfc

dfc = tdf.copy()
def prefilter(dfc):
#     dfc = dfc.apply(pyutil.log2p1)
    dfc = dfc.setDF(dfc.values - dfc.values.min(axis=1,keepdims=1))
    dfc.qc_Avg();
    dfc = dfc.setDF(dfc.values / np.sqrt(dfc.summary.MSQ.values[:,None]))
#     dfc = sutil.stdNorm(dfc,meanNorm=0)
    return dfc


quick = -1
start,end = [0.01, 10.]

XCUT = 75
YCUT = 2.0
XCUT = 100
YCUT = 1.5
figsize=[22,8]
keys =  [  u'light',u'ZTime', u'gtype',]

#### start clustering
dfc = prefilter(dfc)
if quick==1:
    mdl0 = pyjob.vmfMixture__anneal(dfc, start, end,K=10,
                                    nIter=50)

elif quick==0:
    mdl0 = pyjob.vmfMixture__anneal(dfc, start, end,K=30,
                                    nIter=200)
if quick==-1:
    mdl0 = pyext.readBaseFile('results/0316__cluster/mdl0.npy').tolist()
else:
    np.save('mdl0.npy',mdl0)
    
pycbk.qc__vmf__speed(mdl0,XCUT=XCUT,YCUT=YCUT)
figs['qcVMF'] = plt.gcf()


##### Post visualisation
# mdl0  = pyu
# mdl0 = np.load('mdl0.npy').tolist()


mdl = mdl0.callback.mdls[XCUT][-1]
clu  = mdl.predictClu(mdl0.data,entropy_cutoff = YCUT,index=mdl0.data.index)
# score = mdl.score(mdl0.data)
score = pyutil.logsumexp( 
    mdl._log_pdf(mdl0.data),axis=1)
clu['score'] = score
print pyutil.get_cluCount(clu).T


# vdf = dfc.copy()
vdf = mdl0.data.copy()
vdf = vdf.reindex(columns = rnaCurr.index & vdf.columns)
vdf=  scount.countMatrix(vdf,colMeta = rnaCurr,height=10)
# vdf =sutil.sumNorm(scount.countMatrix(rnaTable.astype(float),
#                                      colMeta =rnaCurr))
# .apply(np.sqrt)
vdf.relabel(colLabel=keys)

# clu.clu.replace({0:3,1:3,2:3},inplace=True)

if 1:
    clu.hist('score',bins=30)
    figs['hist-score'] = plt.gcf()

if 1:
    pp = spanel.panelPlot([spanel.fixCluster(clu['clu']), 
                           vdf,
                          ],figsize=figsize,
                          width_ratios=[2,10,0],

                           show_axa=1
                         )
    # pp.render(order = clu )
    fig = pp.render(order = clu,
              index = clu.query('clu>=-1').index
             );
    figs['heatmap-all'] = fig


##### Another heatmap
figsize=[15,15]
indVenn = pyutil.readBaseFile('results/0205__venn__Brachy-funcTarg/venn_index.csv',guess_index=0)
chipTrack  = clu.eval("index in @indVenn.ind2")
blacklist = '''
196RS1
196RS2
196RS3
196RS4
196RS5
196RS6
196RS7
196RS8
'''.strip().splitlines()

# vdf = dfc.copy()
# vdf = vdf.reindex(columns = rnaCurr.index &\
#                   (rnaCurr.index ^ pd.Index(blacklist)) &\
#                   vdf.columns )
# vdf=  scount.countMatrix(vdf,colMeta = rnaCurr,height=10)
# vdf.relabel(colLabel=keys)

# vdf = vdf.reindex(columns=vdf.columns 
if 1:
    pp = spanel.panelPlot([spanel.fixCluster(clu['clu']), 
                           chipTrack,
                           vdf,
                          ],figsize=figsize,
                          width_ratios=[2,10,0],

                           show_axa=1
                         )
    cluc = clu.query('clu> -1 & score > 4.')
    index = cluc.index
    if len(index)==0:
        index = None
    fig =pp.render(order = clu,
              index = index
             );
    
    figs['heatmap-filter'] = fig

    
    
clu.to_csv('raw-clu.csv')
cluc.to_csv('filtered-clu.csv')
    
#### Output annotated csv
gconf=  pyutil.readBaseFile('results/0205__makeGCONF/gconf.npy',baseFile='/home/feng/work').tolist()
labeller = funcy.partial( pyutil.meta__label,gconf.geneMeta)
res = labeller(cluc)

pyutil.printlines(sutil.tidyBd(cluc.query('clu==3')).index,'temp.txt')
res.query('clu==3')[['Best-hit-arabi-name','score']].dropna().to_csv('temp.txt',sep='\t',index=0)
res.to_csv('labelled-clu.csv')



#### Add GOI
keyDF = pyext.readBaseFile('headers/key_brachy.csv')
pyutil.mergeByIndex(keyDF[['BioName']],clu,'left').sort_values(['clu','score']).to_csv('marker-clu.csv')

pyutil.render__images(figs)