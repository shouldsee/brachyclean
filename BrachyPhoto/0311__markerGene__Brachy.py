#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymisca.header as pyheader
pyheader.base__check()
pyheader.execBaseFile('headers/header__import.py')
figs= pyext.collections.OrderedDict()

tks = pyext.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
rnaCurr = pyext.readBaseFile('results/0130__makeTracks-Brachy/rnaCurr.csv')
keyDF = pyext.readBaseFile('headers/key_brachy.csv')


#### Casting value types
rnaCurr.ZTime_int = rnaCurr.ZTime_int.astype(float)
# keys = ['gtype','Age','light','ZTime_int']
keys = ['gtype','Age','light',]
rnaCurr = rnaCurr.sort_values(keys)

# fig,ax = plt.subplots(1,1,figsize=[12,7])
rowBioName = ["LUX","ELF3","PHYC","PRR37"]
gdf = keyDF.query('BioName.str.upper() in @rowBioName')
vdf = scount.countMatrix(tks.rnaseq, 
                         colMeta= rnaCurr,rowMeta = gdf)
vdf = vdf.reindex(columns = rnaCurr.index & vdf.columns)
vdf = vdf.reindex(gdf.index)
tdf = vdf.copy()


##### Reshaping
vdf =tdf.copy()
vdf.relabel(rowLabel='BioName')
vdf = vdf.reindex(columns = vdf.colMeta_.query('Age=="Wk3" & gtype == "Bd21"').index)

data = vdf.melt().rename(columns=dict(variable='col',ind='gene_id')).merge(vdf.colMeta,right_index=True,left_on='col')
data.value = data.value.astype(float)
data.ZTime_int = data.ZTime_int.astype(float)

dfc = data.pivot_table(
    columns=['gene_id'] + keys,values='value',
    index='ZTime_int')

L = 3
fig,axs = pyvis.get_subplotGrid(L=L,ncols=3)
for i,(k,dfcc) in enumerate(dfc.groupby(level='gene_id',axis=1)):
    ax = axs[i]
    dfcc.dropna().plot(marker='.',ax=ax)
    ax.set_title(k)
    ax.grid(1)
    ax.set_ylim(0,None)
    ax.set_ylabel('log(1+TPM)')
figs['lineplots'] = fig
pyutil.render__images(figs)