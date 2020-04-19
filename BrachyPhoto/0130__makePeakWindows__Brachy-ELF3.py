#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()


# npkFiles = \
# ['Mapped_data/188CR/S1/64-LD-ZT0-ELF3-OX-RERUN_S1_peaks.narrowPeak',
#  'Mapped_data/188CR/S2/64-SD-ZT0-ELF3-OX-RERUN_S2_peaks.narrowPeak',
#  'Mapped_data/188CR/S3/64-LL-ZT0-ELF3-OX-RERUN_S3_peaks.narrowPeak',
#  'Mapped_data/188CR/S4/64-LD-ZT4-ELF3-OX-RERUN_S4_peaks.narrowPeak',
#  'Mapped_data/188CR/S5/64-SD-ZT4-ELF3-OX-RERUN_S5_peaks.narrowPeak',
#  'Mapped_data/188CR/S7/64-LD-ZT20-ELF3OX-RERUN_S7_peaks.narrowPeak',
#  'Mapped_data/188CR/S8/64-SD-ZT20-ELF3OX-RERUN_S8_peaks.narrowPeak']
# npkFiles = map(pyext.base__file,npkFiles)

bwCurr= pyutil.readBaseFile('results/0201__dumpMeta__Brachy/bwCurr.csv')
bwCurr = bwCurr.query('bname.str.contains("ELF3",case=0)')
npkFiles = bwCurr.npkFile.map(pyext.base__file)



# bwCurr = bwMeta.query("runID=='188CR'")
# bwCurr = bwCurr.query('bname.str.contains("ELF3",case=0)')
fnames = map(
    pyutil.functools.partial(
        pyutil.queryCopy,
        inplace=False,
        query='FC>2.0',
        reader=sdio.extract_peak),
    npkFiles)
peakFile = ofname = sdio.bed__merge( 
    pyutil.file__cat(fnames,ofname='combined__ELF3__peaks.narrowPeak')
)
print (ofname,pyutil.lineCount(ofname))
windowFile = ofname = sdio.bed__makewindows(peakFile, windowSize=100,stepSize=50,silent=0)


# pyext.os.environ['BASE'] = '/home/feng'
cdsFile = pyext.base__file('ref/Brachypodium_Bd21_v3-1/annotation/Bdistachyon_314_v3.1.gene_exons.gtf.cds')
GSIZE = pyext.base__file('ref/Brachypodium_Bd21_v3-1/genome.sizes')

peakSummit = sutil.bed__summit(peakFile,GSIZE=GSIZE)
windowSummit = sutil.bed__summit(windowFile,GSIZE=GSIZE)
peak2geneFile = sdio.job__nearAUG(peakSummit=windowSummit,
                                  GSIZE=GSIZE,
                           featSummit=sdio.bed__leftSummit(cdsFile,
                                                           inplace=False,
                                                           GSIZE=GSIZE),
                           CUTOFF=6000,
                            peakWid=1,
                          )

pyext.file__rename(
{peakSummit:'peakSummit.bed',
 peak2geneFile:'peak2geneFile.tsv',
 windowFile:'windowFile.bed',
 windowSummit:'windowSummit.bed'
},force=1)


# import shutil
# shutil.