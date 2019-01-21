#模块化神经网络
#forward.py
#定义前向传播、参数w和偏置项b

def forward(x,regularizer):
    w=
    b=
    y=
    return y

def get_weight(shape,regularizer):
    w=tf.Variable()
    tf.add_to_collection('losses',tf.contrib.l2_regularizer(regularizer)(w))
    return w
    
def get_bias(shape):#shape为b的个数
    b=tf.Variable()
    return b
