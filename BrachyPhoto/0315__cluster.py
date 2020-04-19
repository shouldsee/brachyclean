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

pcount = 0.137
tdf = tdf.apply(lambda x:np.log2( 1 + (2**(x) - 1)/pcount ) )

# tdf = pyext.readBaseFile('results/0314__prefiltering/out.csv')

dfc = tdf.copy()
dfc = dfc.astype('float')

def dropByNonZeroCount(dfc,threshold = 2, inplace=0):
    SUM = (dfc!=0).sum(axis=1)
    toDrop = SUM.to_frame('SUM').query('SUM<%d' % threshold).index
    dfc = dfc.drop(index=toDrop,inplace=inplace)
    return dfc
    


def prefilter(dfc):
#     dfc = dfc.apply(pyutil.log2p1)
    dfc = sutil.stdNorm(dfc)
    return dfc


dfc = dropByNonZeroCount(dfc,3,inplace=False)
quick = 0
start,end = [0.5, 3.]
XCUT = 40
YCUT = 1.5
figsize=[22,8]
keys =  [u'Age',  u'ZTime', u'gtype', u'light',]


XCUT = 75
YCUT = 2.7
figsize=[22,8]
keys =  [  u'light',u'ZTime', u'gtype',]

#### start clustering
dfc = prefilter(dfc)
if quick:
    mdl0 = pyjob.vmfMixture__anneal(dfc, start, end,K=10,
                                    nIter=50)

else:
    mdl0 = pyjob.vmfMixture__anneal(dfc, start, end,K=30,
                                    nIter=200)

np.save('mdl0.npy',mdl0)
pycbk.qc__vmf__speed(mdl0,XCUT=XCUT,YCUT=YCUT)
figs['qcVMF'] = plt.gcf()


##### Post visualisation

# mdl0 = np.load('mdl0.npy').tolist()


mdl = mdl0.callback.mdls[XCUT][-1]
clu  = mdl.predictClu(mdl0.data,entropy_cutoff = YCUT,index=mdl0.data.index)
# score = mdl.score(mdl0.data)
score = pyutil.logsumexp( 
    mdl._log_pdf(mdl0.data),axis=1)
clu['score'] = score
print pyutil.get_cluCount(clu).T


vdf = dfc.copy()
vdf = vdf.reindex(columns = rnaCurr.index & vdf.columns)
vdf=  scount.countMatrix(vdf,colMeta = rnaCurr)
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

if 1:
    pp = spanel.panelPlot([spanel.fixCluster(clu['clu']), 
                           vdf,
                          ],figsize=figsize,
                          width_ratios=[2,10,0],

                           show_axa=1
                         )
    index = clu.query('clu>=-1 & score > 10.').index
    if len(index)==0:
        index = None
    pp.render(order = clu,
              index = index
             );
    
    figs['heatmap-filter'] = fig
pyutil.render__images(figs)
    # ;pp.render(order = clu,
    #           index = clu.query('clu>=0').index);