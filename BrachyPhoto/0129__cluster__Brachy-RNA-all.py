#!/usr/bin/env python
# -*- coding: utf-8 -*-

NCORE = 10
import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
figs = pyutil.collections.OrderedDict()

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

mdl0 = pyjob.job__cluster__mixtureVMF__incr(
#     normalizeSample=1,
    tdf=tdf,
    meanNorm=0,
    init_method='random',
    nIter=250,
    start=0.001,
    end=7.0,
    verbose=2,
    K=80,)

axs = pyjob._mod1.qc__vmf(mdl0)
fig = plt.gcf()
ax=  fig.axes[0]
pyvis.abline(y0=3.7,k=0,ax=ax)

figs['qcVMF'] = fig

pyutil.render__images(figs,)