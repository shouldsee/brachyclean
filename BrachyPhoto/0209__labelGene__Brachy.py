#!/usr/bin/env python
# -*- coding: utf-8 -*-

assert 0,"[Obsolete] see: BrachyPhoto/0211__outputSupp__Brachy.py"

import pymisca.ext as pyext
NCORE = 10
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()
# tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
gconf=  pyutil.readBaseFile('results/0205__makeGCONF/gconf.npy').tolist()

# clu.sort_values('clu')

fname = 'results/0129__showCluster__Brachy-RNA-all/clu.csv'

# 'results/
lst = '''
results/0205__venn__Brachy-funcTarg/funcTarg.csv
#results/0129__showCluster__Brachy-RNA-all/clu.csv
results/0214__heatmap__Brachy-all/clu.csv
'''.strip().splitlines()

for fname in lst:
    dfc =pyutil.readBaseFile(fname)
    geneRes = pyutil.meta__label( gconf.geneMeta,  dfc)
    ofname = fname.replace('/','____').rsplit('.',1)[0] +'.xls'
    geneRes.to_excel(ofname)
#     geneRes.to_csv(pyutil.os.path.basename(fname))
