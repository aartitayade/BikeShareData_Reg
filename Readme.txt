==================
BikeShareData_Reg
==================

This projest predicts the rental bike sharing counts on the basis of different environmental and weather situations such as
temperature, humidity and windspeed etc.

=========
Overview
=========

Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
publicly available in http://capitalbikeshare.com/system-data.

The dataset is taken from the publicly available in http://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset

=============
Prerequisite
=============

make sure you have following prerequisites

python_requires= python >=3.6

following is the list of libraries ,need to install for this project.
1. pandas
2. sklearn
3. matplotlib
4. numpy

test_requires= pytest

STRAT --> cmd / shell

$pip install pandas
$pip install -U scikit-learn
$pip install matplotlib
$pip install numpy

$pip install pytest

Donwload data from http://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset

save day.csv under /src/ folder

======
To Do
======
1. Import the libraries: first import all the libraries and module that we are going to use in this project.
2. Load the data: load the dataset using pandas from csv

3. Summarize the data: here also we use pandas to explore the data with descriptive statistics and visualization.

4. Build model: we are using sklerarns LinearRegression technique for preparing the model. for training the model we need to split 
   our data into training set accompanied by the label.we can build different models and estimate its accuracy score. 
   we have created three models for predicting the rental bike sharing count for different temperature, humidity and windspeed.

5. Make Predictions: once the model is fit on training data, we can make prediction on dataset. 

=============
Steps To Run 
=============
To run the python script follow the steps below.
 
1. open Terminal or command prompt
2. go to the directory where your code resides(our code resides in /src/)
   cd src
3. type python
4. here we want to import the function from python script(function- predict_atemp from python script- day1.py)
   type from day1.py import predict_atemp
5  then pass in the value of atemp for which you want the predict count of  the rental sharing bike
   predict_atemp(0.229270)
6  similarly we can make the predict count of  the rental sharing bike for different values of humadity and windspeed
   by importing the function predict_hum and predict_windspeed 

 
----------------------------------------------------------------------------------------------
$ Start --> CMD
$cd  src
$python 
>> from day import predict_atemp
>> predict_atemp(0.150888)
>> from day import predict_hum
>> predict_hum(0.482917)
>> form day import predict_windspeed
>> predict_windspeed(0.160446)
----------------------------------------------------------------------------------------------


 



