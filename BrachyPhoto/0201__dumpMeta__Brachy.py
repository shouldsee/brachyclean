#!/usr/bin/env python
# -*- coding: utf-8 -*-

NCORE = 1
import pymisca.ext as pyext
pyext.execBaseFile('headers/header__import.py')
figs = pyutil.collections.OrderedDict()

meta = pyutil.readBaseFile('meta/meta_rna.tsv')
meta.sort_values(["SpecAcc",
                  "gtype",
                  "Age",
                  "light",
                  "temp",
                  "ZTime_int"],inplace=True)

mcurr = meta.query('SpecAcc=="Bd" ')
mcurr = mcurr.query('gtype not in ["Martin","apices"]')

rnaMeta = pyutil.readData('/home/feng/meta/meta_rna_prog.tsv')
rnaCurr = rnaMeta.query('~index.duplicated()').reindex(mcurr.index)
rnaCurr = rnaCurr[['fname']].merge(mcurr.drop(columns='fname_'),left_index=True,right_index=True)

for key in ['fname',]:
    rnaCurr[key] = rnaCurr[key].str.extract('([^/]+/Mapped_data/.*)')[0].tolist()
rnaCurr.to_csv('rnaCurr.csv')
print('[rnaCurr]')
print(rnaCurr.head().to_csv(sep='\t'))

bwMeta = pyutil.readData('/home/feng/meta/meta_chip.tsv')
bwCurr = bwMeta.query("runID=='188CR'")
# bwCurr = bwCurr.query('bname.str.contains("ELF3",case=0)')
for key in ['RPKMFile','npkFile','bamAcc','bamFinal']:
    bwCurr[key] = bwCurr[key].str.extract('([^/]+/Mapped_data/.*)')[0].tolist()
bwCurr.to_csv('bwCurr.csv')
print('[bwCurr]')
print(bwCurr.head().to_csv(sep='\t'))

# bwCurr.npkFile = bwCurr.npkFile.str.extract('(Mapped_data/.*)')[0].tolist()

# print mcurr.head()

