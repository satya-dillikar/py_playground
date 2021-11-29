import numpy as np
real_numbers = np.array([10, 11])

def softmax(real_numbers):
  return np.exp(real_numbers) / np.sum(np.exp(real_numbers))

print("softmax probabilities: ")
print(softmax(real_numbers))


#import numpy as np
import matplotlib.pyplot as plt

# Data is (height (in), weight(lbs))
num_samples = 100
cat_means = np.array([9.5, 9.0])
cat_cov = np.array([[5.0, 4.0],[4.0,10.0]])
cat_data = np.random.multivariate_normal(cat_means, cat_cov, size=(num_samples))

dog_means = np.array([26, 30])
dog_cov = np.array([[60, 30.0],[30.0, 60]])
dog_data = np.random.multivariate_normal(dog_means, dog_cov, size=(num_samples))

plt.scatter(cat_data[:,0], cat_data[:,1], c='b')
plt.scatter(dog_data[:,0], dog_data[:,1], c='r')
plt.title('cats and dogs')
plt.xlabel('height (inches)')
plt.ylabel('weight (lbs)')
plt.legend(['cat', 'dog'])
#plt.show()

print('size of cat_data: ', cat_data.shape)
print('size of dog_data: ', dog_data.shape)


# Fill in these lines
cat_train_data = ...
dog_train_data = ...
cat_test_data = ...
dog_test_data = ...

## Teacher Answers
cat_train_data = cat_data[:int(len(cat_data)*0.8),:]
dog_train_data = dog_data[:int(len(dog_data)*0.8),:]
cat_test_data = cat_data[int(len(cat_data)*0.8):,:]
dog_test_data = dog_data[int(len(dog_data)*0.8):,:]

print('cat_train_data size: ', cat_train_data.shape)
print('dog_train_data size: ', dog_train_data.shape)
print('cat_test_data size: ', cat_test_data.shape)
print('dog_test_data size: ', dog_test_data.shape)

# Fill in these lines
cat_train_labels = ...
dog_train_labels = ...
cat_test_labels = ...
dog_test_labels = ...

## Teacher Answers
cat_train_labels = np.zeros(len(cat_train_data))
dog_train_labels = np.ones(len(dog_train_data))
cat_test_labels = np.zeros(len(cat_test_data))
dog_test_labels = np.ones(len(dog_test_data))

print('cat_train_labels size: ', cat_train_labels.shape)
print('dog_train_labels size: ', dog_train_labels.shape)
print('cat_test_labels size: ', cat_test_labels.shape)
print('dog_test_labels size: ', dog_test_labels.shape)