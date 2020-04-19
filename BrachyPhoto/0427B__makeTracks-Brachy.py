#!/usr/bin/env python

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

# meta = pyutil.readBaseFile('meta/meta_rna.tsv')
meta = pyutil.readBaseFile('results/0201__dumpMeta__Brachy/rnaCurr.csv')

keys = ['runID','gtype','light','temp','ZTime_int']


keyDF = pyutil.readBaseFile('headers/key_brachy.csv')
keyDF.to_csv('keyMarker.csv')
meta.sort_values(["SpecAcc","gtype","Age","light","temp","ZTime_int"],inplace=True)
# mcurr = mcurr0 = meta.query('SpecAcc=="Bd" & Age in ["Wk2","Wk3"]')
mcurr = mcurr0 = meta.query('SpecAcc=="Bd" & Age in ["Wk2","Wk3","Wk4"]')


# rnaDF = pyutil
# rnaseq = pyutil.readData('/home/feng/envs/Fig_Brachy/rna_brachy_log2p1_aligned.pk')
# rnaseq = pyutil.readBaseFile('results/0131__dumpDataRNA__Brachy/rna_log2p1_filtered.pk')
rnaseqs = []
rnaseq = res = pyutil.readBaseFile('results/0131__dumpDataRNA__Brachy/rna_raw.pk')
rnaseqs += [res]

FNAME = 'results/data/0413-dumpRunData/199R_201R/TPM.csv'
res = pyext.readBaseFile(FNAME, header=[0,1],)
res.columns = res.columns.droplevel(1)
res = res.T.query('~index.duplicated()').T
rnaseqs += [res]
rnaseq = pd.concat(rnaseqs,axis=1)
assert rnaseq.columns.is_unique

rnaseq = rnaseq.apply(pyutil.log2p1)

tks = tracks = pyutil.util_obj()


# key ='rnaseq'
# assert key in locals().keys(),'Variable not defined:%s'%key

# rnaseq = dfcc
## sutil.qc_Sort(df=dfccc)

tdf  = rnaseq.reindex(columns=mcurr0.index).dropna()
tdf = sutil.meanNorm(tdf)
rnaseqAll  = tdf

# tks = pyutil.util_obj()

metaList = []
# mcurr = meta.query('SpecAcc=="Bd" & gtype == "Bd21" & Age == "Wk3"')
query = 'SpecAcc=="Bd" & light == "SD" & Age == "Wk3"'

_meta = meta.query('RunID not in "199R,201R".split(",")')
mcurr = _meta.query(query)
m1 = mcurr.query('gtype=="Bdelf3"')
m2 = mcurr.query('gtype=="Bd21"')
tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = m1.index).values 
       - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)
tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]

tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += "_gtype=Bdelf3-Bd21"

rnaseq_wk3sd = rnaseq_wk3sd_elf3ko = tdf
assert ~(tdf.isnull().values.any())
metaList += [m1, m2]



# mcurr = meta.query('SpecAcc=="Bd" & gtype == "Bd21" & Age == "Wk3"')
query = 'SpecAcc=="Bd" & light == "SD" & Age == "Wk2"'
mcurr = _meta.query(query)
m1 = mcurr.query('gtype=="Bdelf3"')
m2 = mcurr.query('gtype=="Bd21"')
tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = m1.index).values 
       - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)

tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]
tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += "_gtype=Bdelf3-Bd21"

rnaseq_wk2sd = rnaseq_wk2sd_elf3ko = tdf
metaList += [m1, m2]


query = 'SpecAcc=="Bd" & light == "LD" & Age == "Wk2"'
mcurr = _meta.query(query)
m1 = mcurr.query('gtype=="phyC"')
m2 = mcurr.query('gtype=="Bd21"')

mm = m1.reset_index().merge(m2.reset_index(),on='ZTime_int',how='inner',sort=True)

tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = mm.DataAcc_x).values 
       - rnaseq.reindex(columns = mm.DataAcc_y).values ),
    
    rowName = rnaseq.index,colName = mm.DataAcc_x,)

tdf = scount.countMatrix(tdf,colMeta=meta.reindex(mm.DataAcc_x))
tdf.vlim = [-2,2]
tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += "_gtype=BdphyC-Bd21"
tdf.relabel('ZTime')

rnaseq_wk2ld_phycko = tdf
metaList += [m1, m2]

# query = ''
# mcurr = meta.query('SpecAcc=="Bd" & Age == "Wk3"')
# # mcurr = meta.query('SpecAcc=="Bd" & light == "LD" & Age == "Wk2"')
# # m1 = mcurr.query('gtype=="Bdelf3"')
# # m2 = mcurr.query('gtype=="Bd21"')
# # tdf = pyutil.init_DF(
# #     (rnaseq.reindex(columns = m1.index).values 
# #        - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)
# tdf = rnaseq.reindex(columns = mcurr.index)

# tdf = scount.countMatrix(tdf,colMeta = mcurr)
# tdf.relabel(['gtype','ZTime'])
# tdf.vlim = [-2,2]

# tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')

# rnaseq_wk3sd_joint = tdf


query = 'SpecAcc=="Bd" & gtype=="Bd21" & Age == "Wk2"'
mcurr = _meta.query(query)
m1 = mcurr.query('light=="LD"')
m2 = mcurr.query('light=="SD"')
tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = m1.index).values 
       - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)

tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]

tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += '_light=LD-SD'
print tdf.name
rnaseq_wk2wt = tdf
metaList += [m1, m2]


query = 'SpecAcc=="Bd" & gtype=="Bd21" & Age == "Wk3" & runID!="196R"'
mcurr = _meta.query(query)
mcurr = mcurr.query( 'ZTime!="ZT22"')
m1 = mcurr.query('light=="LD"')
m2 = mcurr.query('light=="SD"')
tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = m1.index).values 
       - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)

tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]

tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += '_light=LD-SD'
print tdf.name
rnaseq_wk3wt = tdf
metaList += [m1, m2]


query = 'SpecAcc=="Bd" & gtype=="Bd21" & light == "LD" & runID!="196R"'
mcurr = _meta.query(query)
# mcurr = mcurr.query( 'ZTime!="ZT22"')
m1 = mcurr.query('Age=="Wk3"')
m2 = mcurr.query('Age=="Wk2"')
mm = m1.reset_index().merge(m2.reset_index(),on='ZTime_int',how='inner',sort=True)
tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = mm.DataAcc_x).values 
       - rnaseq.reindex(columns = mm.DataAcc_y).values ),
    
    rowName = rnaseq.index,colName = mm.DataAcc_x,)

tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]

tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += '_Age=Wk3-Wk2'
print tdf.name
rnaseq_wk3ld_wk2ld = tdf
metaList += [m1, m2]



query = 'SpecAcc=="Bd" & Age == "Wk3" & light=="LD" & runID!="196R"'
mcurr = _meta.query(query)
m1 = mcurr.query('gtype=="Bdelf3"')
m2 = mcurr.query('gtype=="Bd21"')
tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = m1.index).values 
       - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)

tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]

tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += '_gtype=Bdelf3-Bd21'
print tdf.name
rnaseq_wk3ld_elf3ko = tdf
metaList += [m1, m2]



query = 'SpecAcc=="Bd" & gtype == "Bd21" & light=="LD" & runID!="196R" '
mcurr = _meta.query(query)
m1 = mcurr.query('Age=="Wk3"')
m2 = mcurr.query('Age=="Wk2"')

mm = m1.reset_index().merge(m2.reset_index(),on='ZTime_int',how='inner',sort=True)

tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = mm.DataAcc_x).values 
       - rnaseq.reindex(columns = mm.DataAcc_y).values ),
    
    rowName = rnaseq.index,colName = mm.DataAcc_x,)

# tdf = pyutil.init_DF(
#     (rnaseq.reindex(columns = m1.index).values 
#        - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)

tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]

tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += '_Age=Wk3-Wk2'
print tdf.name
rnaseq_wk3ld_wk2ld = tdf
metaList += [m1, m2]


query = 'SpecAcc=="Bd"  & light=="LD" & Age== "Wk3" & runID=="196R"'
mcurr = _meta.query(query)
m1 = mcurr.query('gtype=="ppd1-1"')
m2 = mcurr.query('gtype=="Bd21"')

mm = m1.reset_index().merge(m2.reset_index(),on='ZTime_int',how='inner',sort=True)

tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = mm.DataAcc_x).values 
       - rnaseq.reindex(columns = mm.DataAcc_y).values ),
    
    rowName = rnaseq.index,colName = mm.DataAcc_x,)

# tdf = pyutil.init_DF(
#     (rnaseq.reindex(columns = m1.index).values 
#        - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)

tdf = scount.countMatrix(tdf,colMeta = m1)
tdf.relabel('ZTime')
tdf.vlim = [-2,2]

tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += '_gtype=ppd1-Bd21'
print tdf.name
rnaseq_wk3ldppd1_wk3ldwt = tdf
metaList += [m1, m2]


# assert 0



# query = 'SpecAcc=="Bd" & Age.str.contains("day")'
# mcurr = meta.query(query)
# # m1 = mcurr.query('gtype=="Bdelf3"')
# # m2 = mcurr.query('gtype=="Bd21"')
# # tdf = pyutil.init_DF(
# #     (rnaseq.reindex(columns = m1.index).values 
# #        - rnaseq.reindex(columns = m2.index).values ),rowName = rnaseq.index,colName = m1.index)
# tdf = sutil.meanNorm(scount.countMatrix(rnaseq.reindex(columns=mcurr.index)))
# tdf.columns= mcurr.index
# tdf = scount.countMatrix(tdf, colMeta = mcurr)

# # tdf.relabel('ZTime')
# tdf.vlim = [-2,2]

# # tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
# # tdf.name_ += ''
# print tdf.name
# rnaseq_age_meanNorm = tdf


mcurr=  _meta.copy()
query = 'SpecAcc=="Bd" & Age=="Wk4" & runID =="143R" & light=="LD"'
mcurr = mcurr.query(query)

m1 = mcurr.query('gtype=="Bdphyc"')
m2 = mcurr.query('gtype=="Bd21"')

mm = m1.reset_index().merge(m2.reset_index(),on='ZTime_int',how='inner',sort=True)

tdf = pyutil.init_DF(
    (rnaseq.reindex(columns = mm.DataAcc_x).values 
       - rnaseq.reindex(columns = mm.DataAcc_y).values ),
    
    rowName = rnaseq.index,colName = mm.DataAcc_x,)

tdf = scount.countMatrix(tdf,colMeta=meta.reindex(mm.DataAcc_x))
tdf.vlim = [-2,2]
tdf.name_ = query.replace('&','_').replace('==','=').replace('"','').replace(' ','')
tdf.name_ += "_gtype=BdphyC-Bd21"
tdf.relabel('ZTime')

rnaseq_wk4ldphyc_wk4ldwt = tdf
metaList += [m1, m2]

lst = [
    dict(
        key='rnaseq_wk4elf3oxld_wk4wtld',
#         name = 'LD_Wk4_ELF3OX/wt_169R',
        name = 'LD_Wk4_ELF3OX/wt',
        relabel='ZTime',
        buf = '''
control,169RS17,169RS18,169RS19,169RS20
treatment,169RS25,169RS26,169RS27,169RS28
        '''),
    dict(
        key = 'rnaseq_wk3elf3ld_wk3elf3sd',
#         name = 'LD/SD_Wk3_elf3-1_193R/144R',
        name = 'LD/SD_Wk3_elf3-1',
        relabel='ZTime',
        buf =  '''
control,144RS17,144RS18,144RS19,144RS20,144RS21,144RS16
treatment,193RS8,193RS9,193RS10,193RS11,193RS12,193RS13
        ''',),
    dict(
        key = 'rnaseq_wk6ppd1oxsd_wk6wtsd',
#         name = 'SD_Wk6_PPD1OX-1/WT_199R',
        name = 'SD_Wk6_PPD1OX-1/WT',
        relabel='ZTime',
        buf =  '''
control,199RS1,199RS2,199RS3,199RS4,199RS6,199RS7,199RS8
treatment,199RS9,199RS10,199RS11,199RS12,199RS14,199RS15,199RS16
        ''',),
    dict(
        key = 'rnaseq_wk4phycld_wk4wtld',
#         name = 'LD_Wk4_phyC-4/WT_201R',
        name = 'LD_Wk4_phyC-4/WT',
        relabel='ZTime',
        buf =  '''
control,201RS1,201RS2,201RS3,201RS4,201RS5,201RS6,201RS7,201RS8
treatment,201RS9,201RS10,201RS11,201RS12,201RS13,201RS14,201RS15,201RS16
        ''',),
]


common  = dict(
    self = rnaseq,
    colMeta = meta.astype(unicode),
)
keys

for d in lst:
    d = pyutil.util_obj(**d)
    res = pyutil.df__makeContrastWithMeta(
        buf=d.buf,
        name=d.name,
        **common
    )
    if hasattr(d,'relabel'):
        res = res.relabel(d.relabel)
    print(d.key,d.name)
    print (res.colMeta[keys])
    tks[d.key] = res

rnaCurr = pd.concat(metaList,axis=0).query('~index.duplicated()')
rnaCurr.to_csv('rnaCurr.csv')

rnaseq_wk2wt.name_ = 'LD/SD_Wk2_wt'
rnaseq_wk3wt.name_ = 'LD/SD_Wk3_wt'
rnaseq_wk2sd_elf3ko.name_ = 'SD_Wk2_elf3-1/wt'
rnaseq_wk3sd_elf3ko.name_ = 'SD_Wk3_elf3-1/wt'
rnaseq_wk3ld_elf3ko.name_ = 'LD_Wk3_elf3-1/wt'
rnaseq_wk2ld_phycko.name_ = 'LD_Wk2_phyC-4/wt'
rnaseq_wk4ldphyc_wk4ldwt.name_ = 'LD_Wk4_phyC-4/wt'
rnaseq_wk3ld_wk2ld.name_ = 'LD_Wk3/Wk2_wt'
rnaseq_wk3ldppd1_wk3ldwt.name_ = 'LD_Wk3_ppd1/wt'


##### adding runID to trackLabel
for k,v in vars(tks).items():
    if hasattr(v,'name'):
        colMeta = v.colMeta
        if colMeta is not None:
            rids = colMeta['runID'].dropna().unique().tolist()
        else:
            rids = []
        if rids:
            rid = rids[0]
            if str(rid)!='nan':
                v.set__name(v.name+'_%s'%rid)
#         if v.name and len(rids)
        print(k, v.name, rids )
# ##### keyDFTrack
# inc = '''
# GENE_NAME,KEYDFTRACK,KEYDFTRACK2
# GI,1,1
# PIF2,1,1
# #PIF3,0,1
# PIF7,1,1
# FT1,1,1
# FT2,1,1
# #BdAP1,0,1
# PRR37,1,1
# CCA1,1,1
# ELF4,1,1
# LUX,1,1
# #RVE7,0,1
# RVE6,1,1
# #BdPRR95,0,1
# BdCO13,1,1
# BdPRR59,1,1
# BdGHD7L2,1,1
# BBX281,1,1
# BdMAD5,1,1
# #BdMAD16,0,1
# #CDF2,0,1
# #BdLNK4,0,1
# #BdLNK1,0,1
# #BdSTO,0,1
# '''
# # .strip().splitlines()
# pyext.read__buffer(inc,ext='csv')
# inc = [x for x in inc if not x.startswith("#")]
# keyDFC = keyDF.query('BioName in @inc')
# keyDFTrack = scount.countMatrix(
#             keyDFC.get(['BioName']),height=1.0,
#         )
# keyDFTrack = keyDFTrack.rename(columns={'BioName':'Marker'})




inc = '''
KEYDFTRACK,KEYDFTRACK2,GENE_NAME
1,1,GI
1,1,PIF2
0,1,PIF3
1,1,PIF7
1,1,FT1
1,1,FT2
0,1,BdAP1
1,1,PRR37
1,1,CCA1
1,1,ELF4
1,1,LUX
0,1,RVE7
1,1,RVE6
0,1,BdPRR95
1,1,BdCO13
1,1,BdPRR59
1,1,BdGHD7L2
1,1,BBX281
1,1,BdMAD5
0,1,BdMAD16
0,1,CDF2
0,1,BdLNK4
0,1,BdLNK1
0,1,BdSTO
0,1,BdMYR2
'''

dfc = pyext.read__buffer(inc,ext='csv',guess_index=0).set_index('GENE_NAME')
# print len(dfc)

#### keyDFTRACK1
keyDFC = keyDF.copy()
keyDFC['include'] = dfc['KEYDFTRACK'].loc[keyDFC.BioName.tolist()].fillna(0).tolist()
keyDFC = keyDFC.query('include==1')

keyDFC = scount.countMatrix(
            keyDFC.get(['BioName']),height=4.0,
        )
keyDFC = keyDFC.rename(columns={'BioName':'Marker'})
keyDFTrack = keyDFC
print (keyDFC.name,len(keyDFC))

#### keyDFTRACK2
keyDFC = keyDF.copy()
keyDFC['include'] = dfc['KEYDFTRACK2'].loc[keyDFC.BioName.tolist()].fillna(0).tolist()
keyDFC = keyDFC.query('include==1')

keyDFC = scount.countMatrix(
            keyDFC.get(['BioName']),height=4.0,
        )
keyDFC = keyDFC.rename(columns={'BioName':'Marker'})
keyDFTrack2 = keyDFC
print (keyDFC.name,len(keyDFC))

# tracks = pyutil.dictFilter(oldd=locals(),keys='''
# rnaseq_wk2wt
# rnaseq_wk3wt
# rnaseq_wk2sd_elf3ko
# rnaseq_wk3sd_elf3ko
# rnaseq_wk2ld_phycko
# rnaseq_wk4ldphyc_wk4ldwt
# rnaseq_wk3ld_wk2ld
# keyDFTrack
# '''.strip().splitlines())
d = pyutil.dictFilter(locals(),
                           keys = filter(lambda x:x.startswith('rnaseq'),
                                         locals().keys()
                                        ) + ['keyDFTrack','keyDFTrack2']
                          )
tracks.__dict__.update(d)
# tracks.__dict__.update(

tracks['rnaUniq'] = list(pyutil.unique([v for k,v in vars(tracks).items() if k.startswith('rnaseq_')]))

for v in tracks.rnaUniq:
    v.height = 4
tks.keyDFTrack.height = 4.
tks.keyDFTrack2.height = 6.


trackOrders = {
    'order1':[
        'cluTrack',
#         chipTrack,
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
        tks.rnaseq_wk4ldphyc_wk4ldwt,
#         rnaseq_wk3ldppd1_wk3ldwt,
#         rnaseq_wk3ld_wk2ld,
#         rnaseq_wk3ld_elf3ko,
        tks.keyDFTrack,
    ],
    'order2':[
        'cluTrack',
#         chipTrack,
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
#         tks.rnaseq_wk4ldphyc_wk4ldwt,
#         rnaseq_wk3ldppd1_wk3ldwt,
#         rnaseq_wk3ld_wk2ld,
#         rnaseq_wk3ld_elf3ko,
        tks.keyDFTrack,
    ],    
    'order3':[
        'cluTrack',
#         chipTrack,
        tks.rnaseq_wk2wt,
#         rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk2ld_phycko,
#         rnaseq_wk4ldphyc_wk4ldwt,
#         rnaseq_wk3ldppd1_wk3ldwt,
        tks.rnaseq_wk3ld_wk2ld,
#         rnaseq_wk3ld_elf3ko,
        tks.keyDFTrack,
    ],    
    'allRNA':[
        'cluTrack',
#         chipTrack,
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk3elf3ld_wk3elf3sd,        
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk3ld_elf3ko,
        tks.rnaseq_wk4elf3oxld_wk4wtld,
        tks.rnaseq_wk2ld_phycko,
#         tks.rnaseq_wk4ldphyc_wk4ldwt,
        tks.rnaseq_wk3ldppd1_wk3ldwt,
        tks.rnaseq_wk3ld_wk2ld,
        tks.rnaseq_wk6ppd1oxsd_wk6wtsd,
        tks.rnaseq_wk4phycld_wk4wtld,
#         tks.rnaseq_wk
#         tks.rn
#         tks.rnaseq_wk4ldphyc_wk4ldwt,
#         rnaseq_wk3ldppd1_wk3ldwt,
#         rnaseq_wk3ld_wk2ld,
#         rnaseq_wk3ld_elf3ko,
        tks.keyDFTrack,
    ],   
    'main':[
        'cluTrack',
        tks.rnaseq_wk2wt,
        tks.rnaseq_wk3wt,
        tks.rnaseq_wk2sd_elf3ko,
        tks.rnaseq_wk3sd_elf3ko,
        tks.rnaseq_wk3ld_elf3ko,
        
        tks.rnaseq_wk2ld_phycko, ## 0701
#         tks.rnaseq_wk4phycld_wk4wtld,
        tks.keyDFTrack,        
    ],
        
    
}
trackOrders['currentOrder'] = trackOrders['order2']
tks.trackOrders= trackOrders

np.save('tracks.npy', tracks)




# tracks = 