import pandas as pd
import numpy as np
from scipy import stats
import os

#Understanding NullHypo(Ho) and alternate Hypothesis(H1)

# Null Hypothesis (H₀): This hypothesis assumes that there is no significant difference, effect, or relationship between the 
#                  variables we are studying. It represents the status quo or the absence of an effect. It's often formulated 
#                  to represent the opposite of what we are trying to show with our study.

# Alternative Hypothesis (H₁): This hypothesis proposes the opposite of the null hypothesis. It suggests that there is indeed a 
#                         significant difference, effect, or relationship between the variables. It's what we are trying to determine 
#                         or demonstrate with our study.

# For example, let's say you want to test whether a new drug is effective in treating a certain disease. The null hypothesis in this case might be that there 
# is no difference in the effectiveness of the new drug compared to the existing treatment or a placebo.

# In statistics, we often try to reject the null hypothesis based on evidence from our data. If we find enough evidence to reject the null hypothesis, 
# it suggests that there is indeed a difference, effect, or relationship between the variables we're studying. If we don't find enough evidence, we fail to 
# reject the null hypothesis, but we don't necessarily prove it to be true.

# In summary, the null hypothesis is a starting point for statistical testing, and we try to gather evidence to either reject or fail to reject it based on the data we have.  

df=pd.read_csv('C:\\Users\\user\\Desktop\\IBM_bckEnd\\Python\\NumPy\\scores.csv')
# print(df.shape)
# print(df)  

#in this project our Null hypo assumes that there is no potential difference between
#female scores and male scores . . .

def computeTandP(male_array,female_array):
    T_value=0
    P_value=0
    
    mean1=np.mean(male_array)
    mean2=np.mean(female_array)

    std_devi_1=np.std(male_array)
    std_devi_2=np.std(female_array)

    variance= (((male_array.size-1)*(std_devi_1**2)) + ((female_array.size-1)*(std_devi_2**2)))/(male_array.size+female_array.size-2)
    #Pooled standard deviation= sqrt of variance
    Pooled_std=np.sqrt(variance)

    #Calculate the standard error: Standard_error=pooled_st_deviation* sqrt(1/n1 + 1/n2)
    std_error=Pooled_std*np.sqrt(1/male_array.size + 1/female_array.size)

    #T value: 
    T_value=(mean1-mean2)/std_error

    #deg_of_freedom
    deg_of_freedom=male_array.size + female_array.size - 2
    P_value=2*(1-stats.t.cdf(T_value,deg_of_freedom))
    
    return T_value,P_value

def remove_Outliers(arr):
    Q3=np.percentile(arr,75)
    Q1=np.percentile(arr,25)
     
    inter_quartile_range=Q3-Q1

    lower_limit=Q1-1.5*inter_quartile_range
    upper_limit=Q3+1.5*inter_quartile_range

    arr= arr[(arr>=lower_limit)&(arr<=upper_limit)]

    return arr

female_array=df.loc[df['gender']=='female','math score'].values

male_array=df.loc[df['gender']=='male','math score'].values 

# print(female_array)
# print(male_array)

female_array=remove_Outliers(female_array)    
male_array=remove_Outliers(male_array)

t,p=computeTandP(male_array,female_array)
print('T_value: ',t)  #Output: 5.388622...  (Without removing outliers)
print("P_value:",p)   #output: 8.85904700 * 10^-8

#Seeing the data of T and P value we conclude: Reject the Null Hypothesis
