def icv(list_of_pitches):
    """Returns the interval class vectors of pitch set"""
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
    """Returns prime form after attempting all inversions and transpositions of set"""
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




test_pitches = [0, 4, 2, 5, 3, 77] #works with numbers ove 12 and microtonal (nondiscrete) pitches
icv(test_pitches)

prime_form(test_pitches)
