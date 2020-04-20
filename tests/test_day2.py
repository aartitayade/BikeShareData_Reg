import pytest
from day2 import predict_atemp, predict_hum, predict_windspeed


def test_predict_atemp():
	assert predict_atemp(0.150888)==1407
	assert predict_atemp(0.229270)==1904
	
def test_predict_hum():
	assert predict_hum(0.482917)== 3405
	assert predict_hum(0.805833)==3410
	
def test_predict_windspeed():
	assert predict_windspeed(0.160446)==3561
	assert predict_windspeed(0.36195)==2559
	