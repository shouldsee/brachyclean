#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

# bwFiles = \
# ['Mapped_data/188CR/S1/64-LD-ZT0-ELF3-OX-RERUN_S1_RPKM.bw',
#  'Mapped_data/188CR/S2/64-SD-ZT0-ELF3-OX-RERUN_S2_RPKM.bw',
#  'Mapped_data/188CR/S3/64-LL-ZT0-ELF3-OX-RERUN_S3_RPKM.bw',
#  'Mapped_data/188CR/S4/64-LD-ZT4-ELF3-OX-RERUN_S4_RPKM.bw',
#  'Mapped_data/188CR/S5/64-SD-ZT4-ELF3-OX-RERUN_S5_RPKM.bw',
#  'Mapped_data/188CR/S7/64-LD-ZT20-ELF3OX-RERUN_S7_RPKM.bw',
#  'Mapped_data/188CR/S8/64-SD-ZT20-ELF3OX-RERUN_S8_RPKM.bw']
# bwFiles = map(pyext.base__file,bwFiles)

bwCurr= pyutil.readBaseFile('results/0201__dumpMeta__Brachy/bwCurr.csv')
bwFiles = bwCurr.RPKMFile.map(pyext.base__file)

bedFile = pyext.base__file('results/0130__makePeakWindows__Brachy-ELF3/windowFile.bed')
bwTrack = sutil.extract_bigwig_multiple(fnames=bwFiles,
#                                          outIndex=None,
                                        bedFile=bedFile,
                                        radius=None,
                                        stepSize=5,
                                        center_summit = 1,
                                        NCORE=5)

bwAvg = pyutil.colGroupMean(bwTrack).apply(pyutil.log2p1)
bwTrack.to_pickle('bwTrack.pk')
bwAvg.to_pickle('bwAvg.pk')