import numpy as np


class kMeans():
	'''
	1. set k centroids within the dataset (the data points are already on the plane)
	2. calculate distance bewteen the points with each centroid and color each one to that centroid
	3. Update the centroid of each contempory cluster
	4. iterate the step 1, 2, 3, to make the assignment of cluster stable
	
	'''
	def __init__(self, k = 3):
	'''
	k: topic number
	
	'''
		self.k = k
		self.clusterMatrix = []
	
	def __distEclud(vecA, vecB):
		'''
		sqr((a1-b1)^2 + (a2-b2)^2 +.... )
		
		'''
		return sqrt(sum(power(vecA - vecB, 2)))
	
	def __randCent(self, dataset, k):
		'''
		creates a set of k random centroids for a given dataset. 
		In order to within the boundary, the min and max value are needed to 
		dataset: array with index as case and column as feature
		k topic numbers
		'''
		n_feature = shape(dataset)[1]
		centroids = mat(zeros((k, n_feature))
		for j in n_feature:
		
			# get min of each column
			minj = min(dataset[:, j])
			rangej = float(max(dataset[:, j]) - minj)
			centroids[:,j] = minJ + rangeJ * random.rand(k,1)
		return centroids
		
	def kmean(self, dataset):
		n_case = shape(dataset)[0] 
		
		# create a 2d array: | sample | nearest centroid | distance^2 |
		clusterAssessment = mat(zeros((n_case,2)))
		
		# initiate the centroid of the cluster
		centroids = self.__randCent(dataSet, self.k)
		
		# set a cluster change state
		clusterChanged = True
		while clusterChanged:
			clusterChanged = False
				for sample in range(n_case):
					# set the minimum distance and index of such distance, as the centroid 
					minDist = inf; minIndex = -1
					for cent_point in range(self.k):
					
					# Calculate the distance between each sample with each centroid
						distance = self.__distEclud(centroids[cent_point,:],dataSet[sample,:])
						if distance < minDist: 
							minDist = distance
							minIndex = cent_point
							
						# Update the clusterAsse with the most recent min value and its centroid matrix index
						if clusterAsse[0, 1] != minIndex:
							clusterAssment[i,:] = minIndex, minDist**2
							
							# set the status as true, because if still clusterAsse[0, 1] != minIndex, it indicates the algorithm is not converged. 
							clusterChanged = True
				
				# Update centroid after each iteration
				for centroid in range(self.k):
					# Get the all datapoints within each tempory cluster and find new centroid
					centroids[cent,:] = np.mean(dataset[nonzero(clusterAsse[:, 0] == centroid)[0]], axis = 0)
		return centroids, clusterAssessment
		
		
		
		
		
		