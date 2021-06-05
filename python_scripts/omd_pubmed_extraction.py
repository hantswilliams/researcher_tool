#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:21:55 2021

@author: hantswilliams


References: 
    
    https://docs.google.com/document/d/1YUHKbUr_cVSfNy0I_s040xFqbs8sowBL/edit# 
    https://docs.google.com/document/d/1MscEAcqp7dAfoJ8Gff86aeI8lou87lLnwOMdzxHok0A/edit 


https://pubmed.ncbi.nlm.nih.gov/32021216/



Individual Articles - SUMMARY 

https://pubmed.ncbi.nlm.nih.gov/33658867/ 
https://pubmed.ncbi.nlm.nih.gov/31846068/ 
https://pubmed.ncbi.nlm.nih.gov/30098660/ 
https://pubmed.ncbi.nlm.nih.gov/32498577/ 
https://pubmed.ncbi.nlm.nih.gov/30457075/
https://pubmed.ncbi.nlm.nih.gov/26425446/
https://pubmed.ncbi.nlm.nih.gov/29761488/ 
https://pubmed.ncbi.nlm.nih.gov/24284258/ 
https://pubmed.ncbi.nlm.nih.gov/26012350/ 
https://pubmed.ncbi.nlm.nih.gov/32130308/
https://pubmed.ncbi.nlm.nih.gov/31526204/    # predicting response -> early response is important to treatment 
https://pubmed.ncbi.nlm.nih.gov/31357161/    # inflammatory markers 
https://pubmed.ncbi.nlm.nih.gov/30071387/ 
https://pubmed.ncbi.nlm.nih.gov/29596148/
https://pubmed.ncbi.nlm.nih.gov/27155594/     # predictors / 
https://pubmed.ncbi.nlm.nih.gov/25305428/
https://pubmed.ncbi.nlm.nih.gov/23870720/ 

https://effectivehealthcare.ahrq.gov/sites/default/files/pdf/treatment-resistant-depression_research.pdf










## General Searches 


treatment resistant depression[Title]
     
#1324 all                  https://pubmed.ncbi.nlm.nih.gov/?term=treatment+resistant+depression%5BTitle%5D&sort=date&filter=pubt.systematicreview&filter=pubt.systematicreview
#47 systematic review      https://pubmed.ncbi.nlm.nih.gov/?term=treatment+resistant+depression%5BTitle%5D&sort=date&size=50

treatment resistant depression[Title/Abstract]
#276  all                               https://pubmed.ncbi.nlm.nih.gov/?term=treatment+resistant+depression%5BTitle%2FAbstract%5D&sort=date&size=50 
#115 systematic review                  https://pubmed.ncbi.nlm.nih.gov/?term=treatment+resistant+depression%5BTitle%2FAbstract%5D&sort=date&filter=pubt.systematicreview&filter=pubt.systematicreview
#540  complenentary medicine            https://pubmed.ncbi.nlm.nih.gov/?term=treatment+resistant+depression%5BTitle%2FAbstract%5D&filter=subject.cam&sort=date&size=50
#31   complemetnary medicine + review   https://pubmed.ncbi.nlm.nih.gov/?term=treatment+resistant+depression%5BTitle%2FAbstract%5D&filter=pubt.systematicreview&filter=subject.cam&sort=date&size=50





https://pubmed.ncbi.nlm.nih.gov/clinical/?term=%22treatment+resistant+depression%22&clinical_study_category=prognosis 

"treatment resistant depression"

TRAETMENT: 
TRAETMENT: 
    

therapy 
// narrow 
#353    https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Therapy/Narrow[filter])&sort=date
therapy // broad 
#1707   https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Therapy/Broad[filter])&sort=date

clinical prediction guideliness // 
// narrow     
#40     https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Clinical%20Prediction%20Guides/Narrow[filter])&sort=date
// broad    
#1044   https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Clinical%20Prediction%20Guides/Broad[filter])&sort=date 

diagnosis 
// narrow 
#35     https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Diagnosis/Narrow[filter])&sort=date
// broad
#656    https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Diagnosis/Broad[filter])&sort=date

etiology 
// narrow 
#176    https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Etiology/Narrow[filter])&sort=date
// broad 
#1063   https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Etiology/Broad[filter])&sort=date

prognosis 
// narrow 
# 186   https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Prognosis/Narrow[filter])&sort=date
// broad 
# 659    https://pubmed.ncbi.nlm.nih.gov/?term=(%22treatment%20resistant%20depression%22)%20AND%20(Prognosis/Broad[filter])&sort=date

 














"""

