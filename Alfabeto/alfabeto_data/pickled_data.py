import pickle
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import bach_note_counter, corpus_note_counter, corpus_chordify
from music21 import corpus
from Continuo.kmeans import alf_notes_and_labels
from alfabeto_sources import all_sources
from sklearn.externals import joblib

if __name__ == '__main__':
#     from time import time
    alfabeto_notes = alf_notes_and_labels(all_sources.GetAll.all_alf)
    alfabeto_pickle_out = open("pickles/alfabeto_notes.pickle", "wb")
    pickle.dump(alfabeto_notes, alfabeto_pickle_out)
    alfabeto_pickle_out.close()
#     from alfabeto_code.AlfabetoConverter import song_roots
#     all_songs = []
#     all_keys = []
#     st = time()
#     for x in all_sources.GetAll.all_alf:
#         for song in x.values():
#             t = time()
#             all_keys.append((song['data']['key'], song['data']['final']))
#             all_songs.append(song_roots(song['alfabeto']))
#             print('finished song in', time()-t, 'seconds')
#     alfabeto_roots_pickle_out = open('pickles/alfabeto_roots.pickle', 'wb')
#     pickle.dump((all_songs, all_keys), alfabeto_roots_pickle_out)
#     alfabeto_roots_pickle_out.close()
#     print('finished all in', time()-st, 'seconds')


    # bach_notes = corpus_chordify(corpus.getComposer('bach'), key_sig='tonal')
    # bach_notes_pickle_out = open("pickles/bach_notes.pickle", "wb")
    # pickle.dump(bach_notes, bach_notes_pickle_out)
    # bach_notes_pickle_out.close()

    # beethoven_notes = corpus_chordify(corpus.getComposer('beethoven'), key_sig='tonal')
    # beethoven_notes_pickle_out = open("pickles/beethoven_notes.pickle", "wb")
    # pickle.dump(beethoven_notes, beethoven_notes_pickle_out)
    # beethoven_notes_pickle_out.close()

    # corelli_notes = corpus_chordify('/home/daniel/Desktop/corelli/', key_sig='tonal')
    # corelli_notes_pickle_out = open("pickles/corelli_notes.pickle", "wb")
    # pickle.dump(corelli_notes, corelli_notes_pickle_out)
    # corelli_notes_pickle_out.close()

    # corelli_harm_pickle_out = open("pickles/corelli_harm.pickle", "wb")
    # pickle.dump(corelli_harm, corelli_harm_pickle_out)
    # corelli_harm_pickle_out.close()

    # dufay_notes = corpus_chordify('/home/daniel/Desktop/Duf/', key_sig='modal')
    # dufay_notes_pickle_out = open("pickles/dufay_notes.pickle", "wb")
    # pickle.dump(dufay_notes, dufay_notes_pickle_out)
    # dufay_notes_pickle_out.close()
    #
    # haydn_notes = corpus_chordify('/home/daniel/Desktop/quartet/', key_sig='tonal')
    # haydn_notes_pickle_out = open("pickles/haydn_notes.pickle", "wb")
    # pickle.dump(haydn_notes, haydn_notes_pickle_out)
    # haydn_notes_pickle_out.close()
    #
    # josquin_notes = corpus_chordify('/home/daniel/Desktop/Jos/', key_sig='modal')
    # josquin_notes_pickle_out = open("pickles/josquin_notes.pickle", "wb")
    # pickle.dump(josquin_notes, josquin_notes_pickle_out)
    # josquin_notes_pickle_out.close()

    # liber_usalis_notes_pickle_out = open("pickles/liber_usalis_notes.pickle", "wb")
    # pickle.dump(liber_usalis_notes, liber_usalis_notes_pickle_out)
    # liber_usalis_notes_pickle_out.close()

    # marini_notes_pickle_out = open("pickles/marini_notes.pickle", "wb")
    # pickle.dump(marini_notes, marini_notes_pickle_out)
    # marini_notes_pickle_out.close()

    # monteverdi_notes = corpus_chordify(corpus.getComposer('monteverdi'), key_sig='modal')
    # monteverdi_notes_pickle_out = open("pickles/monteverdi_notes.pickle", "wb")
    # pickle.dump(monteverdi_notes, monteverdi_notes_pickle_out)
    # monteverdi_notes_pickle_out.close()
    #
    # mozart_notes = corpus_chordify('/home/daniel/Desktop/mozart_quartets/', key_sig='tonal')
    # mozart_notes_pickle_out = open("pickles/mozart_notes.pickle", "wb")
    # pickle.dump(mozart_notes, mozart_notes_pickle_out)
    # mozart_notes_pickle_out.close()
    #
    # palestrina_notes = corpus_chordify(corpus.getComposer('palestrina'), key_sig='modal')
    # palestrina_notes_pickle_out = open("pickles/palestrina_notes.pickle", "wb")
    # pickle.dump(palestrina_notes, palestrina_notes_pickle_out)
    # palestrina_notes_pickle_out.close()
    #
    # trecento_notes = corpus_chordify(corpus.getComposer('trecento'), key_sig='modal')
    # trecento_notes_pickle_out = open("pickles/trecento_notes.pickle", "wb")
    # pickle.dump(trecento_notes, trecento_notes_pickle_out)
    # trecento_notes_pickle_out.close()

#-----------------
#
alfabeto_notes_pickle_in = open("pickles/alfabeto_notes.pickle", "rb")
alfabeto_notes_data = pickle.load(alfabeto_notes_pickle_in)

alfabeto_roots_pickle_in = open('pickles/alfabeto_roots.pickle', 'rb')
alfabeto_roots = pickle.load(alfabeto_roots_pickle_in)

bach_notes_pickle_in = open("pickles/bach_notes.pickle", "rb")
bach_notes_data = pickle.load(bach_notes_pickle_in)
#
bach_harm_pickle_in = open('pickles/bach_harm.pickle', 'rb')
bach_harm_data = pickle.load(bach_harm_pickle_in)

bach_chords_pickle_in = open("pickles/bach_harmonic_function.pickle", "rb")   #for harmonic function
bach_chords_data = pickle.load(bach_chords_pickle_in)

bach_continuo_pickle_in = open("pickles/bach_continuo_chords.pickle", "rb") #[0[047]] and keys
bach_continuo_data = pickle.load(bach_continuo_pickle_in)

# beethoven_notes_pickle_in = open("pickles/beethoven_notes.pickle", "rb")
# beethoven_notes_data = pickle.load(beethoven_notes_pickle_in)
#
# corelli_notes_pickle_in = open("pickles/corelli_notes.pickle", "rb")
# corelli_notes_data = pickle.load(corelli_notes_pickle_in)

# corelli_harm_pickle_in = open("pickles/corelli_harm.pickle", "rb")
# corelli_harm_data = pickle.load(corelli_harm_pickle_in)


# dufay_notes_pickle_in = open("pickles/dufay_notes.pickle", "rb")
# dufay_notes_data = pickle.load(dufay_notes_pickle_in)
#
# haydn_notes_pickle_in = open("pickles/haydn_notes.pickle", "rb")
# haydn_notes_data = pickle.load(haydn_notes_pickle_in)

# haydn_continuo_pickle_in = open("pickles/haydn_continuo_chords.pickle", "rb") #[0[047]] and keys
# haydn_continuo_data = pickle.load(haydn_continuo_pickle_in)

# josquin_notes_pickle_in = open("pickles/josquin_notes.pickle", "rb")
# josquin_notes_data = pickle.load(josquin_notes_pickle_in)
#
josquin_continuo_pickle_in = open("pickles/josquin_continuo_chords.pickle", "rb") #[0[047]] and keys
josquin_continuo_data = pickle.load(josquin_continuo_pickle_in)
#
# liber_usalis_notes_pickle_in = open("pickles/liber_usalis_notes.pickle", "rb")
# liber_usalis_notes_data = pickle.load(liber_usalis_notes_pickle_in)
#
# marini_notes_pickle_in = open("pickles/marini_notes.pickle", "rb")
# marini_notes_data = pickle.load(marini_notes_pickle_in)
# #
# monteverdi_notes_pickle_in = open("pickles/monteverdi_notes.pickle", "rb")
# monteverdi_notes_data = pickle.load(monteverdi_notes_pickle_in)

monteverdi_notes_data = joblib.load('pickles/monteverdi_notes.pkl')

monteverdi_continuo_pickle_in = open("pickles/monteverdi_continuo_chords.pickle", "rb") #[0[047]] and keys
monteverdi_continuo_data = pickle.load(monteverdi_continuo_pickle_in)


# mozart_notes_pickle_in = open("pickles/mozart_notes.pickle", "rb")
# mozart_notes_data = pickle.load(mozart_notes_pickle_in)

# mozart_continuo_pickle_in = open("pickles/mozart_continuo_chords.pickle", "rb") #[0[047]] and keys
# mozart_continuo_data = pickle.load(mozart_continuo_pickle_in)
#
palestrina_notes_pickle_in = open("pickles/palestrina_notes.pickle", "rb")
palestrina_notes_data = pickle.load(palestrina_notes_pickle_in)
#
# palestrina_chords_pickle_in = open("pickles/palestrina_harmonic_function.pickle", "rb")   #for harmonic function
# palestrina_chords_data = pickle.load(palestrina_chords_pickle_in)

palestrina_continuo_pickle_in = open("pickles/palestrina_continuo_chords.pickle", "rb") #[0[047]] and keys
palestrina_continuo_data = pickle.load(palestrina_continuo_pickle_in)

# trecento_notes_pickle_in = open("pickles/trecento_notes.pickle", "rb")
# trecento_notes_data = pickle.load(trecento_notes_pickle_in)

victoria_notes_data = joblib.load('pickles/victoria_notes.pkl')


zma_continuo_data = joblib.load('pickles/Zma_continuo.pkl')
zmo_continuo_data = joblib.load('pickles/Zmo_continuo.pkl')
zso_continuo_data = joblib.load('pickles/Zso_continuo.pkl')

zma_notes_data = joblib.load('pickles/Zma_notes.pkl')
zmo_notes_data = joblib.load('pickles/Zmo_notes.pkl')
zso_notes_data = joblib.load('pickles/Zso_notes.pkl')

liber_notes_data = joblib.load('pickles/liber_notes.pkl')
#
