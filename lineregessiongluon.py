#encoding=utf-8

import mxnet.ndarray as nd
import mxnet.autograd as autograd
import matplotlib.pyplot as plt
import random

from mxnet import gluon

num_inputs = 2
num_examples = 1000

true_w = [2,-5]
true_b = 4

X = nd.random_normal(shape=(num_examples,num_inputs))
y = true_w[0] * X[:, 0] + true_w[1] * X[:, 1] + true_b
y += .01 * nd.random_normal(shape=y.shape)

# plt.scatter(X[:, 1].asnumpy(),y.asnumpy())
# plt.show()

# batch_size = 10
# def data_iter():
#     # 产生一个随机索引
#     idx = list(range(num_examples))
#     random.shuffle(idx)
#     for i in range(0, num_examples, batch_size):
#         j = nd.array(idx[i:min(i+batch_size,num_examples)])
#         yield nd.take(X, j), nd.take(y, j)
#
#
# for data, label in data_iter():
#     print(data, label)
#     break

batch_size = 10
dataset = gluon.data.ArrayDataset(X, y)
data_iter = gluon.data.DataLoader(dataset, batch_size, shuffle=True)

net = gluon.nn.Sequential()
net.add(gluon.nn.Dense(1))

net.initialize()

square_loss = gluon.loss.L2Loss()

trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.1})


# w = nd.random_normal(shape=(num_inputs, 1))
# b = nd.zeros((1,))
# params = [w, b]
#
# for param in params:
#     param.attach_grad()
#
# def net(X):
#     return nd.dot(X, w) + b
#
#
# def square_loss(yhat, y):
#     # 注意这里我们把y变形成yhat的形状来避免矩阵形状的自动转换
#     return (yhat - y.reshape(yhat.shape)) ** 2
#
# def SGD(params, lr):
#     for param in params:
#         param[:] = param - lr * param.grad
#
#
# 模型函数
def real_fn(X):
    return 2 * X[:, 0] - 5 * X[:, 1] + 4


# 绘制损失随训练次数降低的折线图，以及预测值和真实值的散点图
def plot(losses, X, sample_size=100):
    xs = list(range(len(losses)))
    f, (fg1, fg2) = plt.subplots(1, 2)
    fg1.set_title('Loss during training')
    fg1.plot(xs, losses, '-r')
    fg2.set_title('Estimated vs real function')
    fg2.plot(X[:sample_size, 1].asnumpy(),
             net(X[:sample_size, :]).asnumpy(), 'or', label='Estimated')
    fg2.plot(X[:sample_size, 1].asnumpy(),
             real_fn(X[:sample_size, :]).asnumpy(), '*g', label='Real')
    fg2.legend()
    plt.show()

epochs = 5
learning_rate = .001
niter = 0
losses = []
moving_loss = 0
smoothing_constant = .01

# 训练
for e in range(epochs):
    total_loss = 0

    for data, label in data_iter:
        with autograd.record():
            output = net(data)
            loss = square_loss(output, label)
        loss.backward()
        # SGD(params, learning_rate)
        trainer.step(batch_size)
        total_loss += nd.sum(loss).asscalar()

        # 记录每读取一个数据点后，损失的移动平均值的变化；
        niter +=1
        curr_loss = nd.mean(loss).asscalar()
        moving_loss = (1 - smoothing_constant) * moving_loss + (smoothing_constant) * curr_loss

        # correct the bias from the moving averages
        est_loss = moving_loss/(1-(1-smoothing_constant)**niter)

        if (niter + 1) % 100 == 0:
            losses.append(est_loss)
            print("Epoch %s, batch %s. Moving avg of loss: %s. Average loss: %f" % (e, niter, est_loss, total_loss/num_examples))
            plot(losses, X)