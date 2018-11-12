#encoding=utf-8
#author:Ethan
#software:Pycharm
#file:tf_test.py
#time:2018/11/8 下午7:56
import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a,b)
with tf.Session() as sess:
	#add this line to use tensorboard
	writer = tf.summary.FileWriter('./graphs',sess.graph)
	print(sess.run(x))
	writer.close()
