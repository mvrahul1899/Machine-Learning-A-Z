# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:30:00 2018

@author: RAHUL
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:30:40 2018

@author: RAHUL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

"""from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)"""

"""from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)""" 

#fitting the decision tree regressin to the dataset

#create your regressor here

#predicting a new result
y_pred=regressor.predict(6.5)


#visualising the decision tree regression results
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title('truth or bluff(decision tree regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()


#regression with highter resolusion i.e. considering all points
x_grid=np.arange(min(x),max(x),0.1)
x_grid=x_grid.reshape((len(x_grid),1))

plt.scatter(x,y,color='red')
plt.plot(x_grid,regressor.predict(regressor),color='blue')
plt.title('truth or bluff(polynomial regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()