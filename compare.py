import numpy as np
import math

def stdev(arr):
	meanx = np.mean(arr)
	shp0 = len(arr)
	totsum = 0
	for el in arr:
		ant = (el-meanx)*(el-meanx)	
		totsum+=ant
	return math.sqrt(totsum/shp0)

def compare_arrays(brr,crr):
	shp=brr.shape
	diffcount = 0
	totsum = 0
	holex = []
	for j in range(shp[0]):
		for k in range(shp[1]):
			if brr[j][k]!=crr[j][k]:
				holex.append(brr[j][k])
				diffr = brr[j][k]-crr[j][k]			#difference
				diff2 = diffr*diffr 				#squared difference
				diffcount = diffcount+1
				totsum = totsum + diff2
	mean_error = totsum/float(diffcount)
	rmse = math.sqrt(mean_error)
	standev = stdev(holex)
	nrmse1 = rmse/standev
	return nrmse1,diffcount	

arr1 = np.loadtxt('original.txt')
arr2 = np.loadtxt('output.txt')

x,y= compare_arrays(arr1,arr2)
print 'NRMSE=',x