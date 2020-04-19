#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
NCORE = 10
execfile(pyext.base__file('headers/header__import.py'))
tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
figs = pyutil.collections.OrderedDict()


ENT_CUTOFF=2.5
ENT_CUTOFF=3.5
STEP = 60


ENT_CUTOFF=4.0
STEP = 25

# mdl0 = pyutil.readBaseFile('results/0211__cluster__Brachy/mdl-86667075.npy').tolist()
fname = 'results/0212__cluster__BrachyNOW/mdl-77315655.npy'
mdl0 = pyutil.readBaseFile(fname).tolist()
# mdl0 = pyutil.readBaseFile('results/0211__cluster__Brachy/mdl.npy').tolist()

# axs = pyjob._mod1.qc__vmf(mdl0,YCUT=ENT_CUTOFF,XCUT=STEP)
axs = pycbk.qc__vmf__speed(mdl0,YCUT=ENT_CUTOFF,XCUT=STEP)
fig = plt.gcf()
figs['qcVMF'] = fig



for STEP in [35,50]:
    mdl = mdl0.callback.mdls[STEP][-1]
    mdl.predict = pyutil.functools.partial(mdl.predict, 
                                                  entropy_cutoff=ENT_CUTOFF)
    # tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
    # data = mdl0.data
    data = tdf = pd.concat([
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
        tks.rnaseq_wk3ldppd1_wk3ldwt,    
    ],axis=1)
    print (data.shape)

    clu0 = clu= mdl.predictClu(data, index = data.index )
    cacheFile = pyutil.cache__model4data(mdl,tdf=data,
                                         ofname='cache.npy')
    # clu0 = clu= mdl.predictClu(mdl0.data, entropy_cutoff=ENT_CUTOFF,index=mdl0.data.index )
    # clu.to_csv()
    clu = clu.sort_values('clu')

    # clu = pyutil.readData('http://172.26.114.34:81/static/results/0129__showCluster__Brachy-RNA-all/clu.csv')
    # vdf = scount.countMatrix( data)
    # vdf = vdf.reindex(clu.index)
    # vdf.heatmap(figsize=[12,12])
    # plt.title('N=%d'%len(vdf))
    # figs['allClu'] = plt.gcf() 

    vdf = scount.countMatrix( data)
    vdf = vdf.reindex(clu.query('clu!=-1').index)
    vdf.heatmap(figsize=[12,12])
    plt.title('N=%d'%len(vdf))
    figs['sureClu_%d' % STEP] = plt.gcf() 

    clu0 = clu0.sort_values('clu')
    clu0.to_csv('clu.csv')

pyutil.render__images(figs,)