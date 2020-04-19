#!/usr/bin/env python
# -*- coding: utf-8 -*-
NCORE=6
import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

fig,ax = plt.subplots(1,1,figsize=[7,7])
axs = [None,ax,None]
plt.rcParams['font.size'] = 20.
plt.rcParams['xtick.labelsize'] = 22.
plt.rcParams['axes.titlepad'] = 24.



# execfile('/home/feng/meta/header__script2figure.py')
# import synotil.chipShot
keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
# keyDF = pyutil.readData('/home/feng/meta/key_brachy.csv')
# GSIZE = 
GSIZE= pyext.base__file('ref/Brachypodium_Bd21_v3-1/genome.sizes')
# gconf = pyutil.envSource('/home/feng/ref/config/config_Bd21-3.sh',silent=1);
# gconf = pyutil.util_obj(**gconf)


bwCurr= pyutil.readBaseFile('results/0201__dumpMeta__Brachy/bwCurr.csv')
# bwCurr = bwCurr.query('bname.str.contains("ELF3",case=0)')
# bwFiles = bwCurr.RPKMFile.map(pyext.base__file)

# bwCurr = bwMeta.query('runID=="182C"').query('bamFinal.str.contains("TAIR10")')

# bwCurr = bwMeta
# bwCurr.bname=bwCurr.bname.str.split('_').str.get(0)
bwCurr['bnameShort']=bwCurr.bname.str.split('_').str.get(0)
bwCurr = bwCurr.query('runID=="188CR"')

bwFlat = ' '.join(bwCurr.RPKMFile)

bwCurr.header = bwCurr.bnameShort
bwCurr.header = bwCurr.header.str.replace("GFP|RERUN|64|FLAG",'')
bwCurr.header = bwCurr.header.str.replace("-+",'-').str.strip('-')


rec1 = bwCurr.loc['188CRS8']
for rec2 in [
    bwCurr.loc['188CRS9'],
    bwCurr.loc['188CRS10'],
]:
#     rec2 = bwCurr.loc['188CRS8']


    peak1,peak2 = map(
        funcy.compose(
            pyutil.functools.partial(pyutil.queryCopy, query = 'FC>2.0',reader = sdio.extract_peak),
            pyutil.functools.partial(sdio.npk_expandSummit,radius=1),
            pyext.base__file,
        ),
        [rec1.npkFile, rec2.npkFile]
    )

    res = sutil.qc_summitDist(peak1=peak1,peak2=peak2,
                        xlab=rec1.header,ylab=rec2.header,
                        CUTOFF=1000,GSIZE=GSIZE,
                        query='FC>2.0',
                       );
    res[0].to_csv('peakVenn__%s__%s.csv' % (rec1.name,rec2.name))

    figs['venn__peakLevel__%s'%rec2.name] = plt.gcf()


    pyutil.render__images(figs,exts=['png','svg'])

# execfile('/home/feng/meta/footer__script2figure.py')