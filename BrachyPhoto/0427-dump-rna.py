#!/usr/bin/env python2
import pymisca.header as pyheader
pyheader.execBaseFile('headers/header__import.py')
figs = pyext.collections.OrderedDict()

def dropByNonZeroCount(dfc,threshold = 2, MIN = 20, inplace=0):
    dfc = dfc.copy()
    dfc.values[dfc.values < MIN ] = MIN
    SUM = (dfc > MIN).sum(axis=1)
    toDrop = SUM.to_frame('SUM').query('SUM < %d' % threshold).index
    print len(toDrop)
    dfc = dfc.drop(index=toDrop,inplace=inplace)
    return dfc
    


def saveDF(tdf,name):
    pyext.shellexec('mkdir -p csv pk')
    print ('[SAVING] dataset:%s %s'%(name,tdf.shape))
    tdf.to_csv('csv/%s.csv'%name)
    tdf.to_pickle('pk/%s.pk'%name)
    
BLACKLIST = '''
196RS1
196RS2
196RS3
196RS4
196RS5
196RS6
196RS7
196RS8
'''.strip().splitlines()

tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
tdf = tks.rnaseq
tdf = scount.countMatrix(tdf)

rnaCurr = pyext.readBaseFile('results/0130__makeTracks-Brachy/rnaCurr.csv',)
rnaCurr.to_csv('rnaCurr.csv')

tdf.set__colMeta(rnaCurr)
# tdf.relabel(colLabel=KEYS)
# tdf.relabel(colLabel='DISPLAY_NAME')


# pyext.localise



rnaCurr['DATAACC'] = rnaCurr.index
rnaCurr.columns = rnaCurr.columns.str.upper()
KEYS = ['AGE','LIGHT','GTYPE','ZTIME_INT','DATAACC']
rnaCurr['DISPLAY_NAME'] = pyext.df__paste0(rnaCurr,KEYS,sep='_')
rnaCurr = rnaCurr.query('AGE=="Wk3"').sort_values(KEYS)
rnaCurr = rnaCurr.query('DATAACC not in @BLACKLIST')


# pyutil.render__images(figs,exts=['png','svg'])


saveDF(tdf,'read')

tdf = dropByNonZeroCount(tdf.apply(pyext.exp2m1),threshold= 4,MIN = 20,inplace=False)
tdf = tdf.apply(np.log2)
saveDF(tdf,'read-topped-log2')


tdf = tdf.filter(axis=1,items=rnaCurr.index)
tdf.set__colMeta(rnaCurr)
saveDF(tdf,'read-topped-log2-wk3')

tdf = sutil.meanNorm(tdf)
saveDF(tdf,'read-topped-log2-wk3-meannorm')