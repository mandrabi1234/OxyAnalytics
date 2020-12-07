'''
    RANDOM FOREST CLASSIFIER
'''

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import time
class Models():
    def rfClassifier(train_features, train_labels, test_features, test_labels):
        # Set a timer to check execution length

        start_time = time.clock()

        #   1. Create a Gaussian Classifier
        clf = RandomForestClassifier(n_estimators=1000)

    #   2. Train the model
        clf.fit(train_features, train_labels.values.ravel())
        labels_pred = clf.predict(test_features)
        print( "Classifier Predictions:")
        print(labels_pred)
        print(labels_pred.shape)
        print("RandomForestClassifier execution time:", time.clock() - start_time, "seconds")

    # 3. Check Accuracy using actual and predicted values

    # Model Accuracy, how often is the classifier correct?

        print("Accuracy:", metrics.accuracy_score(test_labels, labels_pred))
