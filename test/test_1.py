import answers_lab
import pytest


def approximately_equal(a, b, tolerance=0.05):
	return abs(a - b) < tolerance

def sample_function(x):
        return x**2 + 2*x + 1
#find_min_mc(n, xl, xr, f):


def test_find_min_mc():
	output = answers_lab.find_min_mc(500, -10, 10, sample_function)
	xmin = output[0]
	ymin = output[1]
	#print(xmin)
	#print(ymin)
	assert approximately_equal(xmin, -1.0)
	assert approximately_equal(ymin, 0.0)



#test_find_min_mc()
