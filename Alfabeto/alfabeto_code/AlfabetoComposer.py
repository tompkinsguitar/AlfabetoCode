from alfabeto_code.AlfabetoMarkov import *
from alfabeto_sources import *
import ast
from alfabeto_data.all_data import numeral_converter
from music21 import *



# You can use the following code for a preview of the Markov Chain probabilites:
# `for state in markov: print('%r => %r' % (state, markov[state]))`
korpus = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, obizzi.libro_primo, stefani.stefani, sanz.sanz_1674]
random_state = random.choice(list(markovComposer(korpus, 'major', 4, 'first', 'guitar').keys()))
kaps = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7]
start_2 = 'I'
start_3 = ('I', 'IV')
start_4 = ('I', 'IV', 'I')


def markov_composer(corpus, mode, ngram, start_state, progression_element, tab):
    final = stream.Stream()
    sampleStream = []

    for x in start_state:
        sampleStream.append(x)

    # print(start_state)

    if ngram == 2:
        s1 = start_state
        max_length = 50
        # result = [s1]
        for i in range(max_length):
            next_state = weighted_choice(markovComposer(corpus, mode, ngram, progression_element, tab)[s1])
            if next_state is None:
                break
            elif i >= 12 and (s1 == 'I' or s1 == 'i'):
                break
            # stream.append(next_state)
            sampleStream.append(next_state)

                # stream.append(chord.Chord(next_state))
            s1 = next_state

    elif ngram == 3:
        s1, s2 = start_state
        max_length = 50
        # result = [s1, s2]
        for i in range(max_length):
            next_state = weighted_choice(markovComposer(corpus, mode, ngram, progression_element, tab)[(s1, s2)])
            if next_state is None:
                break
            elif i >= 12 and s1 == 'V' and (s2 == 'I' or s2 == 'i'):
                break
            # stream.append(next_state)
            sampleStream.append(next_state)

                # stream.append(chord.Chord(next_state))
            s1 = s2
            s2 = next_state

    elif ngram == 4:
        s1, s2, s3 = start_state
        max_length = 50
        # result = [s1, s2, s3]
        for i in range(max_length):
            next_state = weighted_choice(markovComposer(corpus, mode, ngram, progression_element, tab)[(s1, s2, s3)])
            if next_state is None:
                break
            elif i >= 12 and s2 == 'V' and (s3 == 'I' or s3 == 'i'):
                break
            # stream.append(next_state)
            sampleStream.append(next_state)

                # stream.append(chord.Chord(next_state))
            s1 = s2
            s2 = s3
            s3 = next_state

    elif ngram == 5:
        s1, s2, s3, s4 = start_state
        max_length = 30
        # result = [s1, s2, s3, s4]
        for i in range(max_length):
            next_state = weighted_choice(markovComposer(corpus, mode, ngram, progression_element, tab)[(s1, s2, s3, s4)])
            if next_state is None:
                break
            elif i >= 7 and s3 == 'V' and (s4 == 'I' or s4 == 'i'):
                break
            # stream.append(next_state)
            sampleStream.append(next_state)

                # stream.append(chord.Chord(next_state))
            s1 = s2
            s2 = s3
            s3 = s4
            s4 = next_state

    elif ngram == 6:
        s1, s2, s3, s4, s5 = start_state
        max_length = 30
        # result = [s1, s2, s3, s4]
        for i in range(max_length):
            next_state = weighted_choice(markovComposer(corpus, mode, ngram, progression_element, tab)[(s1, s2, s3, s4, s5)])
            if next_state is None:
                break
            elif i >= 7 and s4 == 'V' and (s5 == 'I' or s5 == 'i'):
                break
            # stream.append(next_state)
            sampleStream.append(next_state)

                # stream.append(chord.Chord(next_state))
            s1 = s2
            s2 = s3
            s3 = s4
            s4 = s5
            s5 = next_state

    elif ngram == 7:
        s1, s2, s3, s4, s5, s6 = start_state
        max_length = 30
        # result = [s1, s2, s3, s4]
        for i in range(max_length):
            next_state = weighted_choice(markovComposer(corpus, mode, 7, progression_element, tab)[(s1, s2, s3, s4, s5, s6)])
            if next_state is None:
                break
            elif i >= 7 and s5 == 'V' and (s6 == 'I' or s6 == 'i'):
                break
            # stream.append(next_state)
            sampleStream.append(next_state)

                # stream.append(chord.Chord(next_state))
            s1 = s2
            s2 = s3
            s3 = s4
            s4 = s5
            s5 = s6
            s6 = next_state

    print(sampleStream)

    for x in sampleStream:
        # print(x)
        for a, b in numeral_converter.items():
            if x == b:
                # print(a)
                c = chord.Chord(ast.literal_eval(a))
                c.lyric = x
                final.append(c)

        # stream.append(note.Note(x))
    # final.show()
    #final.write('lily.png', fp='/home/daniel/Desktop/Lily/lily.ppng')
    #final.show('midi')
    return final.show()



# print('all')
# markov_composer(korpus, 'major', 3, start_3, 'all', 'guitar')
#
# print('first')
# markov_composer(korpus, 'major', 3, start_3, 'first', 'guitar')
#
# print('first and last')
# markov_composer(korpus, 'major', 3, start_3, 'first_and_last', 'guitar')


print('Kaps 1')
markov_composer([kapsperger.v1], 'major', 3, start_3, 'all', 'guitar')

print('Kaps 2')
markov_composer([kapsperger.v2], 'major', 3, start_3, 'all', 'guitar')

print('Kaps 3')
markov_composer([kapsperger.v3], 'major', 3, start_3, 'all', 'guitar')

print('Kaps 4')
markov_composer([kapsperger.v4], 'major', 3, start_3, 'all', 'guitar')

print('Kaps 5')
markov_composer([kapsperger.v5], 'major', 3, start_3, 'all', 'guitar')

print('Kaps 6')
markov_composer([kapsperger.v6], 'major', 3, start_3, 'all', 'guitar')

print('Kaps 7')
markov_composer([kapsperger.v7], 'major', 3, start_3, 'all', 'guitar')

# print('Obizzi')
# markov_composer([obizzi.libro_primo], 'major', 3, start_3, 'all', 'guitar')
#
# print('Stefani')
# markov_composer([stefani.stefani], 'major', 3, start_3, 'all', 'guitar')
#
# print('Sanz')
# markov_composer([sanz.sanz_1674], 'major', 3, start_3, 'all', 'guitar')
