#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
NCORE = 10
execfile(pyext.base__file('headers/header__import.py'))
# tks = pyutil.readBaseFile('results/0130__makeTracks-Brachy/tracks.npy').tolist()
figs = pyutil.collections.OrderedDict()


pyutil.readBaseFile('results/0208__peakTarget__Brachy-PHYC/peak2geneFile.tsv',index_col=[0],
                   ).to_excel('DatasetS8.xls',
#                               index=0
                             )
it = [
    ('ELF3__SD__ZT20__peaks',
     sdio.extract_peak('results/0205__vennChip__Brachy_ELF3-PHYC/\
64-SD-ZT20-ELF3OX-RERUN_S8_peaks_radius=1_query=FC-GT-3.tsv',baseFile=1)),
    ('phyC__LD__ZT20__peaks',
     sdio.extract_peak('results/0205__vennChip__Brachy_ELF3-PHYC/\
phyC-OX-GFP-FLAG-Zt20-LD-RERUN_S10_peaks_radius=1_query=FC-GT-3.tsv',baseFile=1)),
    ('ELF3__phyC__overlap',
     pyutil.readBaseFile('http://172.26.114.34:81/static/results/0205__vennChip__Brachy_ELF3-PHYC/\
peakVenn__188CRS8__188CRS10.csv',index_col=[0])),
   ]
pyutil.it__toExcel(it=it,
                   ofname='DatasetS8.xls',sheetFunc=lambda x:x)
                   
                    
# pyutil.readBaseFile('results/0205__vennChip__Brachy_ELF3-PHYC/phyC-OX-GFP-FLAG-Zt20-LD-RERUN_S9_peaks_radius=1_query=FC-GT-3.tsv')




if 1:
    gconf=  pyutil.readBaseFile('results/0205__makeGCONF/gconf.npy').tolist()

    # clu.sort_values('clu')

    fname = 'results/0129__showCluster__Brachy-RNA-all/clu.csv'

    # 'results/
    lst = '''
    results/0205__venn__Brachy-funcTarg/funcTarg.csv
    #results/0129__showCluster__Brachy-RNA-all/clu.csv
    results/0214__heatmap__Brachy-all/clu.csv
    '''.strip().splitlines()


    #     geneRes.to_csv(pyutil.os.path.basename(fname))

worker = funcy.compose(
    funcy.partial( pyutil.meta__label,gconf.geneMeta),
    pyutil.readBaseFile,
)

worker(
    'results/0214__heatmap__Brachy-all/clu.csv'
).to_excel(
    'DatasetS3.xls')
worker(
    'results/0205__venn__Brachy-funcTarg/funcTarg.csv'
).to_excel('DatasetS4.xls')

pyutil.localise(
    'results/0210__tidyRNAMeta__Brachy/TPM__table.xls',
    baseFile=1,
    ofname= 'DatasetS2.xls')


# d = {
#     'DatasetS2.xls':'results/0210__tidyRNAMeta__Brachy/TPM__table.xls',
#     'DatasetS3.xls':'results/0209__labelGene__Brachy/results____0129__showCluster__Brachy-RNA-all____clu.xls',
#     'DatasetS4.xls':'results/0209__labelGene__Brachy/results____0205__venn__Brachy-funcTarg____funcTarg.xls',
# #     'DatasetS5.xls':'results'
# }

meta ='''
name,describ
DatasetS2.xls, RNA-seq TPM for all time courses considered
DatasetS3.xls, Cluster assignment of filtered genes
DatasetS4.xls, functional targets of ELF3
DatasetS8.xls, ChIP-Seq peaks for ELF3 and phyC that produced the venn diagram
'''
meta = pyutil.read__buffer(meta,ext='csv')
meta['url'] = pyutil.df__paste0(meta,[['<a href="'],'name',['">'],'name',['</a>'] ])
pd.set_option('display.max_colwidth', -1)
print(meta.to_html('meta.html'))

# d = {pyext.base__file(v):k for k,v in d.items()}
# for k,v in d.items():
#     pyutil.localise(pyext.base__file(v),ofname=k)
    
pyutil.shellexec('ls -1 . | grep -v .gz | xargs tar -zvcf archive.tar.gz')
# pyext.file__rename(d,copy=1)