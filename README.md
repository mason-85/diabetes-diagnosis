***0- project Goal***</br></br>

The objective of this project is to predict whether a patient is suffering from diabetes. A sample dataset is presented below:

![image](https://github.com/mason-85/diabetes-prognosis/assets/156556839/151bd2c3-f5e0-4750-91a5-811bf21951ba)

The description of each column is presented herein:</br></br>
Target:</br>
  
**Diabetes_012:** 0 = no diabetes / 1 = prediabetes / 2 = diabetes

features / attributes:</br>

**HighBP:** 0 = no high BP / 1 = high BP

**HighChol:** 0 = no high cholesterol / 1 = high cholesterol

**CholCheck:** 0 = no cholesterol check in 5 years / 1 = yes cholesterol check in 5 years

**BMI:** Body Mass Index

**Smoker:** Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no / 1 = yes

**Stroke:** (Ever told) you had a stroke. 0 = no / 1 = yes

**HeartDiseaseorAttack:** coronary heart disease (CHD) or myocardial infarction (MI) 0 = no / 1 = yes

**PhysActivity:** physical activity in past 30 days - not including job 0 = no / 1 = yes

**Fruits:** Consume Fruit 1 or more times per day 0 = no / 1 = yes

**Veggies:** Consume Vegetables 1 or more times per day 0 = no / 1 = yes

**HvyAlcoholConsump:** Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) 0 = no / 1 = yes

**AnyHealthcare:** Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. 0 = no / 1 = yes

**NoDocbcCost:** Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? 0 = no / 1 = yes

**GenHlth:** Would you say that in general your health is: scale 1-5 / 1 = excellent / 2 = very good / 3 = good / 4 = fair / 5 = poor

**MentHlth:** Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how

**PhysHlth:** Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30

**DiffWalk:** Do you have serious difficulty walking or climbing stairs? 0 = no / 1 = yes

**Sex:** 0 = female / 1 = male

**Age:** 13-level age category (_AGEG5YR see codebook) 1 = 18-24 / 9 = 60-64 / 13 = 80 or older

**Education:** Education level (EDUCA see codebook) scale 1-6 / 1 = Never attended school or only kindergarten / 2 = Grades 1 through 8

**Income:** Income scale (INCOME2 see codebook) scale 1-8 / 1 = less than $10,000 / 5 = less than $35,000 / 8 = $75,000 or more</br></br>

***1- Code Description***</br></br>

Refere to the ".ipynb" file for complete description. All cells and the reason(s) behind each decision have been elaborated in the ".ipynb"
file.</br></br>

***2- Dataset Link***

The link of the dataset is available in the ".ipynb" file.</br>
Please note that only the first five percent of the dataset has been utilized for this code to reduce processing time.</br></br>

***3- Saved Model***</br></br>

The best classification metrics were achieved with the 'RandomForest' (RF) method. Consequently, the output model of the RF has been saved as "rf_model.pkl". This model will be utilized for the API code.

***4- API***</br></br>

The code is provided in "dp_api.py". This file needs to be used to deploy the model on the target website(s)..</br></br>

***5- Requirements.txt***</br></br>

In this project, Heroku is the chosen cloud platform. The necessary dependencies and libraries are specified in this file to be installed on Heroku.</br></br>

***6- diabetes.csv***</br></br>

A truncated dataset comprising five percent of the original dataset, referenced in the previous link, is utilized in this project.</br></br>

***7- Procfile***</br></br>

This file contains the mechanism for specifying the commands to be executed by the application's dynos on the Heroku platform.</br></br>

***8- runtime.txt***</br></br>

It specifies the version of Python.

