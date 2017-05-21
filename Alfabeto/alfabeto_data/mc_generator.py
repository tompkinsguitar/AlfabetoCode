from alfabeto_data.hmm_threading import hmm_randomizer as hr
from alfabeto_data import dissertation_images as di

for K in range(2, 16):
    for mc in range(5):
        hr('alfabeto continuo', di.GetAll.all_alf, di.modal_major, 'alfabeto_continuo',
           'major', mc, K, range(500), 'hmm/')
        hr('alfabeto continuo', di.GetAll.all_alf, di.modal_minor, 'alfabeto_continuo',
           'minor', mc, K, range(500), 'hmm/')

        hr('bach', di.bach_continuo, di.tonal_major, 'bach',
           'major', mc, K, range(500), 'hmm/')
        hr('bach', di.bach_continuo, di.tonal_minor, 'bach',
                   'minor', mc, K, range(500), 'hmm/')

        hr('palestrina', di.palestrina_continuo, [(0, 0), (-1, 5)], 'palestrina',
           'major', mc, K, range(500), 'hmm/')
        hr('palestrina', di.palestrina_continuo, [(0, 9), (-1, 2)], 'palestrina',
           'minor', mc, K, range(500), 'hmm/')

