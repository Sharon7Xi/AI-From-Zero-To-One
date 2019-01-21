#训练网络，优化网络参数
def backwarf():
    x=tf.placeholder()
    y_=tf.placeholder()
    y=forward.forward(x,REGULARIZER)
    global_step=tf.Variable(0,trainable=False)
    loss=
    
    #loss是y与y_的差距
    #如果用均方差
    loss_mse=tf.reduce_mean(tf.square(y-y_))
    #如果用交叉熵
    ce=tf.nn.sparse_softmax_cross_entropy_witf_logits(logits=y,labels=tf.argmax(y_,1))
    loss_cem=tf.reduce_mean(ce)
    
    #加入正则化
    loss=loss_mse + loss_cem + tf.add_n(tf.get_collection('losses'))
    
    #使用指数衰减学习率
    learning_rate  = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        数据集总样本数/BATCH_SIZE，
        LEARNING_RATE_DECAY，
        staircase=True）
        
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)
    
    #滑动平均
    ema=tf.train.ExponentiaMovingAverage(MOVING_AVERAGE_DECAY,global_step)
    ema_op = ema.apply(tf.trainable_variables())
    with tf.control_dependencies([train_step,ema_op]):
        train_op = tf.no_op(name='train')
    
    #执行会话
    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run()
        
        for i in range(STEPS):
            sess.run(train_step,feed_dict={x: ,y_: })
            if i% 轮数 ==0：
                print
                
if__name__=='__main__':
    backward()
    
