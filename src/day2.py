import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model

#create the regressionline function that will plot the regression line
def regressionline(model,datatest,labeltest,title):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(datatest,labeltest,c='b',alpha=0.5)
	ax.plot(datatest,model.predict(datatest),c ='r', alpha=0.7)
	score = model.score(datatest,labeltest)
	title += " score(R2) :"+str(score)
	ax.set_title(title)
	
	
	plt.show()
	

#load the csv dataset into a varible dataset

dataset = pd.read_csv('day.csv', index_col=0)

	
print(dataset.head(10))
print(dataset.describe())
#print(dataset.dtypes)

dataset.dteday= pd.to_datetime(dataset.dteday)

#print(dataset.dtypes)
#print(dataset.isna().sum())
#print(dataset.corr())
#exit()

#dataset1 = pd.concat([dataset.atemp,dataset.hum,],axis= 1)
#print(dataset1.head())
#dataset1.plot.hist(alpha=0.5)
#plt.show()
#exit()
	
	
def predict_atemp(p_atemp):

	if p_atemp > 0.840896 or p_atemp < 0.079070:
		raise ValueError('atemp should be the value between 0.84 and 0.079')
	
	#prepare the training data with corresponding labels for modeling the data
	
	dataset_train=dataset.atemp[dataset.dteday < '2011-12-31']
	dataset_train = dataset_train.to_frame()
	label_train=dataset.cnt[dataset.dteday < '2011-12-31']
	#print(type(dataset_train))
	#exit()
	
	#create the linear regression model and save into the variable model and fit the traing data into it and pass it
	#to the regressionline
	model = linear_model.LinearRegression()
	model.fit(dataset_train,label_train)
	regressionline(model,dataset_train,label_train,"count for temperature(atemp)")
	
	#test_atemp=0.229270
	test_atemp=p_atemp
	predict_cnt= model.predict([[test_atemp]])[0]
	
	print("count(atemp), R2: ",model.score(dataset_train,label_train))
	print("for atemp {0} predicted count is {1}".format(test_atemp,int(predict_cnt)))
	return int(predict_cnt )
	
	#if you want predict count for the value within the dataset,you have the actual count as well then you can uncomment the line here
	
	#actual_cnt=1600
	#print("for atemp {0} actual count is {1}".format(test_atemp,actual_cnt))

def predict_hum(p_hum):
	
	#prepare the training data with corresponding labels for modeling the data
	
	dataset_train=dataset.hum[dataset.dteday < '2011-12-31']
	dataset_train = dataset_train.to_frame()
	label_train=dataset.cnt[dataset.dteday < '2011-12-31']
	#print(type(dataset_train))
	#exit()
	
	#create the linear regression model and save into the variable model and fit the traing data into it and pass it
	#to the regressionline
	model = linear_model.LinearRegression()
	model.fit(dataset_train,label_train)
	regressionline(model,dataset_train,label_train,"count for temperature(hum)")
	
	#test_atemp=0.229270
	test_hum=p_hum
	predict_cnt= model.predict([[test_hum]])[0]
	
	print("count(hum), R2: ",model.score(dataset_train,label_train))
	print("for hum {0} predicted count is {1}".format(test_hum,int(predict_cnt)))
	return int(predict_cnt) 
	
	
 	
def predict_windspeed(p_windspeed):

	
	dataset_train=dataset.windspeed[dataset.dteday < '2011-12-31']
	dataset_train = dataset_train.to_frame()
	label_train=dataset.cnt[dataset.dteday < '2011-12-31']
	
	model = linear_model.LinearRegression()
	model.fit(dataset_train,label_train)
	regressionline(model,dataset_train,label_train,"count for windspeed")
	
	test_windspeed=p_windspeed
	#actual_cnt=1600
	predict_cnt= model.predict([[test_windspeed]])[0]
	
	print("count(windspeed), R2: ",model.score(dataset_train,label_train))
	print("for windspeed {0} predicted count is {1}".format(test_windspeed,int(predict_cnt)))
	#print("for windspeed {0} actual count is {1}".format(test_windspeed,actual_cnt))
	return int(predict_cnt)