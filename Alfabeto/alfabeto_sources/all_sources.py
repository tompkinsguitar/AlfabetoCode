from alfabeto_sources import *


class GetComposer:
    all_dindia = [dindia.DIndia_1621, dindia.DIndia_1623]
    all_ghizzolo = [ghizzolo.Ghizzolo_1623]
    all_giaccio = [giaccio.Giaccio_1618a, giaccio.Giaccio_1618b]
    all_kaps = [kapsperger.v1_continuo, kapsperger.v2_continuo, kapsperger.v3_continuo, kapsperger.v4_continuo,
                kapsperger.v5_continuo, kapsperger.v6_continuo, kapsperger.v7_continuo]
    all_landi = [landi.Landi_1620]
    all_marini = [marini.Marini_1622]
    all_milanuzzi = [milanuzzi.Milanuzzi_1622a, milanuzzi.Milanuzzi_1625, milanuzzi.Milanuzzi_1628,
                     milanuzzi.Milanuzzi_1630, milanuzzi.Milanuzzi_1635]
    all_montesardo = [montesardo.Montesardo_1612]
    all_obizzi = [obizzi.libro_primo_continuo]
    all_rontani = [rontani.Rontani_1619, rontani.Rontani_1620b, rontani.Rontani_1623]
    all_sabbatini = [sabbatini.Sabbatini_1652]
    all_stefani = [stefani.Stefani_1621, stefani.Stefani_1622, stefani.Stefani_1623]
    all_vitali = [vitali.Vitali_1622]

chronological = \
    {
        1610: [kapsperger.v1_continuo],
        1612: [montesardo.Montesardo_1612],
        1618: [giaccio.Giaccio_1618a, giaccio.Giaccio_1618b],
        1619: [kapsperger.v2_continuo, kapsperger.v3_continuo, rontani.Rontani_1619],
        1620: [landi.Landi_1620, rontani.Rontani_1620b],
        1621: [dindia.DIndia_1621, stefani.Stefani_1621],
        1622: [stefani.Stefani_1622, vitali.Vitali_1622, marini.Marini_1622, milanuzzi.Milanuzzi_1622a],
        1623: [stefani.Stefani_1623, dindia.DIndia_1623, kapsperger.v4_continuo, ghizzolo.Ghizzolo_1623, rontani.Rontani_1623],
        1625: [milanuzzi.Milanuzzi_1625],
        1627: [obizzi.libro_primo_continuo],
        1628: [milanuzzi.Milanuzzi_1628],
        1630: [milanuzzi.Milanuzzi_1630, kapsperger.v5_continuo],
        1632: [kapsperger.v6_continuo],
        1635: [milanuzzi.Milanuzzi_1635],
        1640: [kapsperger.v7_continuo],
        1652: [sabbatini.Sabbatini_1652]
    }

composer_labels = \
    {
        'Kapsperger 1610': [kapsperger.v1_continuo],
        'Montesardo 1612': [montesardo.Montesardo_1612],
        'Giaccio 1618': [giaccio.Giaccio_1618a],
        'Giaccio 1620': [ giaccio.Giaccio_1618b],
        'Kapsperger 1619a': [kapsperger.v2_continuo],
        'Kapsperger 1619b': [kapsperger.v3_continuo],
        'Rontani 1619': [rontani.Rontani_1619],
        'Landi 1620': [landi.Landi_1620],
        'Rontani 1620': [rontani.Rontani_1620b],
        'DIndia 1621': [dindia.DIndia_1621],
        'Stefani 1621': [stefani.Stefani_1621],
        'Stefani 1622': [stefani.Stefani_1622],
        'Vitali 1622': [vitali.Vitali_1622],
        'Marini 1622': [marini.Marini_1622],
        'Milanuzzi 1622': [milanuzzi.Milanuzzi_1622a],
        'Stefani 1623': [stefani.Stefani_1623],
        'DIndia 1623': [dindia.DIndia_1623],
        'Kapsperger 1623': [kapsperger.v4_continuo],
        'Ghizzolo 1623': [ghizzolo.Ghizzolo_1623],
        'Rontani 1623': [rontani.Rontani_1623],
        'Milanuzzi 1625': [milanuzzi.Milanuzzi_1625],
        'Obizzi 1627': [obizzi.libro_primo_continuo],
        'Milanuzzi 1628': [milanuzzi.Milanuzzi_1628],
        'Milanuzzi 1630': [milanuzzi.Milanuzzi_1630],
        'Kapsperger 1630': [kapsperger.v5_continuo],
        'Kapsperger 1632': [kapsperger.v6_continuo],
        'Milanuzzi 1635': [milanuzzi.Milanuzzi_1635],
        'Kapsperger 1640': [kapsperger.v7_continuo],
        'Sabbatini 1652': [sabbatini.Sabbatini_1652]
    }

composer_labels_linebreak = \
    {
        'Kapsperger\n1610': [kapsperger.v1_continuo],
        'Montesardo\n1612': [montesardo.Montesardo_1612],
        'Giaccio\n1618': [giaccio.Giaccio_1618a],
        'Giaccio\n1620': [ giaccio.Giaccio_1618b],
        'Kapsperger\n1619a': [kapsperger.v2_continuo],
        'Kapsperger\n1619b': [kapsperger.v3_continuo],
        'Rontani\n1619': [rontani.Rontani_1619],
        'Landi\n1620': [landi.Landi_1620],
        'Rontani\n1620': [rontani.Rontani_1620b],
        'DIndia\n1621': [dindia.DIndia_1621],
        'Stefani\n1621': [stefani.Stefani_1621],
        'Stefani\n1622': [stefani.Stefani_1622],
        'Vitali\n1622': [vitali.Vitali_1622],
        'Marini\n1622': [marini.Marini_1622],
        'Milanuzzi\n1622': [milanuzzi.Milanuzzi_1622a],
        'Stefani\n1623': [stefani.Stefani_1623],
        'DIndia\n1623': [dindia.DIndia_1623],
        'Kapsperger\n1623': [kapsperger.v4_continuo],
        'Ghizzolo\n1623': [ghizzolo.Ghizzolo_1623],
        'Rontani\n1623': [rontani.Rontani_1623],
        'Milanuzzi\n1625': [milanuzzi.Milanuzzi_1625],
        'Obizzi\n1627': [obizzi.libro_primo_continuo],
        'Milanuzzi\n1628': [milanuzzi.Milanuzzi_1628],
        'Milanuzzi\n1630': [milanuzzi.Milanuzzi_1630],
        'Kapsperger\n1630': [kapsperger.v5_continuo],
        'Kapsperger\n1632': [kapsperger.v6_continuo],
        'Milanuzzi\n1635': [milanuzzi.Milanuzzi_1635],
        'Kapsperger\n1640': [kapsperger.v7_continuo],
        'Sabbatini\n1652': [sabbatini.Sabbatini_1652]
    }



class GetAll:
    all_alf = []
    for x in GetComposer.all_dindia:
        all_alf.append(x)
    for x in GetComposer.all_ghizzolo:
        all_alf.append(x)
    for x in GetComposer.all_giaccio:
        all_alf.append(x)
    for x in GetComposer.all_kaps:
        all_alf.append(x)
    for x in GetComposer.all_landi:
        all_alf.append(x)
    for x in GetComposer.all_marini:
        all_alf.append(x)
    for x in GetComposer.all_milanuzzi:
        all_alf.append(x)
    for x in GetComposer.all_montesardo:
        all_alf.append(x)
    for x in GetComposer.all_obizzi:
        all_alf.append(x)
    for x in GetComposer.all_rontani:
        all_alf.append(x)
    for x in GetComposer.all_sabbatini:
        all_alf.append(x)
    for x in GetComposer.all_stefani:
        all_alf.append(x)
    for x in GetComposer.all_vitali:
        all_alf.append(x)





#########
