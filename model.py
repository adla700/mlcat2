import pandas as pd
data = pd.read_excel('ice cream.xlsx')

x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.linear_model import LinearRegression
regression = LinearRegression()

regression.fit(x,y)

print(regression.predict([[101,2]]))

import pickle

pickle.dump(regression,open('model.pkl','wb'))










