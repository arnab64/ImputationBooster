import knn
import time
import math
import random
import getstuff
import numpy as np
from scipy import stats
from time import gmtime, strftime
from sklearn.cluster.bicluster import SpectralBiclustering

#------------------------------------------------------------------------------

class spectral:
	def __init__(self,list1,list2):
		intermediate = arr1[list1,:]
	    	self.data = intermediate[:,list2]
	    	self.listx = list1
	    	self.listy = list2

	def fit_data_to_model(self,shapey):
		model = SpectralBiclustering(n_clusters=shapey, method='log',random_state=0)
		model.fit(self.data)
		self.fit_data = self.data[np.argsort(model.row_labels_)]
		self.fit_data = self.fit_data[:, np.argsort(model.column_labels_)]
		self.rowl = model.row_labels_
		self.coll = model.column_labels_
		self.shapex = shapey

	def find_average_spearman_one(self):
		rho1, pval1 = stats.spearmanr(self.array1,axis=0)
		rho2, pval2 = stats.spearmanr(self.array1,axis=1)
		sum1 = 0
		for a in range(self.array1.shape[0]):
			for b in range(self.array1.shape[0]):
				if b>a:
					#print a,b, rho2[a][b]
					gg1 = rho2[a][b]
					sum1+= gg1
		div1 = self.array1.shape[0]*(self.array1.shape[0]-1)
		fac1 = sum1/float(div1)
		sum2 = 0
		for c in range(self.array1.shape[1]):
			for d in range(self.array1.shape[1]):
				if d>c:
					#print c,d, rho1[c][d]
					gg2 = rho1[c][d]
					sum2+= gg2
		div2 = self.array1.shape[1]*(self.array1.shape[1]-1)
		fac2 = sum2/float(div2)
		lista = [fac1,fac2]
		return 2*max(lista)

	def find_average_spearman_two(self):
		rho1, pval1 = stats.spearmanr(self.array2,axis=0)
		rho2, pval2 = stats.spearmanr(self.array2,axis=1)
		sum1 = 0
		for a in range(self.array2.shape[0]):
			for b in range(self.array2.shape[0]):
				if b>a:
					#print a,b, rho2[a][b]
					gg1 = rho2[a][b]
					sum1+= gg1
		div1 = self.array2.shape[0]*(self.array2.shape[0]-1)
		fac1 = sum1/float(div1)
		sum2 = 0
		for c in range(self.array2.shape[1]):
			for d in range(self.array2.shape[1]):
				if d>c:
					#print c,d, rho1[c][d]
					gg2 = rho1[c][d]
					sum2+= gg2
		div2 = self.array2.shape[1]*(self.array2.shape[1]-1)
		fac2 = sum2/float(div2)
		lista = [fac1,fac2]
		return 2*max(lista)		

	def segment(self):
		ones = []
		zeros = []
		zeroz1 = []
		onez1 = []
		if self.shapex==(1,2):
			for k in range(len(self.coll)):
				if self.coll[k]==1:
					ones.append(k)
				else:
					zeros.append(k)
			self.array1 = self.data[:,zeros]
			self.array2 = self.data[:,ones]
			for h in range(len(zeros)):
				zeroz1.append(self.listy[zeros[h]])				#idhar mein kuch lafda hai
			for p in range(len(ones)):
				onez1.append(self.listy[ones[p]])
	
		elif self.shapex==(2,1):
			for k in range(len(self.rowl)):
				if self.rowl[k]==1:
					ones.append(k)
				else:
					zeros.append(k)	
			self.array1 = self.data[zeros,:]
			self.array2 = self.data[ones,:]
			for h in range(len(zeros)):
				zeroz1.append(self.listx[zeros[h]])				#idhar mein kuch lafda hai
			for p in range(len(ones)):
				onez1.append(self.listx[ones[p]])
		else:
			print "invalid shape!"
		return zeroz1, onez1

#---------------------------------------------------------------------------------		

class knn_impute:
	def __init__(self,lista,listb):
		inter = arr1[lista,:]	
		self.arr = inter[:,listb]
		self.shp1 = self.arr.shape[0]
		self.shp2 = self.arr.shape[1]
		self.xindexes = lista
		self.yindexes = listb
		self.missingx = []
		self.real_missingx = []
		decoy = misspositions[lista,:]
		self.mix1 = decoy[:,listb]

	def get_missing(self):
		self.misslist = []	
		real_misslist = []
		checked = 0
		missb = 0
		for j in range(len(self.xindexes)):
			for k in range(len(self.yindexes)):
				mstat = check_missing(self.xindexes[j],self.yindexes[k])
				checked+=1
				if mstat==1:
					missb+=1
					self.missingx.append(tuple([j,k]))	
					self.real_missingx.append(tuple([self.xindexes[j],self.yindexes[k]]))
		return checked,missb

	def impute_this(self):
		kobj = knn.knn_impute(self.arr,self.mix1)
		self.predicted = kobj.predict_all()

	def return_predicted(self):
		real_predicted = []
		for j in range(len(self.missingx)):
			house1 = self.missingx[j]
			car1 = self.real_missingx[j]
			aa = car1[0]
			ab = car1[1]
			pr = self.predicted[house1[0]][house1[1]]
			real_predicted.append(tuple([aa,ab,pr]))
		return real_predicted

#----------------------------------------------------------------------------

def find_average_spearman(listu,listv):
	inter = arr1[listu,:]	
	nowarr = inter[:,listv]
	rho1, pval1 = stats.spearmanr(nowarr,axis=0)
	rho2, pval2 = stats.spearmanr(nowarr,axis=1)
	sum1 = 0
	for a in range(nowarr.shape[0]):
		for b in range(nowarr.shape[0]):
			if b>a:
				gg1 = rho2[a][b]
				sum1+= gg1
	div1 = nowarr.shape[0]*(nowarr.shape[0]-1)
	fac1 = sum1/float(div1)
	sum2 = 0
	for c in range(nowarr.shape[1]):
		for d in range(nowarr.shape[1]):
			if d>c:
				gg2 = rho1[c][d]
				sum2+= gg2
	div2 = nowarr.shape[1]*(nowarr.shape[1]-1)
	fac2 = sum2/float(div2)
	lista = [fac1,fac2]
	return 2*max(lista)

def find_spearman2(nowarr):
	rho1, pval1 = stats.spearmanr(nowarr,axis=0)
	rho2, pval2 = stats.spearmanr(nowarr,axis=1)
	sum1 = 0
	for a in range(nowarr.shape[0]):
		for b in range(nowarr.shape[0]):
			if b>a:
				gg1 = rho2[a][b]
				sum1+= gg1
	div1 = nowarr.shape[0]*(nowarr.shape[0]-1)
	fac1 = sum1/float(div1)
	sum2 = 0
	for c in range(nowarr.shape[1]):
		for d in range(nowarr.shape[1]):
			if d>c:
				gg2 = rho1[c][d]
				sum2+= gg2
	div2 = nowarr.shape[1]*(nowarr.shape[1]-1)
	fac2 = sum2/float(div2)
	lista = [fac1,fac2]
	return 2*max(lista)
#-----------------------------------------------------------------------------------------------------------	

def recursive_biclust(lis1,lis2):
	megalist = []
	arrq = [lis1,lis2]
	
	if len(lis1)<minlen and len(lis2)<minlen:
		megalist.append(tuple(arrq))
		return megalist
	
	spec1 = spectral(lis1,lis2)					#initiating the matrix
	spec1.fit_data_to_model(this_shape1)		#specbi using shape1 (1,2)
	zero1,one1 = spec1.segment()

	if len(zero1)<minlen or len(one1)<minlen: 	
		spec2 = spectral(lis1,lis2)					#initiating the matrix
		spec2.fit_data_to_model(this_shape2)		#specbi using shape2
		zero2,one2 = spec2.segment()
		if len(zero2)<minlen or len(one2)<minlen:
			megalist.append(tuple(arrq))
			return megalist		
		scr21 = spec2.find_average_spearman_one()
		scr22 = spec2.find_average_spearman_two()
		totscr2 = scr21+scr22

		q3 = recursive_biclust(zero2,lis2)
		q4 = recursive_biclust(one2,lis2)
		megalist.extend(q3)
		megalist.extend(q4)
		return megalist
	else:
		scr11 = spec1.find_average_spearman_one()
		scr12 = spec1.find_average_spearman_two()
		totscr1 = scr11+scr12

		spec2 = spectral(lis1,lis2)					#initiating the matrix
		spec2.fit_data_to_model(this_shape2)		#specbi using shape2
		zero2,one2 = spec2.segment()
		if len(zero2)<minlen or len(one2)<minlen:
			megalist.append(tuple(arrq))
			return megalist		
		scr21 = spec2.find_average_spearman_one()
		scr22 = spec2.find_average_spearman_two()
		totscr2 = scr21+scr22

		if totscr1<0.05 and totscr2<0.05:
			megalist.append(tuple(arrq))
			return megalist	
		else:
			if totscr1>totscr2:
				q1 = recursive_biclust(lis1,zero1)
				q2 = recursive_biclust(lis1,one1)
				megalist.extend(q1)
				megalist.extend(q2)
				return megalist
			else:
				q3 = recursive_biclust(zero2,lis2)
				q4 = recursive_biclust(one2,lis2)
				megalist.extend(q3)
				megalist.extend(q4)
				return megalist

#--------------------------------------------------------------------------------------------------			

def check_missing(a,b):
	return misspositions[a][b]

def assign_missing():
	for k in range(missindexes.shape[0]):
		a = int(missindexes[k][0])
		b = int(missindexes[k][1])
		misspositions[a][b] = 1

def replace_missing_with_mean(arr11):
	new_data = np.copy(arr11)						#replace missing values with zero.
	arr = np.nanmean(new_data,axis=0)
	for k in range(missindexes.shape[0]):		#modify code to replace missing value with mean.
		ax = int(missindexes[k][0])
		ay = int(missindexes[k][1])
		new_data[ax][ay]=arr[ay]
	#arr1 = np.copy(new_data)                                 
	return new_data

def get_change(brr,crr):
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
	return rmse

def write_back(finx,fname):
	shap = finx.shape
	ofile = open(fname,'w')
	for j in range(shap[0]):
		for k in range(shap[1]):
			ofile.write(str(finx[j][k])+" ")
		ofile.write("\n")
	ofile.close()

def getmissindices(arr):
	listlol = []
	for x in range(arr.shape[0]):
		for y in range(arr.shape[1]):
			if np.isnan(arr[x][y])==True:
				listlol.append([x,y])
	return np.array(listlol)


#--------------------------------------------------------------------------------	

if __name__ == "__main__":

	infile = 'input_w_missing.txt'
	outfile = 'output.txt'

	starttime = time.time()
	print 'started at:', starttime
	
	nan_array = np.loadtxt(infile)
	missindexes = getmissindices(nan_array)

	arr1 = replace_missing_with_mean(nan_array)
	
	misspositions = np.zeros((nan_array.shape[0],nan_array.shape[1]))
	assign_missing()

	listx = []
	listy = []
	for j in range(nan_array.shape[0]):
		listx.append(j)
	for jj in range(nan_array.shape[1]):
		listy.append(jj)

	shapes = [(1,2),(2,1)] 
	this_shape1 = shapes[0]
	this_shape2 = shapes[1]

	minlen = getstuff.getminlen()
	orig = find_average_spearman(listx,listy)
	print "original spearman = ", orig

	print 'Recursive Spectral Bicluster based Weighted Knn Imputation (RSKI)'
	arraytocalc = []
	prevspr = 10000
	thresx = getstuff.get_thres()

	for itr in range(getstuff.getiters()):										#iterations
		hello = recursive_biclust(listx,listy)					#returns all the biclusters
		scores = []
		totchecked = 0
		totmiss = 0
		all_predicted = []
		print "iteration no.",itr+1
		print "\n",len(hello),"biclusters formed!"

		for kf in hello:							
			scrr = find_average_spearman(kf[0],kf[1])			#find the average spearman rho of all the biclusters formed
			print "\n",len(kf[0]),len(kf[1]),scrr
			scores.append(scrr)
			impu = knn_impute(kf[0],kf[1])
			pp,qq=impu.get_missing()
			impu.impute_this()
			prednow = impu.return_predicted()
			all_predicted.extend(prednow)
			totchecked+=pp
			totmiss+=qq
		avgspr = np.mean(scores)
		duplicate = np.copy(arr1)
		for j in range(len(all_predicted)):
			thispr = all_predicted[j]
			if getstuff.getreplace()==1:
				prev_val = arr1[thispr[0]][thispr[1]]
				duplicate[thispr[0]][thispr[1]] = (thispr[2]+prev_val*itr)/float(itr+1)
			else:
				duplicate[thispr[0]][thispr[1]] = thispr[2]	
		change = get_change(arr1,duplicate)
		real_asr = find_spearman2(duplicate)
		print "Real_asr, change : ", real_asr, change

		if abs(real_asr-prevspr)<thresx:
			break;
		prevspr = real_asr
		arr1 = np.copy(duplicate)
	write_back(duplicate, outfile)
