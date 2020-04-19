#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

bwCurr= pyutil.readBaseFile('results/0201__dumpMeta__Brachy/bwCurr.csv')
bwCurr = bwCurr.query('bname.str.contains("phyc",case=0)')
bwCurr.npkFile = bwCurr.npkFile.map(pyext.base__file)
print (bwCurr)

# npkFiles = bwCurr.npkFile.map(pyext.base__file)
# print npkFiles


gconf=  pyutil.readBaseFile('results/0205__makeGCONF/gconf.npy').tolist()

rec1 = bwCurr.loc['188CRS9']
rec2 = bwCurr.loc['188CRS10']
npkFiles = [rec1['npkFile'], rec2['npkFile']]
peakFiles = map(
    pyutil.functools.partial(sdio.npk_expandSummit,radius=1),
    npkFiles)
peakFiles = map(
    pyutil.functools.partial(
        pyutil.queryCopy,
        inplace=False,
        query='FC>3.0',
        reader=sdio.extract_peak),
    peakFiles)

peakFile = pyutil.file__cat(peakFiles,ofname='combined__PHYC__peaks.narrowPeak')

gconf.CDS = gconf.GTF + '.cds'
peakSummit = sutil.npk_expandSummit(peakFile,radius=1)
peak2geneFile = sdio.job__nearAUG(peakSummit=peakSummit,
                                  GSIZE=gconf.GSIZE,
                           featSummit=sdio.bed__leftSummit(gconf.CDS,
                                                           inplace=False,
                                                           GSIZE=gconf.GSIZE),
                           CUTOFF=6000,
                            peakWid=1,
                          )
peak2gene = pyutil.readData(peak2geneFile)

res =  sutil.qc_summitDist(
    peak1=peakFiles[0],
    peak2=peakFiles[1],
    query='FC>3.0',
    CUTOFF=1000,
    GSIZE=gconf.GSIZE,
    xlab=rec1.header,
    ylab=rec2.header,
);
figs['peakVenn']= plt.gcf()

interDF = res[0].query('distance < 200')
                       
res1= sdio.peak2gene( peak2gene, interDF[['acc']].set_index('acc'))
res2= sdio.peak2gene( peak2gene, interDF[['feat_acc']].set_index('feat_acc'))

ress = pyvis.qc_index( res1.feat_acc, res2.feat_acc, silent=0);
figs['geneVenn'] = plt.gcf()

geneAcc = pd.Index(ress[0].indAll.dropna()).to_frame('geneAcc')
# .set_index('indAll')
geneRes = pyext.meta__label(gconf.geneMeta,geneAcc)
geneRes.to_csv('geneRes__phyC-target.csv')
peakDF = sdio.gene2peak(peak2gene, geneRes,)
peakDF.to_csv('peakDF__phyC-target.csv')

pyext.file__rename(
{peakSummit:'peakSummit.bed',
 peak2geneFile:'peak2geneFile.tsv',
#  windowFile:'windowFile.bed',
#  windowSummit:'windowSummit.bed'
},force=1)

pyutil.render__images(figs,exts=['png','svg'])
