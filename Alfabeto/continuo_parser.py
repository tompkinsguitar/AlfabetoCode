from music21 import *
import pickle, time, os

# A = corpus.getComposer('monteverdi')
all_parsed = []
all_keys = []
all_chords = []

tonal_major_dict = {(0, 0): 'CM', (1, 7): 'GM', (2, 2): 'DM', (3, 9): 'AM', (4, 4): 'EM', (5, 11): 'BM', (6, 6): 'F♯M',
               (-1, 5): 'FM', (-2, 10): 'B♭M', (-3, 3): 'E♭M', (-4, 8): 'A♭M', (-5, 1): 'D♭M', (-6, 6): 'G♭M'}
tonal_minor_dict = {(0, 9): 'am', (1, 4): 'em', (2, 11): 'bm', (3, 6): 'f♯m', (4, 1): 'c♯m', (5, 8): 'g♯m',
                    (6, 3): 'd♯m', (-1, 2): 'dm', (-2, 7): 'gm', (-3, 0): 'cm', (-4, 5): 'fm', (-5, 10): 'b♭m',
                    (-6, 3): 'e♭m'}
modal_major = [('f', 5), ('n', 0), ('f', 0), ('n', 7), ('f', 10), ('n', 5),
               (-1, 5), (0, 0), (-1, 0), (0, 7), (-1, 10), (0, 5)]
modal_minor = [('n', 2), ('n', 9), ('f', 2), ('f', 7), ('n', 4),
               (0, 2), (0, 9), (-1, 2), (-1, 7), (0, 4)]


def crd_data(unparsed, modality):  
    def parser(song):
        x = converter.parse(song)
        if type(x) is stream.Score:
            song_chords = []
            crd = x.chordify().flat.getElementsByClass(chord.Chord)
            if len(x.flat.getElementsByClass(key.KeySignature)) > 0:
                key_sig = x.flat.getElementsByClass(key.KeySignature)[0].sharps
                bass_note = crd[-1].bass().pitchClass
                modal_type = []
                if modality == 'tonal':
                    for c in tonal_major_dict.keys():
                        modal_type.append(c)
                    for c in tonal_minor_dict.keys():
                        modal_type.append(c)
    #                 modal_type.append(c for c in tonal_minor_dict.keys())
                elif modality == 'modal':
                    for c in modal_major:
                        modal_type.append(c)
                    for c in modal_minor:
                        modal_type.append(c)
    #             print(modal_type, (key_sig, bass_note))
                if (key_sig, bass_note) in modal_type:
                    for c in crd:
                        song_chord = []
                        note_bass = (c.bass().pitchClass - bass_note) % 12
                        song_chord.append(note_bass)
                        song_chord.append(sorted(set([(n.pitchClass-bass_note-note_bass)%12 for n in c])))
                        song_chords.append(song_chord)
                    all_chords.append(song_chords)
                    all_keys.append((key_sig, bass_note))
        elif type(x) is stream.Opus:
            for y in x:
                song_chords = []
                song_chords = []
                crd = y.chordify().flat.getElementsByClass(chord.Chord)
                if len(x.flat.getElementsByClass(key.KeySignature)) > 0:
                    key_sig = y.flat.getElementsByClass(key.KeySignature)[0].sharps
                    bass_note = crd[-1].bass().pitchClass
                    modal_type = []
                    if modality == 'tonal':
                        for c in tonal_major_dict.keys():
                            modal_type.append(c)
                        for c in tonal_minor_dict.keys():
                            modal_type.append(c)
    #                     modal_type.append(c for c in tonal_minor_dict.keys())
                    elif modality == 'modal':
                        for c in modal_major:
                            modal_type.append(c)
                        for c in modal_minor:
                            modal_type.append(c)
                    if (key_sig, bass_note) in modal_type:
                        for c in crd:
                            song_chord = []
                            note_bass = (c.bass().pitchClass - bass_note) % 12
                            song_chord.append(note_bass)
                            song_chord.append(sorted(set([(n.pitchClass-bass_note-note_bass)%12 for n in c])))
                            song_chords.append(song_chord)
                        all_chords.append(song_chords)
                        all_keys.append((key_sig, bass_note))
    start = time.time()
    if type(unparsed) is str:
    
        for root, dirs, files in os.walk(unparsed):
            for file_name, x in zip(files, range(len(files))):
                print(file_name, '...', x+1, 'of', len(files), '...')
                if file_name.endswith('.krn'):
#                     print('it is a krn')
                    path = os.path.join(root, file_name)
                    st = time.time()
                    parser(path)
                    fin = time.time()
                    print('finished', len(all_chords), 'of', len(unparsed), 'in', fin - st, 'seconds')
                    
    else:
        for x in unparsed:
            st = time.time()
            parser(x)
            fin = time.time()
            print('finished', len(all_chords), 'of', len(unparsed), 'in', fin - st, 'seconds')
    print('entire process took:', time.time() - start, 'seconds')

    josquin_chords_pickle_out = open("pickles/josquin_continuo_chords.pickle", "wb")
    pickle.dump((all_chords, all_keys), josquin_chords_pickle_out)
    josquin_chords_pickle_out.close()
