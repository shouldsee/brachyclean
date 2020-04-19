#!/usr/bin/env python

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()
#                    './headers/header__import.py')
NBNAME="1024__chipTarg__ELF3"

# DIR = pyext.base__file('.')

keyDF = pyutil.readData( pyext.base__file('./headers/key_brachy.csv') )

# BED_FILE = bedFile = DIR + '/bedFile.bed'
# bed = sdio.extract_peak(bedFile)

# peak2gene = pyutil.readData('%s/peak2gene.tsv' % DIR)
# chipRel = pyutil.readData('%s/1018__chip-rel.pk'% DIR)
# peak2gene = pyutil.readData('%s/peak2gene.tsv' % DIR)


########## Read data
peak2gene = pyutil.readData(
        'results/0130__makePeakWindows__Brachy-ELF3/peak2geneFile.tsv',baseFile=1)
chipRel = pyutil.readData(
    'results/0130__chipSummary__Brachy-ELF3/bwAvg.pk',baseFile=1,
                         callback=scount.countMatrix)
bedDF = sdio.extract_peak('results/0130__makePeakWindows__Brachy-ELF3/windowFile.bed',baseFile=1,
                             ).set_index('acc',drop=0)
peaks0 = peaks = peak2gene.merge(keyDF,right_index=True,left_on="feat_acc")

bedOrig = bedDF = sdio.extract_peak(
    'results/0130__makePeakWindows__Brachy-ELF3/combined__ELF3__peaks.narrowPeak',baseFile=1,
).set_index('acc',drop=0)





#### QC plot
sutil.qc_Sort(df=chipRel);
figs['qcPlot']  = plt.gcf()




####  Marker Gene
ALIAS='markerWindow'
marker = '''
GI
LUX
'''.strip().splitlines()

peaks = peaks.query('BioName in @marker')
# peaks.acc
# chipRel = chipRel.drop(columns='INPUT-408_S11_RPGC')

dfcc = chipRel
# cols = chipRel.columns[chipRel.columns.str.contains('INPUT|ELF3')]
# cols = chipRel.columns[chipRel.columns.str.contains('ELF3')]
cols = chipRel.columns[chipRel.columns.str.contains('64-')]

dfcc = chipRel.reindex(columns=cols)
dfcc = sutil.meanNorm(dfcc)
dfcc.columns = cols
chipDiff= dfcc

dfccc = dfcc.reindex(peaks.acc)
dfccc.index = keyDF.loc[peaks.feat_acc].BioName

# plt.rcParams()
plt.rcParams['font.size'] = 16
plt.rcParams['legend.fontsize'] = 14

fig,ax = plt.subplots(figsize=[10,5])
ZTime =  dfccc.columns.str.extract('(ZT\d+)-',expand=False) 
Zint = (pd.Series(ZTime,index=dfccc.columns).str.strip('ZT').astype(int) + 4 ) % 24
# dfccc.columns =
chip__cols = Zint.sort_values().index
dfccc = dfccc.reindex(columns = chip__cols)
# dfccc
dfccc.heatmap(tickMax=200,ax=ax,cname='Relative Binding')
figs['markerWindow'] = plt.gcf()

fig = plt.figure()
signature= dfccc.values.mean(axis=0,)
signature = signature - signature.mean()
plt.plot(signature)
# dfccc.groupby(level=0,axis=1).mean()
plt.xticks(range(len(dfccc.columns)),list(dfccc.columns),rotation='vertical')
figs['signature']= fig



######################################################
###### Calling putative chip targets ###############
######################################################

score = sutil.meanNorm(chipDiff.reindex(columns=chip__cols)).dot(signature).to_frame('score__chipDiff')

chipDiff.qc_Avg();
sd = chipDiff.summary.SD.to_frame('sd__chip')

score = pd.concat([score,sd],axis=1,)


# query__chip = query = 'score__chipDiff>0.75 and sd__chip > 0.6'
# query__chip = query = 'score__chipDiff> 1.1 and sd__chip > 0.7'
# query__chip = query = 'score__chipDiff> 1.5 and sd__chip > 0.7'
query__chip = query = 'score__chipDiff> 1.5'
# query__chip = query = 'score__chipDiff<-1.0 and sd__chip > 0.6'
# query = 'score__chipDiff<-0.5'
chipClu = clu =  score.eval(query).to_frame(pyutil.sanitise_query(query))
clu.columns = ['clu']
score = pd.concat([score,clu],axis=1)

clu.to_csv('clu.csv')
score.to_csv('score__%s.csv'%NBNAME)

ind = clu.query('clu==1').index
bedCurr = bedDF.reindex(ind)
pyutil.to_tsv(bedCurr,'windows.bed')
geneDF =sdio.peak2gene(peak2gene[['acc','feat_acc','distance']],bedCurr,how='left')
geneDF.to_csv('geneDF__diffBoundPeak.csv')

ofname = pyutil.to_tsv(
    bedOrig.reindex(ind.str.rsplit('_',1).str.get(0).unique()),
    'diffBoundPeaks.bed',
)
sdio.npk_expandSummit(
    fname = ofname,
    radius=250,
)


#### visualisation
ind = score.sort_values('score__chipDiff')[::-1][:200].index
fig,ax = plt.subplots(figsize=[10,5])
dfcc.reindex(ind,columns=chip__cols).heatmap(ax=ax)

figs['previewTargets'] = plt.gcf()


pyvis.qc_2var(score['sd__chip'],
              score['score__chipDiff'],
#               xlim  =None,
#               ylim = None,
              ylim = [-3.0, 3.0],
              xlim=[0.,2.0],
              nMax=-1,clu=clu)
figs['previewScatter']= plt.gcf()

score = pd.concat([score,sd],axis=1)

# score.to_csv('score__chipDiff.csv')

indc = clu.index[clu.values.flat]
indc



pyutil.render__images(figs)
# execfile('make__rnaPlotter.py')