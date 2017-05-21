import ipyparallel as ipp
import numpy as np
import os

rc = ipp.Client()
dview = rc[:]
print(rc.ids)
print('happening')
dview.execute('import alfabeto_data.hmm_threading as ht')
dview.execute('import alfabeto_data.dissertation_images as di')
parallel_dict_ = {}
thing_number_ = 0
for cluster_ in range(2, 16):
    for book_ in range(7):
        for mc_ in range(5):
            for mc_range_ in range(500):
                parallel_dict_[thing_number_] = {'cluster': cluster_, 'mc': mc_, 'book_number': book_+1,
                                                 'mc_range': [mc_range_]}
                thing_number_ += 1

remaining_list = []
for num, data in parallel_dict_.items():
    for corpus in ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7']:
        for mode in ['major', 'minor']:
            if not os.path.exists('kapshmm/hmm_mc/%s/%s/%s/%s/%s.pkl' % (corpus, mode, parallel_dict_[num]['cluster'],
                                                                         parallel_dict_[num]['mc'],
                                                                         parallel_dict_[num]['mc_range'][0])):
                if num not in remaining_list:
                    remaining_list.append(num)

print('remaining length:', len(remaining_list))

@dview.parallel(block=True)
def parallel_hmm(parallel_number):
    parallel_dict = {}
    thing_number = 0
    for cluster in range(2, 16):
        for book in range(7):
            for mc in range(5):
                for mc_range in range(500):
                    parallel_dict[thing_number] = {'cluster': cluster, 'mc': mc, 'book_number': book+1,
                                                   'mc_range': [mc_range]}
                    thing_number += 1

    ht.hmm_pickle_generator('alfabeto continuo',
                            [di.GetComposer.all_kaps[parallel_dict[parallel_number]['book_number']-1]],
                            di.modal_major, 'k%s' % parallel_dict[parallel_number]['book_number'],
                            'major', parallel_dict[parallel_number]['mc'], parallel_dict[parallel_number]['cluster'],
                            parallel_dict[parallel_number]['mc_range'], 'kapshmm/')

    ht.hmm_pickle_generator('alfabeto continuo',
                            [di.GetComposer.all_kaps[parallel_dict[parallel_number]['book_number']-1]],
                            di.modal_minor, 'k%s' % parallel_dict[parallel_number]['book_number'],
                            'minor', parallel_dict[parallel_number]['mc'], parallel_dict[parallel_number]['cluster'],
                            parallel_dict[parallel_number]['mc_range'], 'kapshmm/')


print('imported stuff')
np.random.shuffle(remaining_list)
parallel_hmm.map(remaining_list)

