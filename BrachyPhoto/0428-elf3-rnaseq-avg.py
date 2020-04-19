#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pymisca.header as pyhead
pyhead.base__check()
execfile(pyhead.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

rnaDF = pyext.readBaseFile('results/0427-dump-rna/pk/read-topped-log2.pk')

rnaDF = pyext.readBaseFile('results/0427-dump-rna/pk/read-topped-log2.pk')
rnaCurr = pyext.readBaseFile('results/0427-dump-rna/rnaCurr.csv')

clu = pyext.readBaseFile('results/0408-freezerCluster/0427-dump-rnapkread-topped-log2-meannormpk/baseDist-vmfDistribution_seed-0/clu.csv')

chipTarg = pyext.readBaseFile('results/0427-heatmap-brachy/withScore__chipTarg__withCHIP__allTracks.csv')

rnaDF.columns = rnaDF.columns.str.split('_').str.get(-1)
rnaCurr = rnaCurr.reindex(rnaDF.columns)
rnaCurr.columns = rnaCurr.columns.str.upper()


qc__subsets = pyvis.qc__subsets    
mcurr = rnaCurr.copy()
_dict = pyext.collections.OrderedDict
# COLS = None
# COLS = ['AGE','GTYPE','LIGHT']
rnaDFC  =rnaDF.copy()

res = pyvis.qc_index(chipTarg.index, rnaDFC.index,
               xlab='ELF3-differentially-bound',
              ylab='significantly-expressed',
                silent=0)
res[0].to_csv('target-venn.csv')
figs['target-venn'] = plt.gcf()

rnaDFC  = rnaDFC.reindex(chipTarg.index).dropna()
# rnaDFC  = rnaDF.reindex(clu.index)
rnaDFC = rnaDFC.dropna()
print rnaDFC.shape

nrow  = 3
fig,axs=plt.subplots(3,2,sharex='col',
                     gridspec_kw=dict(width_ratios=[4,1]),
                     figsize=[12,nrow*4])
i = -1
DQ = [
 _dict(AGE='Wk2', GTYPE='Bd21', LIGHT='SD'),
 _dict(AGE='Wk2', GTYPE='Bdelf3', LIGHT='SD'),
]
i+=1;_axs = axs[i]
axs_ = qc__subsets(rnaDFC, mcurr,DQ, index='ZTIME_INT',
           xlab='ZTIME_INT', ylab='Average log2(TPM)',axs=_axs)

# DATA_QUERYS = [
#  _dict(AGE='Wk2', GTYPE='Bd21', LIGHT='LD'),
#  _dict(AGE='Wk2', GTYPE='Bdelf3', LIGHT='LD'),
# ]
# i+=1;_axs = axs[i]
# axs_ = qc__subsets(rnaDF.reindex(clu.index),mcurr,DATA_QUERYS, index='ZTIME_INT',
#            xlab='ZTIME_INT', ylab='Average log2(TPM)',axs=_axs)

DQ = [
 _dict(AGE='Wk3', GTYPE='Bd21', LIGHT='SD'),
 _dict(AGE='Wk3', GTYPE='Bdelf3', LIGHT='SD'),

]
i+=1;_axs = axs[i]
axs_ = qc__subsets(rnaDFC,mcurr,DQ, index='ZTIME_INT',
           xlab='ZTIME_INT', ylab='Average log2(TPM)',axs=_axs)

DQ = [
 _dict(AGE='Wk3', GTYPE='Bd21', LIGHT='LD'),
 _dict(AGE='Wk3', GTYPE='Bdelf3', LIGHT='LD'),

]
i+=1;_axs = axs[i]
axs_ = qc__subsets(rnaDFC, 
                   mcurr,
                   DQ,
                   index='ZTIME_INT',
           xlab='ZTIME_INT', ylab='Average log2(TPM)',axs=_axs)
axs[0][0].set_title('GeneSet: Directly bound ELF3 targets with significant expression')

figs['main'] = fig
pyutil.render__images(figs,exts=['png','svg'])