from music21 import *
from alfabeto_sources import *
from collections import OrderedDict
from alfabeto_data.all_data import numeral_converter, numeral_converter_plain, scale_degree_converter

"""This shows the fingerings of Alfabeto chords from low to high string"""

AlfabetoSymbols = ['+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z', '&']

AlfabetoTab = [[2, 2, 0, 0, 0], [2, 0, 0, 3, 3], [3, 2, 0, 1, 0], [0, 0, 2, 3, 2], [0, 2, 2, 1, 0],
               [0, 0, 2, 3, 1], [2, 2, 1, 0, 0], [3, 3, 2, 1, 1], [1, 3, 3, 3, 1], [0, 2, 2, 2, 0],
               [1, 3, 3, 2, 1], [3, 1, 0, 4, 3], [1, 1, 3, 4, 3], [3, 1, 1, 1, 4], [1, 0, 0, 3, 3],
               [3, 3, 1, 1, 1], [4, 4, 3, 2, 2], [2, 4, 4, 4, 2], [2, 2, 4, 5, 4], [4, 2, 2, 2, 5],
               [4, 4, 2, 2, 2], [2, 4, 4, 3, 2], [5, 5, 4, 3, 3], [3, 5, 5, 5, 3], [4, 3, 1, 2, 1]]

AlfabetoTuning = [note.Note('A3'), note.Note('D4'), note.Note('G3'), note.Note('B3'), note.Note('E4')]

AlfabetoPcTuning = [9, 2, 7, 11, 4]


AlfabetoDict = {key:value for key, value in zip(AlfabetoSymbols, AlfabetoTab)}


def AlfabetoPcChord(symbol, number):
    '''handles the transposition notation'''
    x = AlfabetoDict[symbol]
    z = [a + b for a, b in zip(AlfabetoPcTuning, x)]
    w = [((x + number) % 12) for x in z]
    return w


def converter(source, progression_element):
    """converts a string of letters and numbers into chords
    :param progression_element: what to return ("all", "first", "last", first_and_last)
    :param source: a string of alfabeto chords, like 'ABACH4AD'
    """
    source_no_spaces = []
    for x in source:
        if x in AlfabetoSymbols:
            source_no_spaces.append(x)
    progression = []
    barlines = []
    first_beat = []
    last_beat = []
    first_and_last = []
    first_beat.append(AlfabetoPcChord(source_no_spaces[0], 0))
    first_and_last.append(AlfabetoPcChord(source_no_spaces[0], 0))
    for x in range(len(source_no_spaces)):
        if source_no_spaces[x] == '|':
            barlines.append(source_no_spaces[x])
        if source_no_spaces[x] in AlfabetoSymbols:
            barlines.append(AlfabetoPcChord(source_no_spaces[x], 0))
            progression.append(AlfabetoPcChord(source_no_spaces[x], 0))
        elif type(source_no_spaces[x]) is int:
            progression[-1] = (AlfabetoPcChord(source_no_spaces[x-1], int(source_no_spaces[x])))
        if source_no_spaces[x] == '|' and x < len(source_no_spaces) and source_no_spaces[x+1] in AlfabetoSymbols:
            first_beat.append(AlfabetoPcChord(source_no_spaces[x+1], 0))
            first_and_last.append(AlfabetoPcChord(source_no_spaces[x+1], 0))
        if source_no_spaces[x] == '|' and x > 0 and source_no_spaces[x-1] in AlfabetoSymbols:
            last_beat.append(AlfabetoPcChord(source_no_spaces[x-1], 0))
            first_and_last.append(AlfabetoPcChord(source_no_spaces[x-1], 0))
    last_beat.append(AlfabetoPcChord(source_no_spaces[-1], 0))
    first_and_last.append(AlfabetoPcChord(source_no_spaces[-1], 0))
    all_final = []
    first_final = []
    last_final = []
    first_and_last_final = []
    if progression_element == 'barlines':
        return barlines
    elif progression_element == 'all':
        all_final.append(progression[0])
        for x in range(1, len(progression)):
            if progression[x] != progression[x-1]:
                all_final.append(progression[x])
        return all_final
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

from alfabeto_sources.all_sources import *

def song_roots(song_source):
    s = converter(song_source, 'all')
    song_chords = []
    song_chords_transposed = []
    for x in s:
        song_chords.append(chord.Chord(x).root().pitchClass)
    for x in song_chords:
        song_chords_transposed.append((x-song_chords[-1])%12)
    return song_chords_transposed

def root_from_continuo(source_list):
    alls = []
    for book in source_list:
        for song in book.values():
            song_list = []
            song_list_transposed = []
            song_chords = converter(song['alfabeto'], 'all')
            for x in song_chords:
                song_list.append(chord.Chord(x).root().pitchClass)
            for x in song_list:
                song_list_transposed.append((x-song_list[-1])%12)
            alls.append(song_list_transposed)
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


def transposed_pc_roots(source, progression_element):
    all_chords = chordSet(source, 'all')
    pc_chords = chordSet(source, progression_element)
    final_root = chord.Chord(all_chords[-1]).root().pitchClass
    trans_chords = []
    chord_roots = []
    for x in pc_chords:
        temp_root = chord.Chord(x).root().pitchClass
        chord_roots.append((temp_root - final_root) % 12)
    return chord_roots


def roots_corpus(alf_corpus, progression_element):
    alls = []
    for x in alf_corpus.values():
        alls.append(transposed_pc_roots(x, progression_element))
    return alls


def transposed_pc_chords(source, progression_element):
    all_chords = chordSet(source, 'all')
    pc_chords = chordSet(source, progression_element)
    final_root = chord.Chord(all_chords[-1]).root().pitchClass
    trans_chords = []
    numeral_chords = []
    for x in pc_chords:
        temp_list = []
        for y in x:
            temp_list.append((y - final_root) % 12)
        trans_chords.append(str(sorted(temp_list)))
    for x in trans_chords:
        numeral_chords.append(numeral_converter[x])
    return numeral_chords


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
    for x in pc_chords:
        temp_list = []
        for y in x:
            if type(y) is int:
                temp_list.append((y - final_root) % 12)
        trans_chords.append(str(sorted(temp_list)))
    for x in trans_chords:
        if x not in numeral_converter_plain.keys():
            numeral_chords.append('|')
        else:
            numeral_chords.append(numeral_converter_plain[x])
    return numeral_chords

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
    #     print(x, ':')
    #     print('    '.join(y))
    #     print()
    #     print()
    return all_chords
