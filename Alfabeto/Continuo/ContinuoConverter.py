from music21 import *
from alfabeto_code import AlfabetoConverter as AC
from alfabeto_sources import *
from Continuo.ContinuoConverters import *

k = kapsperger.v7_continuo

def figure_grouper(continuo_note, alfabeto_chord):
    grouping = []
    if continuo_note in pc_scale_degrees:
        grouping.append(pc_scale_degrees[continuo_note])
    if alfabeto_chord in AC.AlfabetoSymbols:
        grouping.append(sorted(AC.chordSet(alfabeto_chord, 'all')[0]))
    elif alfabeto_chord == ' ':
        grouping.append([])
    return grouping


def figure_grouper_song(song):
    song_list = []
    song_list_no_duplicates = []
    for x, y in zip(song['continuo'], song['alfabeto']):
        for a, b in zip(x, y):
            if len(figure_grouper(a, b)) > 0:
                if b == ' ':
                    temp_list = [pc_scale_degrees[a], song_list[-1][-1]]
                    song_list.append(temp_list)
                else:
                    song_list.append(figure_grouper(a, b))
    song_list_no_duplicates.append(song_list[0])
    for x in range(1, len(song_list)):
        if song_list[x] != song_list[x-1]:
            song_list_no_duplicates.append(song_list[x])
        song_list_no_duplicates.append(song_list[x])
        # else:
            # print('check figure grouper song!!!')
    return song_list_no_duplicates


def transposed_figures(song):
    # print(song) #do this if there is an error in one of the songs
    transposed_song = []
    figured_song = figure_grouper_song(song)
    for x in figured_song:
        temp_list = []
        f_list = []
        for y in x[1]:
            f_list.append((y - figured_song[-1][0]) % 12)
        temp_list.append((x[0] - figured_song[-1][0]) % 12)
        temp_list.append(sorted(f_list))
        transposed_song.append(temp_list)
    return transposed_song


def figure_intervals_pc(song, mode):
    """mode can be a tuple ('f', 5) or string 'all' """
    final_song = []
    final_no_dupes = []
    if type(mode) is str:
        for x in transposed_figures(song):
            temp_list = [x[0]]
            f_list = []
            for y in x[1]:
                f_list.append((y-x[0]) % 12)
            temp_list.append(sorted(f_list))
            final_song.append(temp_list)
    elif type(mode) is tuple:
        # print('it is a tuple')
        if song['data']['key'] == mode[0] and song['data']['final'] == mode[1]:
            # print('it is this key')
            for x in transposed_figures(song):
                temp_list = [x[0]]
                f_list = []
                for y in x[1]:
                    f_list.append((y-x[0]) % 12)
                temp_list.append(sorted(f_list))
                final_song.append(temp_list)
    # print(final_song) #if there is a problem
    if len(final_song) > 0:
        final_no_dupes.append(final_song[0])
        for x in range(1, len(final_song)):
            if final_song[x] != final_song [x-1]:
                final_no_dupes.append(final_song[x])
    return final_no_dupes

def figure_intervals_pc_untransposed(song, mode):
    """mode can be a tuple ('f', 5) or string 'all' """
    final_song = []
    final_no_dupes = []
    if type(mode) is str:
        for x in figure_grouper_song(song):
            temp_list = [x[0]]
            f_list = []
            for y in x[1]:
                f_list.append((y-x[0]) % 12)
            temp_list.append(sorted(f_list))
            final_song.append(temp_list)
    elif type(mode) is tuple:
        # print('it is a tuple')
        if song['data']['key'] == mode[0] and song['data']['final'] == mode[1]:
            # print('it is this key')
            for x in figure_grouper_song(song):
                temp_list = [x[0]]
                f_list = []
                for y in x[1]:
                    f_list.append((y-x[0]) % 12)
                temp_list.append(sorted(f_list))
                final_song.append(temp_list)
    # print(final_song) #if there is a problem
    if len(final_song) > 0:
        final_no_dupes.append(final_song[0])
        for x in range(1, len(final_song)):
            if final_song[x] != final_song [x-1]:
                final_no_dupes.append(final_song[x])
    return final_no_dupes

def book_converter_pc(book, mode):
    all_songs = []
    for song in book.values():
        if type(mode) is tuple:
            all_songs.append(figure_intervals_pc(song, mode))
        elif mode == 'all':
            all_songs.append(figure_intervals_pc(song, mode))
        elif mode == 'other':
            if transposed_figures(song)[0][1] != transposed_figures(song[-2][1]):
                all_songs.append(figure_intervals_pc(song, mode))
        elif mode == 'major':
            if transposed_figures(song)[0][1] == [0, 4, 7] or transposed_figures(song)[1][1] == [0, 4, 7] or \
                            transposed_figures(song)[2][1] == [0, 4, 7]:
                all_songs.append(figure_intervals_pc(song, mode))
        elif mode == 'minor':
            if transposed_figures(song)[0][1] == [0, 3, 7] or transposed_figures(song)[1][1] == [0, 3, 7] or \
                        transposed_figures(song)[2][1] == [0, 3, 7]:
                all_songs.append(figure_intervals_pc(song, mode))
    all_songs_final = []
    for x in all_songs:
        if len(x) > 0:
            no_dupes = [x[0]]
            for y in range(1, len(x)):
                if x[y] != x[y - 1]:
                    no_dupes.append(x[y])
            all_songs_final.append(no_dupes)
    return all_songs_final

def corpus_converter_pc(list_of_books, mode):
    all_corpus = []
    for book in list_of_books:
        abook = book_converter_pc(book, mode)
        for song in abook:
            all_corpus.append(song)
    return all_corpus

def book_converter_pc_untransposed(book, mode):
    all_songs = []
    for song in book.values():
        if type(mode) is tuple:
            all_songs.append(figure_intervals_pc_untransposed(song, mode))
        elif type(mode) is list:
            for x in mode:
                all_songs.append(figure_intervals_pc_untransposed(song, x))
        elif mode == 'all':
            all_songs.append(figure_intervals_pc_untransposed(song, mode))
        elif mode == 'other':
            if figure_grouper_song(song)[0][1] != figure_grouper_song(song[-2][1]):
                all_songs.append(figure_intervals_pc_untransposed(song, mode))
        elif mode == 'major':
            if figure_grouper_song(song)[0][1] == [0, 4, 7] or figure_grouper_song(song)[1][1] == [0, 4, 7] or \
                            figure_grouper_song(song)[2][1] == [0, 4, 7]:
                all_songs.append(figure_intervals_pc_untransposed(song, mode))
        elif mode == 'minor':
            if figure_grouper_song(song)[0][1] == [0, 3, 7] or figure_grouper_song(song)[1][1] == [0, 3, 7] or \
                        figure_grouper_song(song)[2][1] == [0, 3, 7]:
                all_songs.append(figure_intervals_pc_untransposed(song, mode))
    all_songs_final = []
    for x in all_songs:
        if len(x) > 0:
            no_dupes = [x[0]]
            for y in range(1, len(x)):
                if x[y] != x[y - 1]:
                    no_dupes.append(x[y])
            all_songs_final.append(no_dupes)
    return all_songs_final


def figure_intervals(song, mode):
    final_song = []
    if mode == 'major' or mode == 'other' or mode == 'all':
        for x in transposed_figures(song):
            temp_list = [scale_degree_converter_major[x[0]]]
            f_list = []
            octave_fixer = []
            right_order = []
            for y in x[1]:
                a = (y-x[0]) % 12
                if a == 0:
                    octave_fixer.append(12)
                else:
                    octave_fixer.append(a)
            for w, z in zip(x[1], octave_fixer):
                if x[0] in diatonic_major:
                    if w in diatonic_major:
                        # print(x[0], w, z, 'all', x)
                        f_list.append(figures_natural[z])
                    elif w in sharp_major:
                        if z in figures_sharp:
                            # print(x[0], w, z, 'all', x)
                            f_list.append(figures_sharp[z])
                        elif z in figures_flat:
                            # print(x[0], w, z, 'all', x)
                            f_list.append(figures_flat[z])
                        else:
                            print('sharp EXCEPTION', x[0], w, z, 'all', x)
                    elif w in flat_major:
                        if z in figures_flat:
                            # print(x[0], w, z, 'all', x)
                            f_list.append(figures_flat[z])
                        elif z in figures_sharp:
                            # print(x[0], w, z, 'all', x)
                            f_list.append(figures_sharp[z])
                        else:
                            print('flat EXCEPTION', x[0], w, z, 'all', x)
                elif x[0] in sharp_major and w in diatonic_major:
                    # if z in diatonic_major:
                    #     # print('SHARP', x[0], w, z, 'all', x)
                    #     f_list.append(figures_natural[z])
                    # elif z-1 in diatonic_major:
                    #     # print('SHARP', x[0], w, z, 'all', x)
                    f_list.append(figures_natural[(z+1) % 12])
                elif x[0] in sharp_major and w in sharp_major:
                    # print('SHARP', x[0], w, z, 'all', x)
                    f_list.append(figures_sharp[z])
                elif x[0] in flat_major and w in diatonic_major:
                    if z in diatonic_major:
                        # print('FLAT', x[0], w, z, 'all', x)
                        f_list.append(figures_natural[z])
                    elif z+1 in diatonic_major:
                        # print('FLAT', x[0], w, z, 'all', x)
                        f_list.append(figures_natural[(z+1) % 12])
                elif x[0] in flat_major and w in flat_major:
                    # print('FLAT', x[0], w, z, 'all', x)
                    f_list.append(figures_flat[z])
                else:
                    print('exception found: ', x[0], w, z, x)
            for number in ordering:
                if number in f_list:
                    right_order.append(number)
            if right_order in wrong_figures:
                temp_list.append(right_figures[wrong_figures.index(right_order)][0:2])
            else:
                temp_list.append(right_order[0:2])
            final_song.append(temp_list)
    elif mode == 'minor':
        for x in transposed_figures(song):
            temp_list = [scale_degree_converter_minor[x[0]]]
            f_list = []
            octave_fixer = []
            right_order = []
            for y in x[1]:
                a = (y-x[0]) % 12
                if a == 0:
                    octave_fixer.append(12)
                else:
                    octave_fixer.append(a)
            for w, z in zip(x[1], octave_fixer):
                if x[0] in diatonic_minor:
                    if w in diatonic_minor:
                        # print(x[0], w, z, 'all', x)
                        f_list.append(figures_natural[z])
                    elif w in sharp_minor:
                        if z in figures_sharp:
                            # print(x[0], w, z, 'all', x)
                            f_list.append(figures_sharp[z])
                        elif z in figures_flat:
                            # print(x[0], w, z, 'all', x)
                            f_list.append(figures_flat[z])
                        else:
                            print('sharp EXCEPTION', x[0], w, z, 'all', x)
                    # elif w in flat_minor:
                    #     if z in figures_flat:
                    #         # print(x[0], w, z, 'all', x)
                    #         f_list.append(figures_flat[z])
                    #     elif z in figures_sharp:
                    #         # print(x[0], w, z, 'all', x)
                    #         f_list.append(figures_sharp[z])
                    #     else:
                    #         print('flat EXCEPTION', x[0], w, z, 'all', x)
                elif x[0] in sharp_minor and w in diatonic_minor:
                    if z in diatonic_minor:
                        # print('SHARP', x[0], w, z, 'all', x)
                        f_list.append(figures_natural[z])
                    elif z-1 in diatonic_minor:
                        # print('SHARP', x[0], w, z, 'all', x)
                        f_list.append(figures_natural[(z-1) % 12])
                elif x[0] in sharp_minor and w in sharp_minor:
                    # print('SHARP', x[0], w, z, 'all', x)
                    f_list.append(figures_sharp[z])
                # elif x[0] in flat_minor and w in diatonic_minor:
                #     if z in diatonic_minor:
                #         # print('FLAT', x[0], w, z, 'all', x)
                #         f_list.append(figures_natural[z])
                #     elif z+1 in diatonic_minor:
                #         # print('FLAT', x[0], w, z, 'all', x)
                #         f_list.append(figures_flat[z])
                # elif x[0] in flat_minor and w in flat_minor:
                #     # print('FLAT', x[0], w, z, 'all', x)
                #     f_list.append(figures_flat[z])
                else:
                    print('exception found: ', x[0], w, z, x)
            for number in ordering:
                if number in f_list:
                    right_order.append(number)
            if right_order in wrong_figures:
                temp_list.append(right_figures[wrong_figures.index(right_order)])
            else:
                temp_list.append(right_order)
            final_song.append(temp_list)
    return final_song


def book_converter(book, mode):
    all_songs = []
    for song in book.values():
        if mode == 'all':
            all_songs.append(figure_intervals(song, mode))
        elif mode == 'other':
            if transposed_figures(song)[0][1] != transposed_figures(song[-1][1]):
                all_songs.append(figure_intervals(song, mode))
        elif mode == 'major':
            if transposed_figures(song)[0][1] == [0, 4, 7] or transposed_figures(song)[1][1] == [0, 4, 7] or \
                            transposed_figures(song)[2][1] == [0, 4, 7]:
                all_songs.append(figure_intervals(song, mode))
        elif mode == 'major':
            if transposed_figures(song)[0][1] == [0, 3, 7] or transposed_figures(song)[1][1] == [0, 3, 7] or \
                        transposed_figures(song)[2][1] == [0, 3, 7]:
                all_songs.append(figure_intervals(song, mode))
    all_songs_final = []
    for x in all_songs:
        no_dupes = [x[0]]
        for y in range(1, len(x)):
            if x[y] != x[y - 1]:
                no_dupes.append(x[y])
        all_songs_final.append(no_dupes)
    return all_songs_final


def corpus_converter(corpus_list, mode):
    all_corpus = []
    for book in corpus_list:
        all_corpus.append(book_converter(book, mode))
    return all_corpus
