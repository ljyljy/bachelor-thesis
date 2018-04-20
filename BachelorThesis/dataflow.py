from numpy import *
from random import random, shuffle
from sklearn.model_selection import KFold
from features import *
from epoch import *
from gru import *
import filesystem as fs

"""
WRITTEN BY:
Nicklas Hansen
"""

def flow_all(force=False):
	log, clock = Log('Features', echo=True), stopwatch()
	files,_ = fs.getAllSubjectFilenames(preprocessed=True)
	log.print('Total files:  {0}'.format(len(files)))
	log.print('-'*35)
	clock.round()
	epochs = []
	for i, filename in enumerate(files):
		try:
			X,y = fs.load_csv(filename)
			X,y,mask = make_features(X, y)
			epochs.extend(get_epochs(X, y, mask))
			log.print('{0}/{1} files appended'.format(i, len(files)))
		except Exception as e:
			log.print('{0} Exception: {1}'.format(filename, str(e)))
	log.print('Initiating dataflow...')
	dataflow(epochs)
	log.print('Successfully completed full dataflow.')

def dataflow(epochs):
	#X,y = fs.load_csv(filename)
	#X,y,mask = make_features(X, y)
	#epochs = get_epochs(X, y, mask)
	print('Generated a total of {0} epochs'.format(len(epochs)))
	data = dataset(epochs)
	train,test = data.holdout(0.85)
	print('train:', len(train), ' test:', len(test))
	n_cells = epochs[0].timesteps
	model = gru(data, n_cells)
	print('Fitting...')
	model.fit(train, 32)
	print('Evaluating...')
	score = model.evaluate(test)
	print(score)
	#print(metrics.compute_score(score, metrics.TPR_FNR).items())

class dataset:
	def __init__(self, epochs, shuffle=True):
		self.epochs = epochs
		self.size = len(epochs)
		self.timesteps = epochs[0].timesteps
		self.features = epochs[0].features
		if shuffle:
			self.shuffle_epochs()

	def shuffle_epochs(self):
		shuffle(self.epochs)

	def holdout(self, split = 0.67):
		cut = int(self.size * split)
		return self.epochs[:cut], self.epochs[cut:]

	def kfold(self, folds = 10):
		kf = KFold(folds)
		train, test = [], []
		for train_index, test_index in kf.split(self.epochs):
			train.append(self.epochs[train_index[0]:train_index[len(train_index)-1]])
			test.append(self.epochs[test_index[0]:test_index[len(test_index)-1]])
		return train, test

	#def kfold(self, folds = 5):
	#	kf = KFold(folds)
	#	trainX, trainY, testX, testY = [],[],[],[]
	#	for train_index, test_index in kf.split(self.X):
	#		trainX.append(self.X[train_index[0]:train_index[len(train_index)-1]])
	#		trainY.append(self.y[train_index[0]:train_index[len(train_index)-1]])
	#		testX.append(self.X[test_index[0]:test_index[len(test_index)-1]])
	#		testY.append(self.y[test_index[0]:test_index[len(test_index)-1]])
	#	return trainX, trainY, testX, testY