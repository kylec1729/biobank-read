# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:38:15 2018

@author: wcrum
"""

import os
import subprocess
import sys

# Not really needed, but for reference
variables = ['Encoded anonymised participant ID',
 'Heel ultrasound method',
 'Weight method',
 'Sex',
 'Year of birth',
 'Hand grip strength (left)',
 'Hand grip strength (right)',
 'Waist circumference',
 'Hip circumference',
 'Standing height',
 'Month of birth',
 'Date of attending assessment centre',
 'UK Biobank assessment centre',
 'Cancer year/age first occurred',
 'Non-cancer illness year/age first occurred',
 'Systolic blood pressure, manual reading',
 'Diastolic blood pressure, manual reading',
 'Pulse rate (during blood-pressure measurement)',
 'Pulse rate, automated reading',
 'Birth weight known',
 'Place of birth in UK - north co-ordinate',
 'Place of birth in UK - east co-ordinate',
 'Number of self-reported cancers',
 'Number of self-reported non-cancer illnesses',
 'Townsend deprivation index at recruitment',
 'Type of accommodation lived in',
 'Own or rent accommodation lived in',
 'Time employed in main current job',
 'Length of working week for main job',
 'Frequency of travelling from home to job workplace',
 'Distance between home and job workplace',
 'Job involves mainly walking or standing',
 'Job involves heavy manual or physical work',
 'Job involves shift work',
 'Number of days/week walked 10+ minutes',
 'Duration of walks',
 'Number of days/week of moderate physical activity 10+ minutes',
 'Duration of moderate activity',
 'Number of days/week of vigorous physical activity 10+ minutes',
 'Duration of vigorous activity',
 'Frequency of friend/family visits',
 'Time spend outdoors in summer',
 'Time spent outdoors in winter',
 'Length of mobile phone use',
 'Weekly usage of mobile phone in last 3 months',
 'Sleep duration',
 'Getting up in morning',
 'Morning/evening person (chronotype)',
 'Nap during day',
 'Sleeplessness / insomnia',
 'Current tobacco smoking',
 'Past tobacco smoking',
 'Cooked vegetable intake',
 'Salad / raw vegetable intake',
 'Fresh fruit intake',
 'Dried fruit intake',
 'Oily fish intake',
 'Non-oily fish intake',
 'Processed meat intake',
 'Poultry intake',
 'Alcohol intake frequency.',
 'Country of birth (UK/elsewhere)',
 'Breastfed as a baby',
 'Handedness (chirality/laterality)',
 'Skin colour',
 'Ease of skin tanning',
 'Childhood sunburn occasions',
 'Adopted as a child',
 'Part of a multiple birth',
 'Able to confide',
 'Wears glasses or contact lenses',
 'Age started wearing glasses or contact lenses',
 'Chest pain or discomfort',
 'Taking other prescription medications',
 'Light smokers, at least 100 smokes in lifetime',
 'Ever had breast cancer screening / mammogram',
 'Years since last breast cancer screening / mammogram',
 'Ever had cervical smear test',
 'Years since last cervical smear test',
 'Age when periods started (menarche)',
 'Had menopause',
 'Age high blood pressure diagnosed',
 'Forced vital capacity (FVC)',
 'Forced expiratory volume in 1-second (FEV1)',
 'Peak expiratory flow (PEF)',
 'Foot measured for bone density',
 'Fractured heel',
 'Contra-indications for spirometry',
 'Caffeine drink within last hour',
 'Used an inhaler for chest within last hour',
 'Pregnant',
 'Ankle spacing width',
 'Heel Broadband ultrasound attenuation, direct entry',
 'Heel quantitative ultrasound index (QUI), direct entry',
 'Heel bone mineral density (BMD)',
 'Weight, manual entry',
 'Job involve night shift work',
 'Age started smoking in current smokers',
 'Chest pain or discomfort walking normally',
 'Chest pain due to walking ceases when standing still',
 'Age angina diagnosed',
 'Former alcohol drinker',
 'Chest pain or discomfort when walking uphill or hurrying',
 'Age heart attack diagnosed',
 'Age stroke diagnosed',
 'Diastolic blood pressure, automated reading',
 'Systolic blood pressure, automated reading',
 'Stiffness method',
 'Pulse rate',
 'Pulse wave reflection index',
 'Pulse wave peak to peak time',
 'Pulse wave pressure versus time response curve',
 'Pulse wave velocity (manual entry)',
 'Average monthly red wine intake',
 'Average monthly champagne plus white wine intake',
 'Average monthly beer plus cider intake',
 'Average monthly spirits intake',
 'Average monthly fortified wine intake',
 'Leg pain on walking',
 'Intra-ocular pressure (IOP) method (right)',
 'Intra-ocular pressure (IOP) method (left)',
 'Corneal hysteresis (right)',
 'Corneal hysteresis (left)',
 'Leg pain when standing still or sitting',
 'Leg pain in calf/calves',
 'Leg pain when walking uphill or hurrying',
 'Leg pain when walking normally',
 'Which eye(s) affected by hypermetropia (long sight)',
 'Which eye(s) affected by myopia (short sight)',
 'Doctor restricts physical activity due to heart condition',
 'Chest pain felt during physical activity',
 'Qualifications',
 'Gas or solid-fuel cooking/heating',
 'Heating type(s) in home',
 'Current employment status',
 'Transport type for commuting to job workplace',
 'Reason for glasses/contact lenses',
 'Vascular/heart problems diagnosed by doctor',
 'Blood clot, DVT, bronchitis, emphysema, asthma, rhinitis, eczema, allergy diagnosed by doctor',
 'Medication for cholesterol, blood pressure, diabetes, or take exogenous hormones',
 'Medication for pain relief, constipation, heartburn',
 'Vitamin and mineral supplements',
 'Leisure/social activities',
 'Medication for cholesterol, blood pressure or diabetes',
 'Mineral and other dietary supplements',
 'Medication for pain relief, constipation, heartburn (pilot)',
 'Medication for smoking cessation, constipation, heartburn, allergies (pilot)',
 'Vitamin and mineral supplements (pilot)',
 'Regular use of hands-free device/speakerphone with mobile phone (pilot)',
 'Data points for blow (pilot)',
 'Vitamin supplements (pilot)',
 'Frequency of friend/family visits (pilot)',
 'Time using mobile phone in last 3 months (pilot)',
 'Other dietary supplements (pilot)',
 'Gas or solid-fuel cooking/heating (pilot)',
 'Cancer code, self-reported',
 'Non-cancer illness code, self-reported',
 'Interpolated Year when cancer first diagnosed',
 'Interpolated Age of participant when cancer first diagnosed',
 'Interpolated Year when non-cancer illness first diagnosed',
 'Interpolated Age of participant when non-cancer illness first diagnosed',
 'Method of recording time when cancer first diagnosed',
 'Method of recording time when non-cancer illness first diagnosed',
 'Sitting height',
 'Birth weight',
 'Acceptability of each blow result (text)',
 'Acceptability of each blow result (text) (pilot)',
 'Reason for skipping weight',
 'Reason for skipping spirometry',
 'Reason for skipping grip strength (right)',
 'Reason for skipping grip strength (left)',
 'Reason for skipping waist',
 'Reason for skipping hip measurement',
 'Reason for skipping standing height',
 'Reason for skipping sitting height',
 'Reason for skipping arterial stiffness',
 'Reason for skipping IOP (right)',
 'Reason for skipping IOP (left)',
 'Reason for skipping ECG',
 'Reason ECG not completed',
 'Reason at-rest ECG performed without bicycle',
 'Number of diet questionnaires completed',
 'When diet questionnaire completion requested',
 'Day-of-week questionnaire completion requested',
 'Day-of-week questionnaire completed',
 'Hour-of-day questionnaire completed',
 'Duration of questionnaire',
 'Delay between questionnaire request and completion',
 'Vitamin and/or mineral supplement use',
 'Reason for not eating or drinking normally',
 'Type of special diet followed',
 'Types of spreads/sauces consumed',
 'Type of meals eaten',
 'Type of fat/oil used in cooking',
 'Type of sliced bread eaten',
 'Type of baguette eaten',
 'Type of large bap eaten',
 'Type of bread roll eaten',
 'Size of white wine glass drunk',
 'Size of red wine glass drunk',
 'Size of rose wine glass drunk',
 'Liquid used to make porridge',
 'Type of yogurt eaten',
 'Country of Birth (non-UK origin)',
 'Smoking status',
 'Alcohol drinker status',
 'Current employment status - corrected',
 'Reproduciblity of spirometry measurement using ERS/ATS criteria',
 'Ethnic background',
 'Body mass index (BMI)',
 'Weight',
 'Age when attended assessment centre',
 'Pulse wave Arterial Stiffness index',
 'Age at recruitment',
 'Genotype measurement batch',
 'Genetic sex',
 'Heterozygosity',
 'Heterozygosity, PCA corrected',
 'Missingness',
 'Genetic ethnic grouping',
 'Genotype measurement plate',
 'Genotype measurement well',
 'Genetic principal components',
 'Recommended genomic analysis exclusions',
 'Genetic relatedness pairing',
 'Genetic relatedness factor',
 'Genetic relatedness IBS0',
 'UKBiLEVE Affymetrix quality control for samples',
 'Chromosome 1 genotype results',
 'Chromosome 2 genotype results',
 'Chromosome 3 genotype results',
 'Chromosome 4 genotype results',
 'Chromosome 5 genotype results',
 'Chromosome 1 genotype intensities',
 'Chromosome 2 genotype intensities',
 'Chromosome 3 genotype intensities',
 'Chromosome 4 genotype intensities',
 'Chromosome 5 genotype intensities',
 'Chromosome 6 genotype intensities',
 'Chromosome 7 genotype intensities',
 'Chromosome 8 genotype intensities',
 'Nitrogen dioxide air pollution; 2010',
 'Nitrogen oxides air pollution; 2010',
 'Particulate matter air pollution (pm10); 2010',
 'Particulate matter air pollution (pm2.5); 2010',
 'Particulate matter air pollution (pm2.5) absorbance; 2010',
 'Particulate matter air pollution 2.5-10um; 2010',
 'Traffic intensity on the nearest road',
 'Inverse distance to the nearest road',
 'Traffic intensity on the nearest major road',
 'Inverse distance to the nearest major road',
 'Total traffic load on major roads',
 'Close to major road',
 'Sum of road length of major roads within 100m',
 'Nitrogen dioxide air pollution; 2005',
 'Nitrogen dioxide air pollution; 2006',
 'Nitrogen dioxide air pollution; 2007',
 'Particulate matter air pollution (pm10); 2007',
 'Average daytime sound level of noise pollution',
 'Average evening sound level of noise pollution',
 'Average night-time sound level of noise pollution',
 'Average 16-hour sound level of noise pollution',
 'Average 24-hour sound level of noise pollution',
 'Microalbumin in urine',
 'Microalbumin in urine result flag',
 'Creatinine (enzymatic) in urine',
 'Creatinine (enzymatic) in urine result flag',
 'Potassium in urine',
 'Potassium in urine result flag',
 'Sodium in urine',
 'Sodium in urine result flag',
 'Date of death',
 'Underlying (primary) cause of death: ICD10',
 'Contributory (secondary) causes of death: ICD10',
 'Age at death',
 'Description of cause of death',
 'Episodes containing "Diagnoses - secondary ICD9" data',
 'Episodes containing "Diagnoses - secondary ICD10" data',
 'Episodes containing "Dates of operations" data',
 'Episodes containing "Episode start date" data',
 'Episodes containing "Episode end date" data',
 'Episodes containing "Date of admission to hospital" data',
 'Episodes containing "Date of discharge from hospital" data',
 'Episodes containing "Operation status" data',
 'Episodes containing "Diagnoses - main ICD10" data',
 'Episodes containing "Diagnoses - main ICD9" data',
 'Episodes containing "Operative procedure - main OPCS" data',
 'Episodes containing "Date of operation" data',
 'Episodes containing "Source of inpatient record" data',
 'Food weight',
 'Energy',
 'Protein',
 'Fat',
 'Carbohydrate',
 'Saturated fat',
 'Polyunsaturated fat',
 'Total sugars',
 'Englyst dietary fibre',
 'Portion size',
 'Iron',
 'Vitamin B6',
 'Vitamin B12',
 'Folate',
 'Vitamin C',
 'Potassium',
 'Magnesium',
 'Retinol',
 'Carotene',
 'Typical diet yesterday',
 'Vitamin D',
 'Alcohol',
 'Starch',
 'Calcium',
 'Vitamin E',
 'Drinking water intake',
 'Low calorie drink intake',
 'Fizzy drink intake',
 'Squash intake',
 'Orange juice intake',
 'Grapefruit juice intake',
 'Pure fruit/vegetable juice intake',
 'Fruit smoothie intake',
 'Alcohol consumed',
 'Red wine intake',
 'Rose wine intake',
 'White wine intake',
 'Breakfast cereal consumed',
 'Porridge intake',
 'Muesli intake',
 'Oat crunch intake',
 'Sweetened cereal intake',
 'Type milk consumed',
 'Bread consumed',
 'Sliced bread intake',
 'Baguette intake',
 'Bap intake',
 'Bread roll intake',
 'Naan bread intake',
 'Garlic bread intake',
 'Crispbread intake',
 'Oatcakes intake',
 'Other bread intake',
 'Double crust pastry intake',
 'Single crust pastry intake',
 'Crumble intake',
 'Pizza intake',
 'Pancake intake',
 'Scotch pancake intake',
 'Yorkshire pudding intake',
 'Indian snacks intake',
 'Croissant intake',
 'Danish pastry intake',
 'Scone intake',
 'Yogurt/ice-cream consumers',
 'Yogurt intake',
 'Ice-cream intake',
 'Dessert consumers',
 'Milk-based pudding intake',
 'Other milk-based pudding intake',
 'Soya dessert intake',
 'Fruitcake intake',
 'Cake intake',
 'Doughnut intake',
 'Sponge pudding intake',
 'Cheesecake intake',
 'Cheese consumers',
 'Low fat hard cheese intake',
 'Hard cheese intake',
 'Soft cheese intake',
 'Blue cheese intake',
 'Meat consumers',
 'Sausage intake',
 'Beef intake',
 'Pork intake',
 'Lamb intake',
 'Crumbed or deep-fried poultry intake',
 'Vegetarian alternatives intake',
 'Vegetarian sausages/burgers intake',
 'Tofu intake',
 'Quorn intake',
 'Other vegetarian alternative intake',
 'Spreads/sauces consumers',
 'No fat for cooking',
 'Vegetable consumers',
 'Baked bean intake',
 'Pulses intake',
 'Fried potatoes intake',
 'Boiled/baked potatoes intake',
 'Butter/margarine added to potatoes',
 'Mashed potato intake',
 'Added salt to food',
 'Vitamin supplement user',
 'Time spent doing vigorous physical activity',
 'Time spent doing moderate physical activity',
 'Time spent doing light physical activity',
 'When diet questionnaire completed',
 'When diet questionnaire started',
 'Invitation to complete online 24-hour recall dietary questionnaire, acceptance',
 'Invitation to complete online 24-hour recall dietary questionnaire, date sent']

# ----> SET SOMETHING HERE!
# Set the script to test here
scriptList = ['extract_variables.py', 'extract_death.py', 'extract_SR.py', 'HES_extract.py']
scriptdic = {'VAR' : 0, 'DEATH' : 1, 'SR' : 2, 'HES' : 3}
scriptnum = scriptdic['VAR']

# The name of the script to test
scriptname = scriptList[scriptnum];


# Where the data is stored
csvpath = 'Z:\\EABOAGYE\\Users\\wcrum\\Projects\\UKBB\\UKBB-data-2018\\ukb21204.csv'
htmlpath =  'Z:\\EABOAGYE\\Users\\wcrum\\Projects\\UKBB\\UKBB-data-2018\\ukb21204.html'
exclpath =  'Z:\\EABOAGYE\\Users\\wcrum\\Projects\\UKBB\\UKBB-data-2018\\w10035_20180503_exclusions.csv'
hespath = 'Z:\\EABOAGYE\\Users\\wcrum\\Projects\\UKBB\\UKBB-data-2018\\ukb.tsv'

# Output
outpath = 'H:\\IC-Stuff\\software\\Biobank'
outname = 'testnewVARpartial'
outfile = os.path.join(outpath, outname)

# Construct script path and arguments for each script
if scriptname == 'extract_variables.py':
    # Variables and conditions
    varList = ['"Age when attended assessment centre"', '"Body mass index (BMI)"', '"Age high blood pressure diagnosed"']
    varString = ' '.join(varList)
    #varString = 'H:\\IC-Stuff\\software\\Biobank\\BiobankRead-Bash\\vars_test.txt'
    filterList = ['"Age when attended assessment centre>50"', '"Age when attended assessment centre<70"', '"Body mass index (BMI)>=23"', '"Body mass index (BMI)<=30"']
    # Command string
    bbreadargs = [scriptname, 
                ' --csv '+csvpath, 
                ' --html '+htmlpath, 
                ' --vars ' + varString, 
                ' --filter ' + ' '.join(filterList), 
                ' --remove_outliers True', 
                ' --baseline_only False', 
                ' --excl '+exclpath,
                ' --cov_corr True', 
                ' --aver_visits False', 
                ' --combine partial', 
                ' --out ' + outfile]
elif scriptname == 'extract_death.py':
    # Data file for codes or use list e.g. ' --codes C34  C42'
    codespath = 'H:\\IC-Stuff\\software\\Biobank\\codes1.txt'
    # Command string
    bbreadargs = [scriptname, 
                ' --csv '+csvpath, 
                ' --html '+htmlpath, 
                ' --codes '+codespath,
                ' --primary True', 
                ' --secondary False',
                ' --excl '+exclpath,
                ' --out ' + outfile]
elif scriptname == 'extract_SR.py':
    # Command string
    # Note use of "" to prevent argsparse breaking up the disease string
    bbreadargs = [scriptname, 
                ' --csv '+csvpath, 
                ' --html '+htmlpath, 
                ' --baseline_only False', 
                ' --disease "lung cancer" "breast cancer"',
                ' --SRcancer True', 
                ' --excl '+exclpath,
                ' --out ' + outfile]
elif scriptname == 'HES_extract.py':
    # Data file for codes or use list e.g. ' --codes C34  C42'
    codespath = 'H:\\IC-Stuff\\software\\Biobank\\codes.txt'
    # ICD9, ICD10, OPCS
    codetype = 'ICD10'
    # epistart or admidate
    datetype = 'epistart'
    # Command string
    bbreadargs = [scriptname, 
                ' --csv '+csvpath, 
                ' --html '+htmlpath, 
                ' --tsv '+hespath,
                ' --excl '+exclpath,
                ' --codes '+codespath,
                ' --codeType '+ codetype, 
                ' --dateType '+ datetype,
                ' --firstvisit True', 
                ' --baseline True', 
                ' --out ' + outfile]
else:
    print 'error: scriptname =', scriptname, 'not recognised'
    sys.exit(1)

# Make command-line
# Note  append is required here
subprocessargs = ['python']
subprocessargs.append(bbreadargs)

# Output command line
print
print subprocessargs[0], ' '.join(subprocessargs[1])

subprocessargs[1]=' '.join(subprocessargs[1])
#print
#print type(subprocessargs[0]), type(subprocessargs[1])
# Run as sub-process to ensure arguments are passed correctly
print
print 'Running as sub-process, please wait...'
subprocess.call(subprocessargs,shell=True)





