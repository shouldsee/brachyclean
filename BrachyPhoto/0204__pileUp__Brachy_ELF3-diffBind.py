#!/usr/bin/env python
# -*- coding: utf-8 -*-
NCORE=6
import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()
# execfile('/home/feng/meta/header__script2figure.py')
# import synotil.chipShot
keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
# gconf = pyutil.envSource('/home/feng/ref/config/config_Bd21-3.sh',silent=1);
# gconf = pyutil.util_obj(**gconf)
# peak2gene = pyutil.readData('/home/feng/envs/Fig_Brachy/peak2gene.tsv')


plt.rcParams['font.size'] = 20.
plt.rcParams['xtick.labelsize'] = 22.
plt.rcParams['ytick.labelsize'] = 22.
plt.rcParams['axes.titlepad'] = 24.
plt.rcParams['legend.fontsize'] = 22.



# (pyext.base__file('results/0130__callDiffTarg__Brachy-ELF3/DONE'))

chipClu = pyutil.readBaseFile('results/0130__callDiffTarg__Brachy-ELF3/clu.csv')
chipClu.columns = ['clu']
chipClu.query('clu==1')
peakAcc = chipClu.query('clu==1').index.str.replace('_\d+$','').unique()
# peakAcc = chipDF.query('isTarg').index.str.replace('_\d+$','').unique()
# bedFile  = '/home/feng/envs/Fig_Brachy/per_score-GT-0dot6188C_RESEQ-combined.bed'
bedFile = pyext.base__file('results/0130__makePeakWindows__Brachy-ELF3/windowFile.bed')
bedFile =  pyutil.grepFileByKeys(bedFile,peakAcc)




# sutil.job__nearAUG
bwCurr= pyutil.readBaseFile('results/0201__dumpMeta__Brachy/bwCurr.csv')
bwCurr = bwCurr.query('bname.str.contains("ELF3",case=0)')
bwFiles = bwCurr.RPKMFile.map(pyext.base__file)
res = sjob.figs__peakBW(bwFiles=bwFiles,
                        center_summit=1,
                       peakFile=bedFile,
                        detailByChip=0,
                      outerRadius=1500,
                      innerRadius=300,
)
figD = res[0]
axs =figD.values()[0].axes
print (axs[1].get_xlim())
# axs[1].set_xlim(-1600,1600)
figs.update(figD)

pyutil.render__images(figs,exts=['png','svg'])