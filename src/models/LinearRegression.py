from sklearn import linear_model
from train_model import crossLinear
from train_model import x_train, y_train
lr = linear_model.LinearRegression()


model = crossLinear(lr, x_train, y_train, 'neg_root_mean_squared_error', 10)


