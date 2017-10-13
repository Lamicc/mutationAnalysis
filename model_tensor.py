#python 2.7/3
import tensorflow as tf
import numpy as np
import pandas as pd

try :
    df = pd.read_csv("./dataset.csv")
except IOError:
    print("File not found!")

## seperate unlabelled data
ulab_df = df[df.Label <0]
df = df.drop(ulab_df.index)

## balance testing data
tmp1 = df.loc[df['Label'] == 1]
tmp1 = tmp1.sample(10)
tmp0 = df.loc[df['Label'] == 0]
tmp0 = tmp0.sample(10)
test_df = pd.concat([tmp1,tmp0])

## balance trainig data
train_df = df.drop(test_df.index)
rdrm = train_df.loc[train_df['Label']==1].sample(200)
train_df = train_df.drop(rdrm.index)

## extract features and target
training_x = train_df[['x','y','z']]
training_x = training_x.as_matrix()
training_y = train_df.Label
training_y = training_y.as_matrix()

testing_x = test_df[['x','y','z']]
testing_x = testing_x.as_matrix()
testing_y = test_df.Label
testing_y = testing_y.as_matrix()

## build DNN classifier
feature_columns = [tf.feature_column.numeric_column("x", shape=[3])]
classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                        hidden_units=[10, 20, 20, 10],
                                        n_classes=2,
                                        model_dir="../model")

## train with labelled set
train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": training_x},
      y= training_y,
      num_epochs=None,
      shuffle=True)

classifier.train(input_fn=train_input_fn, steps=2000)

## evaluate accuracy
test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": testing_x},
      y= testing_y,
      num_epochs=1,
      shuffle=False)
accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]
print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

## predict unlabelled data
ul = ulab_df[['x','y','z']]
new_samples = ul.as_matrix()
predict_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": new_samples},
      num_epochs=1,
      shuffle=False)
predictions = list(classifier.predict(input_fn=predict_input_fn))
predicted_classes = np.asarray([p["classes"] for p in predictions]).flatten().astype(int)

## build new training set
new_train_x = np.concatenate((training_x, new_samples), axis=0)
new_train_y = np.concatenate((training_y, predicted_classes), axis=0)

## train with labelled data + predicted data
train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": new_train_x},
      y= new_train_y,
      num_epochs=None,
      shuffle=True)
classifier.train(input_fn=train_input_fn, steps=4000)

## new accuracy score
test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": testing_x},
      y= testing_y,
      num_epochs=1,
      shuffle=False)
accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]
print("\nNew Test Accuracy: {0:f}\n".format(accuracy_score))
