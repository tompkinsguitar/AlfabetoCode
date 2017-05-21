from music21 import *
from alfabeto_sources import *
from collections import OrderedDict
from alfabeto_data.all_data import numeral_converter, numeral_converter_plain, scale_degree_converter

TheorboTuning = [note.Note('A3'), note.Note('E3'), note.Note('B3'), note.Note('G3'),
                 note.Note('D3'), note.Note('A2'), note.Note('G2'), note.Note('F2'),
                 note.Note('E2'), note.Note('D2'), note.Note('C2'), note.Note('B1'),
                 note.Note('A1'), note.Note('G1')]

TheorboPcTuning = [9, 4, 11, 7, 2, 9, 7, 5, 4, 2, 0, 11, 9, 7]

def TabChord(tab_chord):
    chord_notes = []
    for x in range(7):
        if type(tab_chord[x]) is int:
            chord_notes.append(TheorboTuning[x].transpose(tab_chord[x]))
    if type(tab_chord[-1]) is int:
        chord_notes.append(TheorboTuning[(tab_chord[-1]-1)])
    return chord.Chord(chord_notes)


def TabPcChord(tab_chord):
    chord_notes = []
    for x in range(7):
        if type(tab_chord[x]) is int:
            chord_notes.append((TheorboPcTuning[x] + tab_chord[x]) % 12)
    if type(tab_chord[-1]) is int:
        chord_notes.append(TheorboPcTuning[(tab_chord[-1]-1)])
    return chord_notes


def converter(source, progression_element):

    barlines = []
    progression = []
    first_beat = []
    last_beat = []
    first_and_last = []
    first_beat.append(TabPcChord(source[0]))
    first_and_last.append(TabPcChord(source[0]))
    for x in range(len(source)):
        # if source[x] == '|':
        #     barlines.append('|')
        if type(source[x]) is list:
            barlines.append(TabPcChord(source[x]))
            progression.append(TabPcChord(source[x]))
        else:
            barlines.append(source[x])
        # elif source[x] is int:
        #     progression[-1] = (TabPcChord(source[x - 1]))
        if source[x] == '|' and x < len(source) and type(source[x+1]) is list:
            first_beat.append(TabPcChord(source[x + 1]))
            first_and_last.append(TabPcChord(source[x + 1]))
        if source[x] == '|' and x > 0 and type(source[x-1]) is list:
            last_beat.append(TabPcChord(source[x - 1]))
            first_and_last.append(TabPcChord(source[x - 1]))
    last_beat.append(TabPcChord(source[-1]))
    first_and_last.append(TabPcChord(source[-1]))
    all_final = []
    first_final = []
    last_final = []
    first_and_last_final = []
    if progression_element == 'all':
        all_final.append(progression[0])
        for x in range(1, len(progression)):
            if progression[x] != progression[x-1]:
                all_final.append(progression[x])
        return all_final
    elif progression_element == 'barlines':
        return barlines
    elif progression_element == 'first':
        first_final.append(first_beat[0])
        for x in range(1, len(first_beat)):
            if first_beat[x] != first_beat[x-1]:
                first_final.append(first_beat[x])
        return first_final
    elif progression_element == 'last':
        last_final.append(last_beat[0])
        for x in range(1, len(last_beat)):
            if last_beat[x] != last_beat[x-1]:
                last_final.append(last_beat[x])
        return last_final
    elif progression_element == 'first_and_last':
        first_and_last_final.append(first_and_last[0])
        for x in range(1, len(first_and_last)):
            if first_and_last[x] != first_and_last[x-1]:
                first_and_last_final.append(first_and_last[x])
        return first_and_last_final


def root_pitch(source_dict, progression_element):
    """finds the root of each chord
    :param source_dict: a dict of sources, like a corpus
    returns list of root progressions
    """
    chords = []
    all_roots = []
    for x in source_dict.values():
        chords.append(converter(x, progression_element))
    for a in chords:
        roots = []
        for x in a:
            z = chord.Chord(x)
            i = z.root()
            roots.append(i)
        all_roots.append(roots)
    return all_roots


def pc_roots(source, progression_element):
    all_roots = []
    for x in root_pitch(source, progression_element):
        roots = []
        for y in x:
            roots.append(y.pitchClass)
        all_roots.append(roots)
    return all_roots


def transposed_roots(source, progression_element):
    all_roots = []
    for x in pc_roots(source, progression_element):
        roots = []
        for y in x:
            roots.append((y - x[-1]) % 12)
        all_roots.append(roots)
    return all_roots


def corpus_roots(corpus_source, progression_element):
    alls = []
    for x in corpus_source:
        alls.append(transposed_roots(x, progression_element))
    return alls

"""
-------------------------------------------------------
Chords
"""


def chordSet(source, progression_element):
    """removes duplicates from the chord
    :param source: a string of alfabeto chords
    returns a set of pitch classes
    """
    return [sorted(set(x)) for x in converter(source, progression_element)]


def transposed_pc_chords(source, progression_element):
    all_chords = chordSet(source, 'all')
    pc_chords = chordSet(source, progression_element)
    final_root = chord.Chord(all_chords[-1]).root().pitchClass
    trans_chords = []
    numeral_chords = []
    numeral_chords_set = []
    for x in pc_chords:
        temp_list = []
        for y in x:
            temp_list.append((y - final_root) % 12)
        trans_chords.append(str(sorted(temp_list)))
    for x in trans_chords:
        if x in numeral_converter:
            numeral_chords.append(numeral_converter[x])
        # else:
        #     numeral_chords.append(numeral_converter[x])
    for x in range(1, len(numeral_chords)):
        if numeral_chords[x] != numeral_chords[x-1]:
            numeral_chords_set.append(numeral_chords[x])
    return numeral_chords_set


def transposed_chords_corpus(source, progression_element):
    all_chords = []
    for y in source.values():
        prog = transposed_pc_chords(y, progression_element)
        all_chords.append(prog)
    return all_chords


def all_combined(sources, progression_element):
    all_list = []
    for x in sources:
        all_list.append(transposed_chords_corpus(x, progression_element))
    return all_list


'''--------------------printing--------------------'''


def transposed_pc_chords_noMMD(source, progression_element):
    all_chords = chordSet(source, 'all')
    pc_chords = chordSet(source, progression_element)
    final_root = chord.Chord(all_chords[-1]).root().pitchClass
    trans_chords = []
    numeral_chords = []
    print(pc_chords)
    for x in pc_chords:
        temp_list = []
        for y in x:
            if type(y) is int:
                temp_list.append((y - final_root) % 12)
            else:
                temp_list.append(y)
        trans_chords.append(str(sorted(temp_list)))
    print(trans_chords)
    for x in trans_chords:
        if x in numeral_converter_plain.keys():
            numeral_chords.append(numeral_converter_plain[x])
        else:
            numeral_chords.append(x)
    print(numeral_chords)
    return pc_chords


def transposed_pc_chords_corpus_noMMD(source, progression_element):
    all_chords = []
    for y in source.values():
        prog = transposed_pc_chords_noMMD(y, progression_element)
        all_chords.append(prog)
    return all_chords

def transposed_chords_corpus_print(source, progression_element):
    all_chords = {}
    for x, y in source.items():
        prog = transposed_pc_chords_noMMD(y, progression_element)
        all_chords[x] = prog
    for x, y in all_chords.items():
        print(x, ':')
        print(' '.join(y))
        print()
        print()
    return None



'''-----------------------scale degrees---------------------'''

def transposed_scale_degrees(source, progression_element):
    all_chords = chordSet(source, 'all')
    pc_chords = chordSet(source, progression_element)
    final_root = chord.Chord(all_chords[-1]).root().pitchClass
    trans_chords = []
    sd_chords = []
    final_sd = []
    # print(pc_chords)
    for x in pc_chords:
        temp_list = []
        for y in x:
            if type(y) is int:
                temp_list.append((y - final_root) % 12)
            else:
                temp_list.append(y)
        trans_chords.append(sorted(temp_list))
    # print(trans_chords)
    for x in trans_chords:
        chord_list = []
        for y in x:
            if y in scale_degree_converter.keys():
                chord_list.append(scale_degree_converter[y])
            else:
                chord_list.append(y)
        sd_chords.append(chord_list)
    for x in sd_chords:
        final_sd.append(' '.join(x))
    # print(final_sd)
    return final_sd


def corpus_sd(source, progression_element):
    all_chords = {}
    for x, y in source.items():
        prog = transposed_scale_degrees(y, progression_element)
        # print(prog)
        all_chords[x] = prog
    # for x, y in all_chords.items():
        # print(x, ':')
        # print('    '.join(y))
        # print()
        # print()
    return all_chords