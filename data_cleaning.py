# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:12:47 2022

@author: bckandemir2018
"""

import pandas as pd

df=pd.read_csv("glassdoor_jobs.csv")

#salary parsing

df["hourly"]=df["Salary Estimate"].apply(lambda x: 1 if "per hour" in x.lower() else 0)
df["hourly"]=df["Salary Estimate"].apply(lambda x: 1 if "employer provided salary" in x.lower() else 0)

"there are some -1 values in Salary Estimate column we hsould remove it. They were (956,15).After we removed it ,it turned (742,15)"

df=df[df["Salary Estimate"]!="-1"] 
salary=df["Salary Estimate"].apply(lambda x: x.split("(")[0])

minus_kd=salary. apply(lambda x: x.replace("$","").replace("K",""))
min_hr=minus_kd.apply(lambda x: x.lower().replace("per hour","").replace("employer provided salary:",""))

df["min_salary"]=min_hr.apply(lambda x :int(x.split("-")[0]))
df["max_salary"]=min_hr.apply(lambda x :int(x.split("-")[1]))
df["avg_salary"]=(df["min_salary"]+df["max_salary"])/2


#company name etxt only
df["company_txt"]=df.apply(lambda x: x["Company Name"] if x["Rating"]<0 else x["Company Name"][:-3],axis=1)

#state field

df["job state"]=df["Location"].apply(lambda x: x.split(", ")[1])

df["same_state"]=df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

#age of company

df["age"]=df["Founded"].apply(lambda x: 1 if x<2 else (2022-x))

#parsing of job description (python, etc)

#python
df["python_yn"]=df["Job Description"].apply(lambda x: 1 if "python" in x.lower() else 0)
df.python_yn.value_counts()
#r studio
df["R_yn"]=df["Job Description"].apply(lambda x: 1 if "r studio" in x.lower() or "r-studio" else 0)
#spark
df["spark"]=df["Job Description"].apply(lambda x: 1 if "spark" in x.lower() else 0)
#aws
df["aws"]=df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)
df.aws.value_counts()
#excel
df["excel"]=df["Job Description"].apply(lambda x: 1 if "excel" in x.lower() else 0)
df.excel.value_counts()

df.columns
df_out=df.drop(["Unnamed: 0"], axis=1)

df_out.to_csv("salary_data_cleaned.csv",index=False)