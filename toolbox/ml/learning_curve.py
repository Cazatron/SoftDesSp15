""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
#print data.DESCR
num_trials = 10
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

scores = []
test_accuracies = []
num_trials = 500

for i in train_percentages:
	X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size = i/100.0)
	model = LogisticRegression(C = 10**-10)
	model.fit(X_train, y_train)
	for j in range(num_trials):
		scores.append(model.score(X_test, y_test))

	test_accuracies.append(sum(scores)/10)

fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()
