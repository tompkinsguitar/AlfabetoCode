from alfabeto_data import dissertation_images as di
import numpy as np
import random
import tensorflow as tf
from sklearn.externals import joblib
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib import rnn

allbach = di.bach_continuo
allpal = di.palestrina_continuo
allalf = di.alfabeto_continuo
allzma = di.zma_continuo
allzmo = di.zmo_continuo
allzso = di.zso_continuo

#[zma, zmo, zso, pal, alf, bach]
#[secular, sacred]
def data_maker(list_of_corpora):
    all_corpus_chords = [x[0] for x in list_of_corpora]
    chord_dict = {}
    chord_index = 0
    allcorpus = []
    for song in all_corpus_chords:
        for chord in song:
            if chord not in chord_dict.values():
                chord_dict[chord_index] = chord
                chord_index += 1
    print('how many chords:', chord_index)
    def onehot_maker(cont_corpus, label_number_list):
        for keysig in range(len(cont_corpus[0])):
            onehot = np.zeros(chord_index)
            for x in cont_corpus[0][keysig]:
                for a, b in chord_dict.items():
                    if x == b:
                        # print("what's the problem?", x)
                        onehot[a] += 1
                # onehot[bass] += 1
            song_data = [onehot, np.array(label_number_list)]
        # song_data = [onehot, np.array([0, 1])]
            allcorpus.append(np.array(song_data))
    secular = [1, 0]
    sacred = [0, 1]
    # onehot_maker(allbach, [])
    onehot_maker(allpal, sacred)
    onehot_maker(allalf, secular)
    onehot_maker(allzma, sacred)
    onehot_maker(allzmo, sacred)
    onehot_maker(allzso, sacred)
    return allcorpus, chord_dict

secular_sacred = data_maker([allpal, allalf, allzma, allzmo, allzso])


# mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

def create_feature_sets_and_labels(data, test_size=.1):
    random.shuffle(data)
    testing_size = int(test_size*len(data))
    train_x = list(data[:,0][:-testing_size])
    train_y = list(data[:,1][:-testing_size])

    test_x = list(data[:,0][-testing_size:])
    test_y = list(data[:,1][-testing_size:])

    return train_x, train_y, test_x, test_y
# train_x, train_y, test_x, test_y = create_feature_sets_and_labels(np.array(secular_sacred))
# joblib.dump([train_x, train_y, test_x, test_y], 'pickles/RNNcorpus.pkl', compress=9)
# mycorpus = joblib.load('pickles/RNNcorpus.pkl')
#
# train_x, train_y, test_x, test_y = mycorpus
#
# hm_epochs = 3  #number of cycles
# n_classes = 2
# batch_size = 64
#
# chunk_size = 12
# n_chunks = 28
# rnn_size = 512
#
# x = tf.placeholder('float', [None, n_chunks, chunk_size])
# y = tf.placeholder('float')
#
# def recurrent_neural_network_model(x):
#     layer = {'weights':tf.Variable(tf.random_normal([rnn_size,n_classes])),
#              'biases':tf.Variable(tf.random_normal([n_classes]))}
#
#     x = tf.transpose(x, [1,0,2])
#     x = tf.reshape(x, [-1, chunk_size])
#     x = tf.split(0, n_chunks, x)
#
#     lstm_cell = rnn_cell.BasicLSTMCell(rnn_size,state_is_tuple=True)
#     outputs, states = rnn.rnn(lstm_cell, x, dtype=tf.float32)
#
#     output = tf.matmul(outputs[-1],layer['weights']) + layer['biases']
#
#     return output
#
# def train_neural_network(x):
#     prediction = recurrent_neural_network_model(x)
#     cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
#
#     #optimizer is learning rate but in this casde the default s fine
#     optimizer = tf.train.AdamOptimizer().minimize(cost)
#
#     with tf.Session() as sess:
#         sess.run(tf.global_variables_initializer())
#
#         for epoch in range(hm_epochs):
#             epoch_loss = 0
#             i=0
#             while i < len(train_x):
#                 start = i
#                 end = i+batch_size
#                 batch_x = np.array(train_x[start:end])
#                 batch_y = np.array(train_y[start:end])
#
#                 _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
#                                                               y: batch_y})
#                 epoch_loss += c
#                 i+=batch_size
#
#             print('Epoch', epoch+1, 'completed out of',hm_epochs,'loss:',epoch_loss)
#
#
#
#         #we come here after optimizing the weights
#         #tf.argmax is going to return the index of max values
#         #in this training module we are checking if the prediction is matching the value
#         correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
#         #accuracy is the float value of correct
#         accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
#         #this is just evaluation
#         print('Accuracy:',accuracy.eval({x:test_x, y:test_y}))

# train_neural_network(x)
