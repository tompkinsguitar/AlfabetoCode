import ipyparallel as ipp
from sklearn.externals import joblib
rc = ipp.Client()
dview = rc[:]

dview.execute('import numpy as np')
dview.execute('import time')
dview.execute('from sklearn.externals import joblib')
dview.execute('from scipy.spatial.distance import cdist')
dview.execute('import alfabeto_data.dissertation_images as di')


@dview.parallel(block=True)
def silhouette_hmm(mc):
    corpus_name = 'alfabeto_continuo'
    mode_name = 'major'
    K_range = 15
    flipped_data = {}
    for K in range(2, K_range+1):
        txt = 'preparing %s %s' % (mc, K)
        joblib.dump(txt, 'pickles/status_%s.pkl' % mc)
        all_data = []
        all_labels = []
        l_number = joblib.load('/home/daniel/Desktop/hmm_mc/%s/%s/%s/%s/0.pkl' % (corpus_name, mode_name, K, mc))['test'][0]
        l_numeral = joblib.load('/home/daniel/Desktop/hmm_mc/%s/%s/%s/%s/0.pkl' % (corpus_name, mode_name, K, mc))['train'][2]
        for l in l_number:
            if l[0] < len(l_numeral):
                all_labels.append(l_numeral[l[0]])
            else:
                all_labels.append('o')
        #             print('one didn\'t fit...')
        for x in range(50):
            temp_data = []
            c = joblib.load('/home/daniel/Desktop/hmm_mc/%s/%s/%s/%s/%s.pkl' % (corpus_name, mode_name, K, mc, x))['decode']
    #         print('decoded')
            for xx in c[1]:
                temp_data.append(xx)
            all_data.append(temp_data)
        numpied = np.swapaxes(np.array(all_data), 0, 1)
    #     print(numpied.shape)
        st = time.time()
        DIST = cdist(numpied, numpied, 'hamming')
    #     DIST = (cdist(numpied, numpied, 'hamming')*len(l_number))**2 #Quinn/White
        st2 = time.time()
        flipped_data[K] = di.k_means_simple(DIST, K, all_labels)
    #     print_labels = ['$'+x+'$' for x in all_labels]
    #     di.k_means_data(DIST, K, print_labels, '/home/daniel/Desktop/hmmkmeans/%s_%s.pdf' % (corpus, K))
    #     print('kmeans took', time.time()-st2)
        print(K, '-->', flipped_data[K])
        joblib.dump(flipped_data[K], 'pickles/scores/%s_%s_%s_%s.pkl' % (corpus_name, mode_name, mc, K))

    return flipped_data

silhouette_hmm.map([mc for mc in range(5)])
