#KNNimpute

import numpy as np
import math
import sys

class knn_impute:
	def __init__(self,dat,mdata):
	   	self.arr = dat
	   	self.shp = self.arr.shape
		self.shp1 = self.shp[0]
		self.shp2 = self.shp[1]
		self.distlist = np.zeros((self.shp1,self.shp1))
		self.missposs = np.copy(mdata)

	def get_missrow(self,n1):
		lisy = []
		for h in range(self.shp2):
			if self.check_missing(n1,h) == 1:
				lisy.append(h)
		return lisy

	def check_missing(self,a,b):
		return self.missposs[a][b]

	def distance(self,n1,n2):
		if self.distlist[n1][n2]==0 and self.distlist[n2][n1]==0: 
			distt = 0
			cnt = 0
			for j in range(self.shp2):
				if np.isnan(self.arr[n1][j]) or np.isnan(self.arr[n2][j]):
					continue;
				else:
					cnt+=1
					diff = self.arr[n1][j]-self.arr[n2][j]
					diff2 = diff*diff
					distt+=diff2			
			try:
				distt2 = math.sqrt(distt/cnt)
			except ZeroDivisionError:
				distt2 = 10000
			self.distlist[n1][n2] = distt2
			self.distlist[n2][n1] = distt2	
			return distt2	
		else:
			return self.distlist[n1][n2]				#if distance is already computed before, then send it directly

	def distance2(self,n1,n2):
		#print 'find dist btn',n1,'-',n2
		if self.distlist[n1][n2]==0 and self.distlist[n2][n1]==0: 
			distt = 0
			cnt = 0
			for j in range(self.shp2):
				cnt+=1
				diff = self.arr[n1][j]-self.arr[n2][j]
				diff2 = diff*diff
				distt+=diff2			
			distt2 = math.sqrt(distt/cnt)
			self.distlist[n1][n2] = distt2
			self.distlist[n2][n1] = distt2	
			return distt2	
		else:
			return self.distlist[n1][n2]				#if distance is already computed before, then send it directly
		
	def predict_it(self,atts,listy):
		predx = []
		for tx in range(len(atts)):
			thisattr = atts[tx]
			pr = []
			for b in range(len(listy)):
				ox = listy[b]
				indx = ox[0]
				wts = ox[1]
				#if np.isnan(self.arr[indx][thisattr])!=True:			#if the attribute values for the list is not nan
				pr.append(self.arr[indx][thisattr]*wts)
			meanx = np.sum(pr)
			predx.append(meanx)
		return predx
		
	def distance2weights(self,brr):
		maxim = max(brr)+1
		for j in range(len(brr)):
			brr[j] = maxim-brr[j]
		sumim = sum(brr)
		for k in range(len(brr)):
			brr[k] = brr[k]/float(sumim) 				#except ZeroDivisionError:
		return brr

	def find_top(self,yy,n1):			#non_weighted
		listy = []
		for k in range(self.shp1):
			if k!=n1:
				distx = self.distance2(n1,k)
				listy.append(tuple([k,distx]))
		sorted_by_second = sorted(listy, key=lambda tup: tup[1])
		if len(sorted_by_second)>yy:						#here yy is the k, in top-k
			tempr = sorted_by_second[:yy]
		else:
			tempr = sorted_by_second					#selecting top 10 or top yy
		wtx = []
		for s in range(len(tempr)):
			u=tempr[s]
			wtx.append(u[1])
		holock = self.distance2weights(wtx)	
		yuya = []
		for r in range(len(tempr)):
			rr = tempr[r]
			yuya.append([rr[0],holock[r]])
		return yuya		

	def write_back(self,finx,fname):
		ofile = open(fname,'w')
		for j in range(self.shp1):
			for k in range(self.shp2):
				ofile.write(str(finx[j][k])+" ")
			ofile.write("\n")
		ofile.close()

	def check(self,brr):
		mism = 0
		for j in range(self.shp1):
			for k in range(self.shp2):
				if self.arr[j][k]!=brr[j][k]:
					mism+=1
		print "mismatched = ",mism

	def drawProgressBar(self,percent, barLen = 50):
	    sys.stdout.write("\r")
	    progress = ""
	    for i in range(barLen):
	        if i<int(barLen * percent):
	            progress += "="
	        else:
	            progress += " "
	    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
	    sys.stdout.flush()

	def predict_all(self):
		finale = np.copy(self.arr)
		predcount = 0
		for g in range(self.shp1):
			misx = self.get_missrow(g)			#returns the index of the missing values in row g 
			if len(misx)>0:
				hell = self.find_top(20,g)					#returns the 10 most similar instances
				predictedx = self.predict_it(misx,hell)
				for j in range(len(misx)):
					mnx = predictedx[j]			#calculates the mean 
					indt = misx[j]
					finale[g][indt]=mnx
				predcount+=len(predictedx)
				pc = g/float(self.shp1)
				self.drawProgressBar(pc)
		self.drawProgressBar(1)
		print '\n'
		return finale

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
	return new_data

def write_back(finx,fname):
	shp1 = finx.shape[0]
	shp2 = finx.shape[1]
	ofile = open(fname,'w')
	for j in range(shp1):
		for k in range(shp2):
			ofile.write(str(finx[j][k])+" ")
		ofile.write("\n")
	ofile.close()
