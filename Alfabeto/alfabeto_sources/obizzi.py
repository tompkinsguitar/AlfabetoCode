"""Obizzi: Madrigali et Arie a voce sola... libro primo"""

from alfabeto_data.all_data import lower_tuning_fixer


libro_primo = \
    {
        1: 'A|DC|A|CA|BAD|ABCA||AC|A+|CDEF|DGO|DAB|ABCA',
        2: 'CA|DC|AB|GA|BF|DC|A|BA|BC|AI|CA|BC|AC|AI|C|OH|OIE',
        3: 'A+|CB|AI|C||CD|FDA|G+E|BE+GA|BAD|+BE+C|AG+B|CA',
        4: 'ACAI|CABA|DOAE|+BGA|BC+C|ABC|A||C|CDF|DGB|AB|BABAD|ADAB|CAC|ACA|BABCA',
        5: 'ABA|DA|IC|+CAI|CDF|D+|GADGAB|BC+C|A+|CAB+|CA|A+CI|EGFB|EGFDAB+CA',
        6: 'DCAC|+CEA|BCA||AE|ICDE|FD+|GABABC|ACAI|CED|FEFD',
        7: 'EO|IE|E+G|B|BC+C|AC|AIHO|IE|IE+|GEFD||DF|DFG|BAB|CABC|AEDA|BGABA|DA+|G+B|EBG|DGE|BABA|DA+|G+B|EB|ABG|+GEBC|OBC|AD|AIEO|OIE',
        8: 'ADA|BAD|AD|AB|CA|C+CA|IC|ABC|+C|A+BCA||G|EF|D|GA|B|DCD+|CA|BC+C|A+B+|CA',
        9: 'O|G|GDHEG|GBG|ABO|CO|OI|EO|OIE|H|G|OBC|O',
        10: 'DE|EFD|A|BA|BCADE|EFD||FG|GAB|BC|A+G|EFD|ABA|BCAI|CE|D|A|B|E+GE|FD',
        11: 'E|OD|DE|EFD|DAB|BCA|AE|EDG|ODH|IDAI|EOIC||EHDO|G|HA|BG|AB|BG|OIC',
        12: 'D+|GB|GA|B||BA|D+|GBE|DF|GEF|GEFD',
        13: 'E|DG|BG|GE|BOB|CA|B|GDE|BHD|OBCA|BGA|BH|DOG|+EB|HDOB|CB|CO|ED|GCOAIH|OIE',
        14: 'E|D|BG|AB+C|OI|EOIE|EGF|DG+|GAB|BCO|OIC',
        15: 'EBHO|IAB|E+G+G|GA|IAGE|IE||DGBE|+GD|AIEB|HOIE',
        16: 'BG|GAB|A|B|BCA|DC|FD|BG|AB|B|GA|B||BA|DGA|BA|DGA|BAC|+BC|AC|+BC|ABA|DGAB',
        17: 'ABA|DCA|A|CB|CA|ED|EFD|DA|BABCA||ACA+|C|DCFE|FD|A|B+D|AD|ABACA',
        18: 'DA|DA|G+E|IEBA|DEFD||D+G|BAB|BAB|GAB|B|AF|DEDF|DAF|DGA+|G+I|EIED|EFD',
        19: 'AB|ADA|BADAD|RF|+E|BA|DA|ACA|ABA|DAC|C|AC|+CBABCA',
        20: 'AC|A|BD|AE|IED|FDA|BA|BC|A+G+|EA|B|A|BAD|AC|ACI|CD|F|DABCA',
        21: 'DC|AG|+E|BG|AB|BAD|FD|AGEI|E|+G|AB|CFGE|FD||G+A|BFDC|A+B|G+E|IEBA|DEFD',
        22: 'E|EDH|G|HB|G|AIE|E|D+|G+GE|B|OBC|AEAIE',
        23: 'E|ED+|GBE|B|OB|BCA|E+GAIE'
    }

libro_primo_continuo = \
    {
        1: {'continuo': '77|96|764|20e|0e9|70027||76|74|2220e924|957|9e0|e027',
            'alfabeto': 'A |DC|A  |C A|BAD|AB CA||AC|A+|C    DEF|DGO|DAB|ABCA',
            'data': {'key':'n', 'final': 7}},

        2: {'continuo': '267|962|740|597|0e98|962|74e|024|02|75421|2e7|0246|746|799|246|79t|792',
            'alfabeto': 'CA |DC |AB |GA |BF  |DC |A  |BA |BC|A I  |CA |BC  |AC |AI |C  |OH |OIE',
            'data': {'key': 'n', 'final': 2}},

        3: {'continuo': '754|220|e9|2462||75429|49|497|542|00245577|00e975|402466|77540|27',
            'alfabeto': 'A+ |C B|AI|C   ||    D|FD|  A|G+E|B E+G A |B A D |+BE+C |A G+B|CA',
            'data': {'key': 'n', 'final': 7}},

        4: {'continuo': '5457|09t9|7053|2t35|t024|5t0|5||0|t72|tt3t|5t|t9t97|5579t|02554|5420t9|t9t05',
            # 'alfabeto': 'ACAI|CABA|DOAE|+BGA|BC+C|ABC|A||C| DF|D GB|AB| ABAD|ADAB |C A C|A  CA |BABCA'}, #original
            'alfabeto': 'GBGA|BGHG|OPGL|EHMG|HBEB|GHB|G||B| OC|O MH|GH| GHGO|GOGH |B G B|G  BG |HGHBG',  #fixed
            'data': {'key': 'f', 'final': 5}},

        5: {'continuo': '5t9|7557|9e00|245t|00072|772|35t3|5t|t024|5422|09t2|05|5420e|032t|032|79t2|05',
            # 'alfabeto': 'ABA|DA  | IC |+CAI|C  DF|D +|GADG|AB| C+C|A + |CAB+|CA|A+ CI|EGFB|EGF|DAB+|CA'}, #original
            'alfabeto': 'GHG|OG  | AB |EBGA|B  OC|O E|MGOM|GH| BEB|G E |BGHE|BG|GE BA|LMCH|LMC|OGHE|BG', #fixed
            'data': {'key': 'f', 'final': 5}},

        6: {'continuo': '772454|20t9t05||550|700t970|27772|35t02t0|5579457|007|2027', #FIX_THIS!!!!!
            'alfabeto': 'D  CAC|+CBABCA||  E|IC   DE|FD + |GABAB C|A  C AI|CED|FEFD',
            'data': {'key': 'f', 'final': 7}},

        7: {'continuo': '2457|921|245|00|0246|776|79e7|924|5124|5249||98|94542|0700|2e02|7729e|04577000e97|99754|55420|2205|5452|07000e97|99754|555420|2200|0e05|545202|702|7799|7927|792',
            'alfabeto': 'E O |IE | +G|B | C+C|A C|AIHO|IE |I E+|GEFD||DF|DFG  |BAB |CABC|A EDA|B GAB     A|D A+ |G  +B|E BG|DGE |BAB    A|D A+ |G  + B|E B |A BG| +GEBC|OBC|A D |AIEO| IE',
            'data': {'key': 'n', 'final': 2}},

        8: {'continuo': '5795|t977|5579t|0255|00245|7700|99t024|52t05||332|002775|335|ttt9|7452|009|t024|52t205',
            # 'alfabeto': 'ADA |B AD|A DAB|C A |C +CA|I C |A BC+C|A+BCA||G  |E FD  |G A|B   |DCD+|C A|BC+C|A+B+CA',
            'alfabeto': 'GOG |H GO|G OGH|B G |B EBG|A B |G HBEB|GEHBG||M  |L CO  |M G|H   |OBOE|B G|HBEB|GEHEBG',
            'data': {'key': 'f', 'final': 5}},

        9: {'continuo': '77|55|59t05|505|7007|27|77|7927|7922|tt|55|5555|702|7',
            'alfabeto': 'O |G | DHBG| BG|AB O|CO|  | IEO| IE |H |G |    |OBC|O',
            'data': {'key': 'f', 'final': 7}},

        10: {'continuo': '7770|02777|99t9|t05700|0277||7233|35tt|tt00|5233|0277|99t9|t057|0002|7799|tttt|0230|27',
             # 'alfabeto': 'D  E| FD  |A BA|BCADE | FD || FG | AB |  C |A+G |EFD |A BA|BCAI|C  E|D A |B   |E+GE|FD',
             'alfabeto': 'O  L| CO  |G HG|HBGOL | CO || CM | GH |  B |GEM |LCO |G HG|HBGA|B  L|O G |H   |LEML|CO',
             'data': {'key': 'f', 'final': 7}},

        11: {'continuo': '2|79|9992|2499|99e0|0277|7722|2295|799t|999979|27792||2t97|55|t705|70|05|792',
             'alfabeto': 'E|OD|   E| FD |  AB| CA |  E |  DG|OD H|I D AI|EO IC||EHDO|G |HABG|AB| G|OIC',
             'data': {'key': 'n', 'final':2}},

        12: {'continuo': '9944|5000|57770||007|9444|5002|9994|5224|52249',
             'alfabeto': 'D + |GB  |GA  B||  A|D+  |GB E|D  F|GE F|GE FD',
             'data': {'key': 'n', 'final': 9}},

        13: {'continuo': '2|95|05|542|0t970|27|00|5422|00t9|700277|057|00t|9755|4200|t970|2200|22tt|2299|56779t|792',
             'alfabeto': 'E|DG|BG|  E|B  OB|CA|B |GDE |B HD|OB CA |BGA|B H|DOG |+EB |HDOB|C B |C O |E D |GCOAIH|OIE',
             'data': {'key': 'n', 'final': 2}},

        14: {'continuo': '2|9|9|9e0244|05|700042|779|2245792|2254|9554|570|027|792',
             'alfabeto': 'E|D| | ABE+ |BG|AB  +C|O I|E O I E|  GF|DG +|GAB| CO| IC',
             'data': {'key': 'n', 'final': 2}},

        15: {'continuo': '202t97|99e0|245545|57|97542|92||22|9502|2459|e120|t7992',
             'alfabeto': 'EBH  O|I AB|E+G +G| A|IAGE |IE||  |DGBE|+ GD|AIEB|HOI E',
             'data': {'key': 'n', 'final': 2}},

        16: {'continuo': '0055|5700|7700|0277|9922|2499|0055|5700|00|5557|0||007|9557|0007|9557|0772|4002|7772|4002|7007|9557|0',
             'alfabeto': 'B G | AB |A B | CA |D C | FD |B G | AB |  |G  A|B||B A|DG A|B  A|DG A|BA C|+B C|A  C|+B C|AB A|DG A|B',
             'data': {'key': 'n', 'final': 0}},

        17: {'continuo': '55t95|745|5420t|t055532|0t97|027|7799|t9t05||5452|000t9|7020|0277|99|tt|97|5t505',
             # 'alfabeto': 'A BA |DCA|   CB| CA    |E  D|EFD|  A |BADCA|| CA+|C    |DCFE| FD |A |B |AD|ABACA',
             'alfabeto': 'G HG |OBG|   BH| BG    |L  O|LCO|  G |HGOBG|| BGE|B    |OBCL| CO |G |H |GO|GHGBG',
             'data': {'key': 'f', 'final': 5}},

        18: {'continuo': '79|75|320|e0t9|7027||723|t5t|t57|35t|tt976|73072|77976|773532|3320e|0e0t97|027',
             # 'alfabeto': 'DA|DA|G+E|IEBA|DEFD||D+G|BAB| AB|GAB|  AF |DE DF|D AF |D GA+ |G +I |EIE  D|EFD',
             'alfabeto': 'OG|OG|MEL|ALHG|OLCO||OEM|HGH| GH|MGH|  GC |OL OC|O GC |O MGE |M EA |LAL  O|LCO',
             'data': {'key': 'f', 'final': 7}},

        19: {'continuo': '5t7|579|t97557|92|20|t975|5055|579t9|7500|02454|20t9t05', #FIX THIS !!!
             'alfabeto': 'ABD|ADA|BADA D|RF|+E|BADA| CA |   BA|DAC |   AC|+CBABCA',
             'data': {'key': 'f', 'final': 5}},

        20: {'continuo': '5554|55579|t75550|770007|2279|t9t0|55232|05|t23579t5|t977|5554|5420e|0722|7795|t05',
             'alfabeto': lower_tuning_fixer('A  C|A    |BDA  E|I E  D|F DA|BABC|A +G+|EA|B     A |BAD |A  C|A  CI|CDF |D A |BCA'),
             'data': {'key': 'f', 'final': 5}},

        21: {'continuo': '774|53|20|t3|5t|t97|277|5307|00|23|5t|023027||325|tt6740|52t|320|e0t9|t027',
             'alfabeto': lower_tuning_fixer('D C|AG|+C|BG|AB| AD|FD |AGEI|E |+G|AB|CFGEFD||G+A|BF DC |A+B|G+E|IEBA|DEFD'),
             'data': {'key': 'f', 'final': 7}},

        22: {'continuo': '2222|29t|555|tt00|555|7792|222222|9994|5452|0000|7002|777727792',
             'alfabeto': 'E   | DH|G  |H B |G  |A IE|      |D  +|G+GE|B   |OB C|A   EA IE',
             'data': {'key': 'n', 'final': 2}},

        23: {'continuo': '2|29|94|5002|0000|7770|027777|2457792',
             'alfabeto': 'E| D| +|GB E|B   |O  B| CA   |E+GA IE',
             'data': {'key': 'n', 'final': 2}},
    }