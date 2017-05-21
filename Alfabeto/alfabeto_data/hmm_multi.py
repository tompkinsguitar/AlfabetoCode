import alfabeto_data.hmm_threading as ht
import alfabeto_data.dissertation_images as di
from multiprocessing import Pool

parallel_dict = {}
thing_number = 0
for cluster in range(2, 16):
    for mc in range(5):
        parallel_dict[thing_number] = {'cluster':cluster, 'mc': mc}
        thing_number += 1

def parallel_hmm(parallel_number):
    parallel_dict = {}
    thing_number = 0
    for cluster in range(2, 16):
        for mc in range(5):
            parallel_dict[thing_number] = {'cluster':cluster, 'mc': mc}
            thing_number += 1
    ht.hmm_pickle_generator('alfabeto continuo', di.GetAll.all_alf, di.modal_major, 'alfabeto_continuo', 
                            'major', parallel_dict[parallel_number]['mc'], parallel_dict[parallel_number]['cluster'], 
                            range(50), 'tryit/')
#     ht.hmm_pickle_generator('palestrina', di.palestrina_continuo, [(0, 0), (-1, 5)], 'palestrina', 
#                             'major', parallel_dict[parallel_number]['mc'], parallel_dict[parallel_number]['cluster'], 
#                             range(50), 'C:/Users/Daniel/Desktop/tryit')
    ht.hmm_pickle_generator('bach', di.palestrina_continuo, di.tonal_major, 'bach', 
                            'major', parallel_dict[parallel_number]['mc'], parallel_dict[parallel_number]['cluster'], 
                            range(50), 'tryit/')

pool = Pool(8)
pool.map(parallel_hmm, [x for x in parallel_dict])
