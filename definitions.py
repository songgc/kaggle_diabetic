import pprint

LABEL_FILE = 'data/trainLabels.csv'
PSEUDO_LABEL_FILE = 'data/testLabels.csv'
MEAN_FILE = 'data/mean.npy'

TRAIN_DIR = 'data/train_medium' 
#TRAIN_DIR = '/data/kaggle/diabetic/train_medium' #TODO remove
TEST_DIR = 'data/test_medium'

# cache files for neural net feature extraction
TRAIN_FEATURES = 'data/X_train.npy'
TEST_FEATURES = 'data/X_test.npy'
TRAIN_LABELS = 'data/y_train.npy'
TEST_LABELS = 'data/y_test.npy'
ESTIMATOR_FILENAME = 'estimator.pickle'
WEIGHTS = 'weights.pickle'
CACHE_DIR = 'data/cache.dat'
TRANSFORM_DIR = 'data/transform'
FEATURE_DIR = 'data/features'

# image dimensions
C = 3
W = 224
H = 224
N_TARGETS = 1
N_CLASSES = 5
REGRESSION = True

CUSTOM_SCORE_NAME = 'kappa'

RANDOM_STATE = 9

MAX_PIXEL_VALUE = 255
TEST_ITER = 1
MAX_ITER = 1000
PATIENCE = 40
BATCH_SIZE = 128
INITIAL_LEARNING_RATE = 0.005
DECAY_FACTOR = 0.1
INITIAL_MOMENTUM = 0.9
STD = [70.53946096, 51.71475228, 43.03428563]
MEAN = [108.64628601, 75.86886597, 54.34005737]
SUBMISSION = 'data/sub'
BALANCE_WEIGHT = 0.2
SIGMA_COLOR = 0.2

#LAMBDAS = np.array([0.9991837, 0.04023934, 0.00356841])
#EIGENVECS = np.array([[0.78414893, 0.5125351, 0.34988332],
#                      [0.55659384, -0.33153433, -0.76176667],
#                      [0.27443382, -0.79208136, 0.54524601]])

#CLASS_WEIGHTS = [1, 2.5, 1.8, 3.5, 4]
#CLASS_WEIGHTS = [1, 10, 3, 5, 5]
CLASS_WEIGHTS = [1.3609453700116234,  14.378223495702006, 6.637566137566138,
                 40.235967926689575, 49.612994350282484]

# number of class samples in training set
#CLASSES = [25810, 5292, 2443, 873, 708]
OCCURENCES = {0: 25810, 2: 5292, 1: 2443, 3: 873, 4: 708}

# print the config to the terminal
print("############################# CONFIG #################################")
pprint.pprint({k: v for k, v in locals().items() if k.isupper()})
print("######################################################################")
