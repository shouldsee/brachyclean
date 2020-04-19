#!/bin/bash
# -*- coding: utf-8 -*-

export PATH=/home/feng/local/bin:$PATH    
. /home/feng/envs/pipe/bin/activate
. config_Bd21-3.sh

# export DB_MOTIF="/home/feng/ref/motif/ARABD/ArabidopsisPBM_20140210.meme"
export DB_MOTIF="
/home/feng/ref/motif/CIS-BP/Arabidopsis_thaliana.meme
/home/feng/ref/motif/JASPAR/JASPAR2018_CORE_plants_non-redundant.meme
/home/feng/ref/motif/ARABD/ArabidopsisPBM_20140210.meme
"

# "http://172.26.114.34:81/static/figures/1219__ELF3__diffBind__summitDist/greped__merged__1219__ELF3__diffbind_radius=500.tsv" \

for URL in \
"http://172.26.114.34:81/static/results/0130__callDiffTarg__Brachy-ELF3/diffBoundPeaks_radius=250.tsv" \
"http://172.26.114.34:81/static/figures/1219__ELF3__diffBind__summitDist/greped__merged__1219__ELF3__diffbind_radius=500.tsv_radius=350.tsv" \
"http://172.26.114.34:81/static/figures/1219__ELF3__diffBind__summitDist/merged__1219__ELF3__diffbind_radius=500.tsv"
do

wget -N "$URL"
INFILE=`basename $URL`
# ln -f functionalPeaks.narrowPeak functionalPeaks.bed
quickFasta $INFILE
pipeline_motif.sh $INFILE
done