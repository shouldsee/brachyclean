#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CUTOFF_PERMAX = 0.4
CUTOFF_PERMAX = 0.0
# CUTOFF_MAX = 2.0
CUTOFF_MAX = 3.

NCORE = 1
import pymisca.ext as pyext
pyext.execBaseFile('headers/header__import.py')
figs = pyutil.collections.OrderedDict()

# meta = pyutil.readBaseFile('meta/meta_rna.tsv')
# meta.sort_values(["SpecAcc","gtype","Age","light","temp","ZTime_int"],inplace=True)
# mcurr = meta.query('SpecAcc=="Bd" ')
# mcurr = mcurr.query('gtype not in ["Martin","apices"]')
# fnames = mcurr.fname_


keyDF = pyutil.readBaseFile('headers/key_brachy.csv')

rnaCurr= pyutil.readBaseFile('results/0201__dumpMeta__Brachy/rnaCurr.csv')
rnaCurr['fnameFull'] = rnaCurr.fname.map(pyext.base__file)
res = pyutil.readData_multiple(rnaCurr.fnameFull, axis=0, baseFile= 0)
# fnames = rnaCurr.fname
tab = res.pivot_table(index='gene_id',values='TPM',columns='fname')
tab=  tab.rename(columns=pyutil.df2mapper( rnaCurr,'fnameFull','index'),)
assert all(tab.columns.isin(rnaCurr.index))
pyutil.printlines(rnaCurr.fnameFull)

tab = tab.loc[~tab.index.str.startswith('STRG'),:]
print (tab.shape)
tab = scount.countMatrix(tab)
tab.to_pickle('rna_raw.pk')


dfc = tab.apply(sutil.log2p1)
dfc.qc_Avg()
axs = pyvis.qc_2var(*dfc.summary[['per_MAX','per_SD']].values.T)
# rnaseq = dfc
pyvis.abline(ax=axs[1],x0=CUTOFF_PERMAX)
figs['qcRaw'] = plt.gcf()

dfc.summary.plot.scatter('per_MAX','MAX')
figs['qcScatter'] = plt.gcf()

dfc = dfc.reindex(dfc.summary.query('per_MAX > {CUTOFF_PERMAX}'.format(**locals())).index)
dfc = dfc.reindex(dfc.summary.query('MAX > {CUTOFF_MAX}'.format(**locals())).index)
dfc.qc_Avg()
pyvis.qc_2var(*dfc.summary[['per_MAX','per_SD']].values.T)
figs['qcClean'] = plt.gcf()

rnaDF = dfc
rnaDF.to_pickle('rna_log2p1_filtered.pk')

pyutil.render__images(figs)