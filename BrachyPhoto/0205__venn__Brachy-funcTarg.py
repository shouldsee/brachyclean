#!/usr/bin/env python
# -*- coding: utf-8 -*-
NCORE=6
import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()


keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
GSIZE= pyext.base__file('ref/Brachypodium_Bd21_v3-1/genome.sizes')
peak2geneFile = 'results/0130__makePeakWindows__Brachy-ELF3/peak2geneFile.tsv'
peak2gene = pyutil.readBaseFile( peak2geneFile )
geneMeta = pyutil.readBaseFile('results/0205__makeGCONF/geneMeta.csv')
# keyDF = pyutil.readData('/home/feng/meta/key_brachy.csv')
# peak2gene = pyutil.readData('/home/feng/envs/Fig_Brachy/peak2gene.tsv')

plt.rcParams['font.size'] = 20.
plt.rcParams['xtick.labelsize'] = 22.
plt.rcParams['axes.titlepad'] = 24.

#####
rnaScore = pyutil.readBaseFile('results/0205__interpAUC__Brachy/score__rnaseq__AUC.csv')
xlab = 'transcriptionally perturbed\n over day-night cycle'
query = 'score__rnaseq__AUC>1.0'
ind1 = rnaScore.query(query).index

chipClu = pyutil.readBaseFile('results/0130__callDiffTarg__Brachy-ELF3/clu.csv')
chipClu.columns = ['clu']
geneDF = sdio.peak2gene(peak2gene,chipClu.query('clu==1'))

chipDF = pyutil.readBaseFile('results/0130__callDiffTarg__Brachy-ELF3/score__1024__chipTarg__ELF3.csv')
# geneDF = sdio.peak2gene(peak2gene,chipDF.query('score__chipDiff > 1.5'))

# chipDF = pyutil.readData('/home/feng/envs/Fig_Brachy/score__1024__chipTarg__ELF3.csv')
# chipDF['isTarg'] = chipDF['score__chipDiff-GT-0dot5andsd__chip-GT-0dot45']
# geneDF = sdio.peak2gene(peak2gene,chipClu.query('clu==1'))
ylab = 'chipSeq_differentially_bound'
# ind2 = geneDF.feat_acc.index
ind2 = geneDF.feat_acc.unique()

qres,axs = pyvis.qc_index(ind1,ind2,silent=0,xlab=xlab,ylab=ylab);
pyvis.hide_Axes(plt.gcf().axes[1])
figs['venn_functional'] = plt.gcf()
qres.to_csv( 'venn_index.csv' )

# funcTarg = keyDF.reindex(qres.indAll.dropna())
# funcTarg = pd.Index(qres.indAll.dropna()).to_frame('GeneAcc')
funcTarg = pyvis.df__indVenn2Flat(qres)[0]
funcTarg.to_csv( 'funcTarg.csv')
# funcTarg = pyutil.meta__label(geneMeta, funcTarg,)

# qres.indAll.dropna().merge(keyDF,right_index=True)



#####
s2 = sdio.peak2gene(peak2gene,chipDF)
ss = s2.merge(rnaScore,left_on='feat_acc',right_index=True)
ss = ss.merge(keyDF,right_index=True,left_on = 'feat_acc',how='left')

xlab,ylab = 'score__rnaseq__AUC','score__chipDiff'

xs = ss[xlab]
ys = ss[ylab]
pyvis.qc_2var(xs,ys,
              xlim=pyutil.span(xs,100.),ylim=pyutil.span(ys,100.),
              nMax=50000,
              xlab=xlab,ylab=ylab)
title = 'peak_level_scatter'
plt.suptitle(title)
figs[title] = plt.gcf()

pyutil.render__images(figs,exts=['png','svg'])
# execfile("/home/feng/meta/footer__script2figure.py")