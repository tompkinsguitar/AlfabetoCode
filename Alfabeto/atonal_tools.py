import time


def icv(list_of_pitches):
    pitch_classes = set(x % 12 for x in list_of_pitches)
    icv_dict = {x: 0 for x in range(1, 7)}
    for x in pitch_classes:
        for y in pitch_classes:
            ic = abs(x - y) % 6
            if ic in icv_dict.keys():
                icv_dict[ic] += 1
    final_icv = []
    for x in range(6):
        for y, z in icv_dict.items():
            if y == x:
                final_icv.append(int(z / 2))
    return final_icv


def prime_form(pitches):
    pc_set = sorted(set([pitch % 12 for pitch in pitches]))
    all_permutations = []

    def inversions(pcset, index):
        i_pitches = [(index - pc) % 12 for pc in pcset]
        return i_pitches

    def transpositions(pcset, index):
        t_pitches = [(index + pc) % 12 for pc in pcset]
        return t_pitches

    for x in range(12):
        all_permutations.append(sorted(inversions(pc_set, x)))
        all_permutations.append(sorted(transpositions(pc_set, x)))

    return min(all_permutations)

test_pitches = [0, 4, 2, 5, 3, 77]
print('time for icv:')
start_time_icv = time.time()
icv(test_pitches)
print(time.time() - start_time_icv)

print()

print('time for prime form:')
start_time_pc = time.time()
prime_form(test_pitches)
print(time.time() - start_time_pc)
