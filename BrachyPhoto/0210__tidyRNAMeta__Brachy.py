#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymisca.ext as pyext
execfile(pyext.base__file('headers/header__import.py'))
figs = pyutil.collections.OrderedDict()

buf = '''
DataAcc	bname	template_protocol	SpecAcc	Age	ZTime	gtype	temp	cultivar	light	sampleID	ZTime_int	runID	pipeline	fname
150RS1	Doro-Bd21-3-ZT0-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT0	Bd21-3	20C	Bd21-3	LD	S1	0	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT0-LD_S1/Doro-Bd21-3-ZT0-LD_S1_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
150RS2	Doro-Bd21-3-ZT1-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT1	Bd21-3	20C	Bd21-3	LD	S2	1	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT1-LD_S2/Doro-Bd21-3-ZT1-LD_S2_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
150RS3	Doro-Bd21-3-ZT4-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT4	Bd21-3	20C	Bd21-3	LD	S3	4	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT4-LD_S3/Doro-Bd21-3-ZT4-LD_S3_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
150RS4	Doro-Bd21-3-ZT8-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT8	Bd21-3	20C	Bd21-3	LD	S4	8	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT8-LD_S4/Doro-Bd21-3-ZT8-LD_S4_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
150RS5	Doro-Bd21-3-ZT12-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT12	Bd21-3	20C	Bd21-3	LD	S5	12	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT12-LD_S5/Doro-Bd21-3-ZT12-LD_S5_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
150RS6	Doro-Bd21-3-ZT16-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT16	Bd21-3	20C	Bd21-3	LD	S6	16	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT16-LD_S6/Doro-Bd21-3-ZT16-LD_S6_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
150RS7	Doro-Bd21-3-ZT20-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT20	Bd21-3	20C	Bd21-3	LD	S7	20	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT20-LD_S7/Doro-Bd21-3-ZT20-LD_S7_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
150RS8	Doro-Bd21-3-ZT22-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT22	Bd21-3	20C	Bd21-3	LD	S8	22	150R	tophat	RNA-seq/Mapped_data/150R_Brachy_LD/Doro-Bd21-3-ZT22-LD_S8/Doro-Bd21-3-ZT22-LD_S8_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS1	Exp0027-ZT0-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT0	Bd21-3	20C	Bd21-3	SD	S1	0	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT0-Bd21-3-SD_S1/Exp0027-ZT0-Bd21-3-SD_S1_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS2	Exp0027-ZT1-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT1	Bd21-3	20C	Bd21-3	SD	S2	1	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT1-Bd21-3-SD_S2/Exp0027-ZT1-Bd21-3-SD_S2_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS3	Exp0027-ZT4-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT4	Bd21-3	20C	Bd21-3	SD	S3	4	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT4-Bd21-3-SD_S3/Exp0027-ZT4-Bd21-3-SD_S3_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS4	Exp0027-ZT8-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT8	Bd21-3	20C	Bd21-3	SD	S4	8	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT8-Bd21-3-SD_S4/Exp0027-ZT8-Bd21-3-SD_S4_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS5	Exp0027-ZT12-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT12	Bd21-3	20C	Bd21-3	SD	S5	12	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT12-Bd21-3-SD_S5/Exp0027-ZT12-Bd21-3-SD_S5_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS6	Exp0027-ZT16-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT16	Bd21-3	20C	Bd21-3	SD	S6	16	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT16-Bd21-3-SD_S6/Exp0027-ZT16-Bd21-3-SD_S6_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS7	Exp0027-ZT20-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT20	Bd21-3	20C	Bd21-3	SD	S7	20	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT20-Bd21-3-SD_S7/Exp0027-ZT20-Bd21-3-SD_S7_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
148RS8	Exp0027-ZT22-Bd21-3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT22	Bd21-3	20C	Bd21-3	SD	S8	22	148R	tophat	RNA-seq/Mapped_data/148R/Brachy_SD_bd21-3_PIF3OX_PIF2OX/Exp0027-ZT22-Bd21-3-SD_S8/Exp0027-ZT22-Bd21-3-SD_S8_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS16	elf3-ZT0-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT0	elf3-1	20C	Bd21-3	SD	S16	0	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT0-SD_S16/elf3-ZT0-SD_S16_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS17	elf3-ZT1-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT1	elf3-1	20C	Bd21-3	SD	S17	1	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT1-SD_S17/elf3-ZT1-SD_S17_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS18	elf3-ZT4-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT4	elf3-1	20C	Bd21-3	SD	S18	4	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT4-SD_S18/elf3-ZT4-SD_S18_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS19	elf3-ZT8-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT8	elf3-1	20C	Bd21-3	SD	S19	8	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT8-SD_S19/elf3-ZT8-SD_S19_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS20	elf3-ZT12-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT12	elf3-1	20C	Bd21-3	SD	S20	12	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT12-SD_S20/elf3-ZT12-SD_S20_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS21	elf3-ZT16-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT16	elf3-1	20C	Bd21-3	SD	S21	16	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT16-SD_S21/elf3-ZT16-SD_S21_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS22	elf3-ZT20-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT20	elf3-1	20C	Bd21-3	SD	S22	20	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT20-SD_S22/elf3-ZT20-SD_S22_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS23	elf3-ZT22-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT22	elf3-1	20C	Bd21-3	SD	S23	22	149R	tophat	RNA-seq/Mapped_data/149R/Brachy_SD_elf3/elf3-ZT22-SD_S23/elf3-ZT22-SD_S23_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS24	phyC-ZT0-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT0	phyC-4	20C	Bd21-3	LD	S24	0	149R	tophat	RNA-seq/Mapped_data/149R/phyC_CRISPR/phyC-ZT0-LD_S24/phyC-ZT0-LD_S24_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS25	phyC-ZT1-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT1	phyC-4	20C	Bd21-3	LD	S25	1	149R	tophat	RNA-seq/Mapped_data/149R/phyC_CRISPR/phyC-ZT1-LD_S25/phyC-ZT1-LD_S25_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS26	phyC-ZT4-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT4	phyC-4	20C	Bd21-3	LD	S26	4	149R	tophat	RNA-seq/Mapped_data/149R/phyC_CRISPR/phyC-ZT4-LD_S26/phyC-ZT4-LD_S26_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS27	phyC-ZT8-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT8	phyC-4	20C	Bd21-3	LD	S27	8	149R	tophat	RNA-seq/Mapped_data/149R/phyC_CRISPR/phyC-ZT8-LD_S27/phyC-ZT8-LD_S27_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS28	phyC-ZT12-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT12	phyC-4	20C	Bd21-3	LD	S28	12	149R	tophat	RNA-seq/Mapped_data/149R/phyC_CRISPR/phyC-ZT12-LD_S28/phyC-ZT12-LD_S28_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS29	phyC-ZT16-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT16	phyC-4	20C	Bd21-3	LD	S29	16	149R	tophat	RNA-seq/Mapped_data/149R/phyC_CRISPR/phyC-ZT16-LD_S29/phyC-ZT16-LD_S29_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
149RS30	phyC-ZT20-LD	softTemplate-sample-RNAseq-Ming	Bd	Wk2	ZT20	phyC-4	20C	Bd21-3	LD	S30	20	149R	tophat	RNA-seq/Mapped_data/149R/phyC_CRISPR/phyC-ZT20-LD_S30/phyC-ZT20-LD_S30_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
193RS1	193R-Bd21-3-LD-20C-ZT0	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT0	Bd21-3	20C	Bd21-3	LD	S1	0	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S1/193R-Bd21-3-LD-20C-ZT0_S1.stringtie.count
196RS1	196R-Bd21-3-LD-20C-ZT0	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT0	Bd21-3	20C	Bd21-3	LD	S1	0	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S1/196R-Bd21-3-LD-20C-ZT0_S1_Bd21-v3-1.stringtie.count
196RS2	196R-Bd21-3-LD-20C-ZT1	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT1	Bd21-3	20C	Bd21-3	LD	S2	1	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S2/196R-Bd21-3-LD-20C-ZT1_S2_Bd21-v3-1.stringtie.count
193RS2	193R-Bd21-3-LD-20C-ZT4	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT4	Bd21-3	20C	Bd21-3	LD	S2	4	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S2/193R-Bd21-3-LD-20C-ZT4_S2.stringtie.count
196RS3	196R-Bd21-3-LD-20C-ZT4	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT4	Bd21-3	20C	Bd21-3	LD	S3	4	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S3/196R-Bd21-3-LD-20C-ZT4_S3_Bd21-v3-1.stringtie.count
193RS3	193R-Bd21-3-LD-20C-ZT8	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT8	Bd21-3	20C	Bd21-3	LD	S3	8	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S3/193R-Bd21-3-LD-20C-ZT8_S3.stringtie.count
196RS4	196R-Bd21-3-LD-20C-ZT8	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT8	Bd21-3	20C	Bd21-3	LD	S4	8	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S4/196R-Bd21-3-LD-20C-ZT8_S4_Bd21-v3-1.stringtie.count
193RS4	193R-Bd21-3-LD-20C-ZT12	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT12	Bd21-3	20C	Bd21-3	LD	S4	12	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S4/193R-Bd21-3-LD-20C-ZT12_S4.stringtie.count
196RS5	196R-Bd21-3-LD-20C-ZT12	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT12	Bd21-3	20C	Bd21-3	LD	S5	12	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S5/196R-Bd21-3-LD-20C-ZT12_S5_Bd21-v3-1.stringtie.count
193RS5	193R-Bd21-3-LD-20C-ZT16	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT16	Bd21-3	20C	Bd21-3	LD	S5	16	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S5/193R-Bd21-3-LD-20C-ZT16_S5.stringtie.count
196RS6	196R-Bd21-3-LD-20C-ZT16	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT16	Bd21-3	20C	Bd21-3	LD	S6	16	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S6/196R-Bd21-3-LD-20C-ZT16_S6_Bd21-v3-1.stringtie.count
193RS6	193R-Bd21-3-LD-20C-ZT20	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT20	Bd21-3	20C	Bd21-3	LD	S6	20	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S6/193R-Bd21-3-LD-20C-ZT20_S6.stringtie.count
196RS7	196R-Bd21-3-LD-20C-ZT20	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT20	Bd21-3	20C	Bd21-3	LD	S7	20	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S7/196R-Bd21-3-LD-20C-ZT20_S7_Bd21-v3-1.stringtie.count
193RS7	193R-Bd21-3-LD-20C-ZT22	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT22	Bd21-3	20C	Bd21-3	LD	S7	22	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S7/193R-Bd21-3-LD-20C-ZT22_S7.stringtie.count
196RS8	196R-Bd21-3-LD-20C-ZT22	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT22	Bd21-3	20C	Bd21-3	LD	S8	22	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S8/196R-Bd21-3-LD-20C-ZT22_S8_Bd21-v3-1.stringtie.count
144RS11	Exp0024-ZT0-BdWT-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT0	Bd21-3	20C	Bd21-3	SD	S11	0	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT0-BdWT-SD_S11/Exp0024-ZT0-BdWT-SD_S11_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS12	Exp0024-ZT4-BdWT-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT4	Bd21-3	20C	Bd21-3	SD	S12	4	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT4-BdWT-SD_S12/Exp0024-ZT4-BdWT-SD_S12_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS13	Exp0024-ZT8-BdWT-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT8	Bd21-3	20C	Bd21-3	SD	S13	8	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT8-BdWT-SD_S13/Exp0024-ZT8-BdWT-SD_S13_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS14	Exp0024-ZT12-BdWT-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT12	Bd21-3	20C	Bd21-3	SD	S14	12	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT12-BdWT-SD_S14/Exp0024-ZT12-BdWT-SD_S14_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS15	Exp0024-ZT-8-BdWT-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT16	Bd21-3	20C	Bd21-3	SD	S15	16	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT-8-BdWT-SD_S15/Exp0024-ZT-8-BdWT-SD_S15_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS10	Exp0024-ZT-4-BdWT-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT20	Bd21-3	20C	Bd21-3	SD	S10	20	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT-4-BdWT-SD_S10/Exp0024-ZT-4-BdWT-SD_S10_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
193RS8	193R-bdelf3-LD-20C-ZT0	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT0	elf3-1	20C	Bd21-3	LD	S8	0	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S8/193R-bdelf3-LD-20C-ZT0_S8.stringtie.count
193RS9	193R-bdelf3-LD-20C-ZT4	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT4	elf3-1	20C	Bd21-3	LD	S9	4	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S9/193R-bdelf3-LD-20C-ZT4_S9.stringtie.count
193RS10	193R-bdelf3-LD-20C-ZT8	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT8	elf3-1	20C	Bd21-3	LD	S10	8	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S10/193R-bdelf3-LD-20C-ZT8_S10.stringtie.count
193RS11	193R-bdelf3-LD-20C-ZT12	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT12	elf3-1	20C	Bd21-3	LD	S11	12	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S11/193R-bdelf3-LD-20C-ZT12_S11.stringtie.count
193RS12	193R-bdelf3-LD-20C-ZT16	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT16	elf3-1	20C	Bd21-3	LD	S12	16	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S12/193R-bdelf3-LD-20C-ZT16_S12.stringtie.count
193RS13	193R-bdelf3-LD-20C-ZT20	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT20	elf3-1	20C	Bd21-3	LD	S13	20	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S13/193R-bdelf3-LD-20C-ZT20_S13.stringtie.count
193RS14	193R-bdelf3-LD-20C-ZT22	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT22	elf3-1	20C	Bd21-3	LD	S14	22	193R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/193R/S14/193R-bdelf3-LD-20C-ZT22_S14.stringtie.count
144RS17	Exp0024-ZT0-Bdelf3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT0	elf3-1	20C	Bd21-3	SD	S17	0	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT0-Bdelf3-SD_S17/Exp0024-ZT0-Bdelf3-SD_S17_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS18	Exp0024-ZT4-Bdelf3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT4	elf3-1	20C	Bd21-3	SD	S18	4	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT4-Bdelf3-SD_S18/Exp0024-ZT4-Bdelf3-SD_S18_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS19	Exp0024-ZT8-Bdelf3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT8	elf3-1	20C	Bd21-3	SD	S19	8	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT8-Bdelf3-SD_S19/Exp0024-ZT8-Bdelf3-SD_S19_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS20	Exp0024-ZT12-Bdelf3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT12	elf3-1	20C	Bd21-3	SD	S20	12	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT12-Bdelf3-SD_S20/Exp0024-ZT12-Bdelf3-SD_S20_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS21	Exp0024-ZT-8-Bdelf3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT16	elf3-1	20C	Bd21-3	SD	S21	16	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT-8-Bdelf3-SD_S21/Exp0024-ZT-8-Bdelf3-SD_S21_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
144RS16	Exp0024-ZT-4-Bdelf3-SD	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT20	elf3-1	20C	Bd21-3	SD	S16	20	144R	tophat	RNA-seq/Mapped_data/144R/bd21-3_and_elf3/Exp0024-ZT-4-Bdelf3-SD_S16/Exp0024-ZT-4-Bdelf3-SD_S16_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
196RS9	196R-Bd21-3-LD-20C-ZT0	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT0	ppd1-1	20C	Bd21-3	LD	S9	0	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S9/196R-Bd21-3-LD-20C-ZT0_S9_Bd21-v3-1.stringtie.count
196RS10	196R-ppd1-1-LD-20C-ZT1	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT1	ppd1-1	20C	Bd21-3	LD	S10	1	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S10/196R-ppd1-1-LD-20C-ZT1_S10_Bd21-v3-1.stringtie.count
196RS11	196R-ppd1-1-LD-20C-ZT4	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT4	ppd1-1	20C	Bd21-3	LD	S11	4	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S11/196R-ppd1-1-LD-20C-ZT4_S11_Bd21-v3-1.stringtie.count
196RS12	196R-ppd1-1-LD-20C-ZT8	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT8	ppd1-1	20C	Bd21-3	LD	S12	8	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S12/196R-ppd1-1-LD-20C-ZT8_S12_Bd21-v3-1.stringtie.count
196RS13	196R-ppd1-1-LD-20C-ZT12	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT12	ppd1-1	20C	Bd21-3	LD	S13	12	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S13/196R-ppd1-1-LD-20C-ZT12_S13_Bd21-v3-1.stringtie.count
196RS14	196R-ppd1-1-LD-20C-ZT16	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT16	ppd1-1	20C	Bd21-3	LD	S14	16	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S14/196R-ppd1-1-LD-20C-ZT16_S14_Bd21-v3-1.stringtie.count
196RS15	196R-ppd1-1-LD-20C-ZT20	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT20	ppd1-1	20C	Bd21-3	LD	S15	20	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S15/196R-ppd1-1-LD-20C-ZT20_S15_Bd21-v3-1.stringtie.count
196RS16	196R-ppd1-1-LD-20C-ZT22	softTemplate-sample-RNAseq-Ming	Bd	Wk3	ZT22	ppd1-1	20C	Bd21-3	LD	S16	22	196R	stringtie	RNA-seq/Mapped_data/pipeline_rnaseq/196R/S16/196R-ppd1-1-LD-20C-ZT22_S16_Bd21-v3-1.stringtie.count
143RS5	Exp0024-ZT20-BdWT	softTemplate-sample-RNAseq-Ming	Bd	Wk4	ZT0	Bd21-3	20C	Bd21-3	LD	S5	0	143R	tophat	RNA-seq/Mapped_data/143R/Exp0024-ZT20-BdWT_S5/Exp0024-ZT20-BdWT_S5_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
143RS1	Exp0024-ZT8-BdWT	softTemplate-sample-RNAseq-Ming	Bd	Wk4	ZT8	Bd21-3	20C	Bd21-3	LD	S1	8	143R	tophat	RNA-seq/Mapped_data/143R/Exp0024-ZT8-BdWT_S1/Exp0024-ZT8-BdWT_S1_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
143RS3	Exp0024-ZT16-BdWT	softTemplate-sample-RNAseq-Ming	Bd	Wk4	ZT16	Bd21-3	20C	Bd21-3	LD	S3	16	143R	tophat	RNA-seq/Mapped_data/143R/Exp0024-ZT16-BdWT_S3/Exp0024-ZT16-BdWT_S3_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
143RS6	Exp0024-ZT20-Bdphyc	softTemplate-sample-RNAseq-Ming	Bd	Wk4	ZT0	phyC-4	20C	Bd21-3	LD	S6	0	143R	tophat	RNA-seq/Mapped_data/143R/Exp0024-ZT20-Bdphyc_S6/Exp0024-ZT20-Bdphyc_S6_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
143RS2	Exp0024-ZT8-Bdphyc	softTemplate-sample-RNAseq-Ming	Bd	Wk4	ZT8	phyC-4	20C	Bd21-3	LD	S2	8	143R	tophat	RNA-seq/Mapped_data/143R/Exp0024-ZT8-Bdphyc_S2/Exp0024-ZT8-Bdphyc_S2_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
143RS4	Exp0024-ZT16-Bdphyc	softTemplate-sample-RNAseq-Ming	Bd	Wk4	ZT16	phyC-4	20C	Bd21-3	LD	S4	16	143R	tophat	RNA-seq/Mapped_data/143R/Exp0024-ZT16-Bdphyc_S4/Exp0024-ZT16-Bdphyc_S4_trimmo_paired_2_10_5_1_tophat_Bd_nomixed_sorted_rmdup_picard_combined_read.txt
'''
rnaCurr = pyutil.read__buffer(buf,ext='tsv')
sortKeys = ['Age','gtype','light','temp','ZTime_int']
dispKeys = ['pipeline','Age','gtype','light','temp','ZTime']
rnaCurr = rnaCurr.sort_values(sortKeys)
# rnaCurr[dispKeys]

rnaDF = pyutil.readBaseFile('results/0131__dumpDataRNA__Brachy/rna_raw.pk')

rnaDF = rnaDF.reindex(columns=rnaCurr.index)
mcurr = rnaCurr[dispKeys].reset_index()
rnaDF.columns = pd.MultiIndex.from_arrays(mcurr.values.T,names=mcurr.columns)
rnaDF.index = rnaDF.index.str.split('.',1).str.get(0)
rnaDF.to_csv('TPM__table.csv')

it = rnaDF.groupby(axis=1,level=dispKeys[:-1])
pyext.it__toExcel(it,'TPM__table.xls')

# rnaDF.to_excel('TPM__table.xls')
# rnaDF.to_excel('TPM__table.xlsx')