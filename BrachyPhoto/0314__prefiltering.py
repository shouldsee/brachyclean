#!/usr/bin/env python
import pymisca.header as pyheader
pyheader.execBaseFile('headers/header__import.py')
figs = pyext.collections.OrderedDict()

df1 = pyext.readBaseFile('results/0311__table-VACV-900R/out.csv')
df2 = df20 = pyext.readBaseFile('results/0311__table-hsap-900R/out.csv')
# sumAll2 = df2.sum(axis=0).to_frame('sum_All2')
df2 = df2.tail(-3)
dfall = pd.concat([df1,df2],axis=0)
df3 = pyext.readBaseFile('results/0311__table-spikein-900R/out.csv')

rnaCurr = pyutil.readBaseFile('meta/900R.meta.csv')
rnaCurr = rnaCurr.sort_values('sampleID_int')


rnaTable = pd.concat([df1,df2],axis=0)

def dropAllZero(dfc,inplace=0):
    
    SUM = dfc.sum(axis=1)
    toDrop = SUM.to_frame('SUM').query('SUM==0').index
    dfc = dfc.drop(index=toDrop,inplace=inplace)
    return dfc

def dropByNonZeroCount(dfc,threshold = 2, inplace=0):
    SUM = (dfc!=0).sum(axis=1)
    toDrop = SUM.to_frame('SUM').query('SUM<%d' % threshold).index
    dfc = dfc.drop(index=toDrop,inplace=inplace)
    return dfc
    
dfc = rnaTable
dfc = dfc.astype('float')
dfc =scount.countMatrix(dfc)
# dropAllZero(dfc,inplace=True)
tdf = dropByNonZeroCount(dfc,2,inplace=False)
tdf.to_csv('out.csv')

# res = (rnaTable != 0).sum(axis=1).to_frame('val')
# res.hist('val')
# nonZero =res.query('val>1')    