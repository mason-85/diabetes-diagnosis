***0- project Goal***
The aim of this project is to predict the if a patient is suffering from diabetes. A sample of datset has been demonstrated as follows:

Diabetes_012	HighBP	HighChol	CholCheck	BMI	Smoker	Stroke	HeartDiseaseorAttack	PhysActivity	Fruits	Veggies	HvyAlcoholConsump	AnyHealthcare	NoDocbcCost	GenHlth	MentHlth	PhysHlth	DiffWalk	Sex	Age	Education	Income
0	1	0	1	27	1	0	0	0	0	0	0	1	0	4	0	5	1	0	11	4	2
1	0	1	1	33	1	0	0	1	1	1	0	1	0	3	0	0	1	0	9	5	3
0	1	1	1	38	1	1	1	0	1	1	0	1	0	4	10	5	1	1	11	5	6
2	1	1	1	28	0	0	0	0	0	1	0	1	0	4	0	0	1	0	11	4	6
0	0	0	1	32	0	0	0	1	0	0	0	1	0	3	0	0	0	0	7	4	3
![image](https://github.com/mason-85/diabetes-prognosis/assets/156556839/151bd2c3-f5e0-4750-91a5-811bf21951ba)


***1- Code Description***

Refere to the ".ipynb" file for complete description. All cells and the reason(s) behind each decision have been elaborated in the ".ipynb"
file.</br>

***2- Dataset Link***

The link of the dataset is available in the ".ipynb" file.</br>
Please note that only the first five percent of the dataset has been utalized for this code to lessen the processing time.
The best classification metrics were obtained for the 'RandomForest'(RF) method. Given that, the output model of the RF has been saved as
"grid_search_rf.h5".
