from music21 import *
from alfabeto_data.all_data import *
import os

paths = corpus.getComposer('josquin')


def palestrina_chorder(corpus):
    all_palestrina = []
    all_parsed = []
    for i in corpus:
        all_parsed.append(converter.parse(i))
    for i in all_parsed:
        pc_chords = []
        full_chords = i.chordify()
        for x in full_chords.flat.getElementsByClass(chord.Chord):
            # print(x)
            pc_chords.append(set(x.pitchClasses))
        final_root = chord.Chord(pc_chords[-1]).root().pitchClass
        trans_chords = []
        numeral_chords = []
        for x in pc_chords:
            temp_list = []
            for y in x:
                temp_list.append((y - final_root) % 12)
            trans_chords.append(str(sorted(temp_list)))
            # print(trans_chords)
        for x in trans_chords:
            if x in numeral_converter.keys():
                numeral_chords.append(numeral_converter[x])
        numeral_chords_set = []
        numeral_chords_set.append(numeral_chords[0])
        for x in range(1, len(numeral_chords)):
            if numeral_chords[x] != numeral_chords[x-1]:
                numeral_chords_set.append(numeral_chords[x])
        all_palestrina.append(numeral_chords_set)
    return all_palestrina


def bach_chorder():
    all_chorales = []

    for i in corpus.chorales.Iterator():
        pc_chords = []
        full_chords = i.chordify()
        for x in full_chords.flat.getElementsByClass(chord.Chord):
            # print(x)
            pc_chords.append(set(x.pitchClasses))
        final_root = chord.Chord(pc_chords[-1]).root().pitchClass
        trans_chords = []
        numeral_chords = []
        for x in pc_chords:
            temp_list = []
            for y in x:
                temp_list.append((y - final_root) % 12)
            trans_chords.append(str(sorted(temp_list)))
            # print(trans_chords)
        for x in trans_chords:
            if x in numeral_converter.keys():
                numeral_chords.append(numeral_converter[x])
        numeral_chords_set = []
        numeral_chords_set.append(numeral_chords[0])
        for x in range(1, len(numeral_chords)):
            if numeral_chords[x] != numeral_chords[x-1]:
                numeral_chords_set.append(numeral_chords[x])
        all_chorales.append(numeral_chords_set)
    return all_chorales


def bach_note_counter():
    all_chorale_data = []

    for i in corpus.chorales.Iterator():
        note_data = {}
        all_notes = []
        bass_part = i.parts[-1]
        a = []
        if type(bass_part.flat.notes[-1]) is note.Note:
            a.append(bass_part.flat.notes[-1].pitchClass)
        elif type(bass_part.flat.notes[-1]) is chord.Chord:
            a.append(bass_part.flat.notes[-1].bass().pitchClass)
        # print('final:', a[0])
        all_percents = []
        for x in i.flat.notes:
            if type(x) is note.Note:
                all_notes.append((x.pitch.pitchClass - a[0]) % 12)
            else:
                for y in x:
                    all_notes.append((y.pitch.pitchClass - a[0]) % 12)
        for x in range(12):
            note_data[x] = 0
        for x in all_notes:
            note_data[x] += 1
        for x in note_data.values():
            all_percents.append(x/len(all_notes)*100)
        all_chorale_data.append(all_percents)
        # print(note_data)
    return all_chorale_data


def corpus_note_counter(corpus_unparsed, key_sig):
    if key_sig == 'modal':
        print('yes')
    else:
        print(key_sig)
    all_chorale_data = []
    all_corpus_labels = []
    all_parsed = []
    if type(corpus_unparsed) is str:
        for root, dirs, files in os.walk(corpus_unparsed):
            for file_name, x in zip(files, range(len(files))):
                print(file_name, '...', x+1, 'of', len(files), '...')
                if file_name.endswith('.krn'):
                    # print('it is a krn')
                    path = os.path.join(root, file_name)
                    tempStream = converter.parse(path)
                    all_parsed.append(tempStream)
    else:
        for i, j in zip(corpus_unparsed, range(len(corpus_unparsed))):
            print('...parsing', j+1, 'of', len(corpus_unparsed), '...')
            all_parsed.append(converter.parse(i))
    for i in all_parsed:
        # print(type(i))
        if type(i) is stream.Score:
            # print("it's a score!")
            note_data = {}
            all_notes = []
            if len(i.parts) > 1:
                bass_part = i.parts[-1]
            else:
                bass_part = i.parts[0]
            a = []
            if len(bass_part.flat.notes) > 1:
                if type(bass_part.flat.notes[-1]) is note.Note:
                    a.append(bass_part.flat.notes[-1].pitchClass)
                elif type(bass_part.flat.notes[-1]) is chord.Chord:
                    a.append(bass_part.flat.notes[-1].bass().pitchClass)
            all_percents = []
            if len(a) > 0:
                # print('final:', a[0])
                theKey = i.flat.getElementsByClass(key.KeySignature)
                if len(theKey) == 0:
                    print('it is 0')
                    all_corpus_labels.append((0, a[0]))
                elif a[0]*7%12 == theKey[0].sharps % 12 or (a[0] + 3) * 7 % 12 == theKey[0].sharps % 12 or key_sig == 'modal':
                    if len(theKey) > 0:
                        bad_keys = [1, 3, 6, 8, 11]
                        # if a[0] in bad_keys and key_sig == 'modal':
                        #     # i.show()
                        # elif theKey[0].sharps == -1 and a[0] == 4 and key_sig == 'modal':
                        #     # i.show()
                        if key_sig == 'tonal':
                            all_corpus_labels.append((theKey[0].sharps, a[0]))
                        else:
                            all_corpus_labels.append((theKey[0].sharps, a[0]))
                    print('key', theKey[0].sharps, 'final', a[0])
                    # for x in i.flat.notes:
                    #     if type(x) is note.Note:
                    #         all_notes.append((x.pitch.pitchClass - a[0]) % 12)
                    #     else:
                    #         for y in x:
                    #             all_notes.append((y.pitch.pitchClass - a[0]) % 12)
                    for x in range(12):
                        note_data[x] = 0
                    for x in all_notes:
                        note_data[x] += 1
                    for x in note_data.values():
                        all_percents.append(x/len(all_notes)*100)
                    all_chorale_data.append(all_percents)
        if type(i) is stream.Opus:
            # print('yes, opus')
            for j in i:
                # print('j in opus', j)

                note_data = {}
                all_notes = []
                if len(j.parts) > 1:
                    bass_part = j.parts[-1]
                else:
                    bass_part = j.parts[0]
                a = []
                if len(bass_part.flat.notes) > 1:
                    if type(bass_part.flat.notes[-1]) is note.Note:
                        a.append(bass_part.flat.notes[-1].pitch.pitchClass)
                    elif type(bass_part.flat.notes[-1]) is chord.Chord:
                        a.append(bass_part.flat.notes[-1].root().pitch.pitchClass)
                all_percents = []
                if len(a) > 0:
                    # print('final:', a[0])
                    theKey = j.flat.getElementsByClass(key.KeySignature)
                    if len(theKey) == 0:
                        print('it is 0')
                        all_corpus_labels.append((0, a[0]))
                    elif a[0] * 7 % 12 == theKey[0].sharps % 12 or (a[0] + 3) * 7 % 12 == theKey[0].sharps % 12 or key_sig == 'modal':
                        if len(theKey) > 0:
                            bad_keys = [1, 3, 6, 8, 11]
                            # if a[0] in bad_keys and key_sig == 'modal':
                            #     # j.show()
                            # elif theKey[0].sharps == -1 and a[0] == 4 and key_sig == 'modal':
                            #     # j.show()
                            if key_sig == 'tonal':
                                all_corpus_labels.append((theKey[0].sharps, a[0]))
                            elif theKey[0].sharps == -1 and a[0] != 4 and a[0] not in bad_keys and key_sig == 'modal':
                                all_corpus_labels.append((theKey[0].sharps, a[0]))
                            elif a[0] not in bad_keys and key_sig == 'modal':
                                all_corpus_labels.append((theKey[0].sharps, a[0]))
                        print('key', theKey[0].sharps, 'final', a[0])
                        for x in j.flat.notes:
                            if type(x) is note.Note:
                                all_notes.append((x.pitch.pitchClass - a[0]) % 12)
                            else:
                                for y in x:
                                    all_notes.append((y.pitch.pitchClass - a[0]) % 12)
                        for x in range(12):
                            note_data[x] = 0
                        for x in all_notes:
                            note_data[x] += 1
                        for x in note_data.values():
                            all_percents.append(x / len(all_notes) * 100)
                        all_chorale_data.append(all_percents)
                # print(note_data)
    return all_chorale_data, all_corpus_labels


def corpus_chordify(corpus_unparsed, key_sig):
    if key_sig == 'modal':
        print('yes')
    else:
        print(key_sig)
    all_chorale_data = []
    all_corpus_labels = []
    all_parsed = []
    if type(corpus_unparsed) is str:
        for root, dirs, files in os.walk(corpus_unparsed):
            for file_name, x in zip(files, range(len(files))):
                print(file_name, '...', x+1, 'of', len(files), '...')
                if file_name.endswith('.krn'):
                    # print('it is a krn')
                    path = os.path.join(root, file_name)
                    tempStream = converter.parse(path)
                    all_parsed.append(tempStream)
    else:
        for i, j in zip(corpus_unparsed, range(len(corpus_unparsed))):
            print('...parsing', j+1, 'of', len(corpus_unparsed), '...')
            all_parsed.append(converter.parse(i))
    for i, p in zip(all_parsed, range(len(all_parsed))):
        print('...chordifying', p + 1, 'of', len(all_parsed), '...')
        if type(i) is stream.Score:
            all_notes = []
            note_data = {}
            song_percents = []
            note_counter = 0
            chorded_song = i.chordify().flat.getElementsByClass(chord.Chord)
            bass_note = chorded_song[-1].bass().pitchClass
            the_key = i.flat.getElementsByClass(key.KeySignature)
            if key_sig == 'modal' or bass_note * 7 % 12 == the_key[0].sharps % 12 \
                    or (bass_note + 3) * 7 % 12 == the_key[0].sharps % 12:
                for x in chorded_song:
                    for y in x:
                        all_notes.append((y.pitchClass - bass_note) % 12)
                        note_counter += 1
                for x in range(12):
                    note_data[x] = 0
                for x in all_notes:
                    note_data[x] += 1
                for x in range(12):
                    song_percents.append(note_data[x]/len(all_notes)*100)
                all_chorale_data.append(song_percents)
                all_corpus_labels.append((the_key[0].sharps, bass_note))
                print(the_key[0].sharps, bass_note)
        elif type(i) is stream.Opus:
            for j in i:
                all_notes = []
                note_data = {}
                song_percents = []
                note_counter = 0
                chorded_song = j.chordify().flat.getElementsByClass(chord.Chord)
                bass_note = chorded_song[-1].bass().pitchClass
                the_key = j.flat.getElementsByClass(key.KeySignature)
                if key_sig == 'modal' or bass_note * 7 % 12 == the_key[0].sharps % 12 \
                        or (bass_note + 3) * 7 % 12 == the_key[0].sharps % 12:
                    for x in chorded_song:
                        for y in x:
                            all_notes.append((y.pitchClass - bass_note) % 12)
                            note_counter += 1
                    for x in range(12):
                        note_data[x] = 0
                    for x in all_notes:
                        note_data[x] += 1
                    for x in range(12):
                        song_percents.append(note_data[x]/len(all_notes)*100)
                    all_chorale_data.append(song_percents)
                    all_corpus_labels.append((the_key[0].sharps, bass_note))
                    print(the_key[0].sharps, bass_note)
    return all_chorale_data, all_corpus_labels
            
            
            
            




