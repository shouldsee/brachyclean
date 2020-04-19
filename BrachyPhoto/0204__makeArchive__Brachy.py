#!/usr/bin/env python
# -*- coding: utf-8 -*-
# execfile('/home/feng/headers/header__import.py')
import pymisca.util as pyutil
dfc = pyutil.readData(pyutil.base__file('TOUCHED.list'),ext='tsv',header=None)

ind = dfc.query('~index.duplicated()').sort_index()
# print (ind.to_csv())
ind.to_csv(pyutil.base__file('file.index',force=1))
pyutil.shellexec('''
cd $BASE
cat file.index | grep ^RNA | xargs tar -cvzf RNA-seq.tar.gz
''')
                
pyutil.shellexec('''
cd $BASE
echo > tracking.index
{
cat file.index | grep -v ^RNA-seq 
echo *.tar.gz 
echo *.index 
echo *.txt 
echo *.list 
echo "Snakefile README" 
} >> tracking.index
''')

pyutil.shellexec('''
cd $BASE
echo
mkdir -p dist;
cat tracking.index | xargs cp -avu --parents -t dist
''')