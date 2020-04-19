#!/usr/bin/env python
# -*- coding: utf-8 -*-

NCORE = 3
NJOB = 10
import pymisca.header as pyhead
execfile(pyhead.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()
def loadData():
    tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy',
    #                          baseFile = '/home/feng/envs/BrachyPhoto',
                             ).tolist()


    # keyDF = pyutil.readBaseFile('headers/key_brachy.csv')

    import pymisca.jobs as pyjob

    tdf = pd.concat([
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
        tks.rnaseq_wk3ldppd1_wk3ldwt,    
    ],axis=1)
    return tdf

def loadData():
    import sklearn.datasets as skdat
    data_digit = data = skdat.load_digits()
    din = data['data']
    data_digit.keys()
    y_true = data_digit['target']
    return din

tdf = loadData()



# ##### debugging!!!!!!!!!!!!
# tdf = pyutil.readData('http://172.26.114.34:81/static/results/0129__cluster__Brachy-RNA-all/mdl.npy').tolist().data
# ##### debugging!!!!!!!!!!!!


# lst = [75434668]

# betas = np.linspace(0.001,1.52, 25).tolist() + [1.52] * 25
# for i,r in enumerate(lst):
def getBeta(i):
    betas = [_betas[i]] * 100
    return betas
def worker((i,r)):
#     betas = [3.0] * 25
    betas  = getBeta(i)
    nIter = 100
    alias = 'i-%d_r-%d'%(i,r)
    
    mdl0 = pyjob.job__cluster__mixtureVMF__incr(
    #     normalizeSample=1,
        tdf=tdf,
        meanNorm=1,
        weighted=True,
        init_method='random',
        nIter=nIter,
        start=0.001,
        end=4.0,
        betas = betas,
        randomState = r,
        alias = 'mdl_'+alias,
        verbose=2,
        K=60,)

    axs = pycbk.qc__vmf__speed(mdl0)
    fig = plt.gcf()
    ax=  fig.axes[0]
    pyvis.abline(y0=3.7,k=0,ax=ax)
#     alias = 'qcVMF__i-%d_r-%d'%(i,r)
    figs[alias] = fig
    return (alias,fig)

N = 60
_betas = np.linspace(0, 2.0, N)

np.random.seed(0)
lst = np.random.randint(100000000,size=(N))
it = enumerate(lst)
res = pyutil.mp_map(worker,it,n_cpu=NJOB)
res = res[::60//5]
figs.update(res)

pyutil.render__images(figs,)    
# pyutil.render__images(figs,)