"""Affetti Amorosi Canzonette ad una voce sola...
Giovanni Stevani, 1621
"""

from alfabeto_data.all_data import lower_tuning



stefani = \
    {
        1: 'O|OCM|C|CO|HM|MG|H|HG|GK4|K4|OLC|A|AC|OM|GH|M|KO|LC|A',
        2: 'O|EB|G|K4A|K4CMLC|A||O|GE|K4|OHMG|H|HGE|K4A|BK4|K4CA',
        3: 'OC|O|BC|O|COG|H|HM|MG|H|GB|G|GO|OI|G|GOG|GC|A',
        4: 'C|CD|D|DF|IG|B|EAI|IC',
        5: 'OCOB|CAOG|HMG|HGC|K4GAB|G+CB|CA',
        6: 'DFG|FD|DA|A|BA|EF|I||I|IC|AC|CI|C|A|D|F|DFG|FB|E|FI',
        7: 'H|GO|M|CB|H|GE|OM|BO|CA|AH|GE|K|CA',
        8: 'A|C|CA|AG|G|A|B||B|AC|FD|DEF|IA|ABC|A',
        9: 'G|OBG|GOH|OIC|EB|EBG|G+GAB|BMC|CABG',
        10: 'O|C|A|B|G|B|A|B|A|D|F|G|H|C|D|HE|EF|I',
        11: 'A|BAD|A|E|DA|AC|A||C|I|C|CAB|CA|ABCA',
        12: 'O|G|GH|H|G|GA|AB|B|O|C|A||E|G|EM|C|HM|G|H|O|MH|DO|HD|OGO|DO|G|OG|GC|G|CBC|MB|BC|A',
        13: 'GAI|CDHB|GHB|GA|B|CHB|G||GKA|BOC|OEHB|BC+G|ADGABD|HBG|AICD|HBG',
        14: 'A|BI|I|GEI|IC|HGA|B|IC|A|BC|A||AD|A|AC|A|BHD|H|A|B|H|D|AB|ABH|I',
        15: 'O|HGOD|HD|MGH|GO|EH|HBCAH|GO|EH|ECA||A|BG|HBG|ABC|A|G|O|HD|O|HD|OMG|H|HDOG|OBC|A',
        16: 'ODH|OBG|GE|HBG|G||GKMGH|HCOLC|A|OC|OCMB|C|HD|O|M|MG|H|GE|K|A|B|OC|M|MC|A|CA',
        17: 'H|HMG|H|K4C|MG|H|A|E|K4|H|G|K4|A|IC|HCB|OC|HC|M|CA|OE|K4H|HA|B|OC|B|C|A',
        18: 'AHC|A|GE|B|GEF|I|EG|A|E|B+H|EBG|A||EG4D|A|BAD|FH|BA|C+|HB|A|E|B+H|CBC|A',
        19: 'G|HC|A|OMG|H|DOC|A||HG|OG|+E|BG|GI|IGAI|C|AB|GOB|CAGB|GOIC|C|BG',
        20: 'A|AB|C|CD|EFI|CA|A|B|BD|DA|BO|C|BDF|FE|FI|OM|BCA',
        21: 'O|GO|HB|G||GH|GMG|H||H|M|OLC|A',
        22: 'ACADC|A|ACBC|A|AC|HI|C||ED|DADC|A|AB|BC|A',
        23: 'G|H|B|G|BE|H|BG||GH|B|G|H|B|G|B|E|B|G',
        24: 'O|OM|M|C||GH|A|BO|MC|AG|OLC|A',
        25: 'AB|BC|CA|GC|A||CD|GA|B|HB|DC|A|I|C|HBC|A',
        26: 'A|DGBC|AB|GA|B|OF|IB|AI|C|DGBC|A',
        27: 'G|HBC|CHB|G||GK|BAC|A|AGA|BG|OI|CD|HBG',
        28: 'D|DGEF|D|F|FR|R+R|FCAI|CB|CA|CDF|D',
        29: 'OM|CLC|O|G|GMLC|HG|HP|L|O|LCO|GML|CLC|A',
        30: 'E|IOI|E|B|BHAI|G|GL|LE|OIE|BHA|IGOI|E',
        31: 'G|AD|HB|G|H|BC|MG|HG|BMO|OBC|AE|EHB|G|O|OC|CF|B|GA|B|GH|GB|G|O|C|M|H|C|AD|H|B|G',
        32: 'E|B|G|A|I|H|AI|C|E|D|G|EF|D|B|C|O|OG|A|O|C||E|B|G|OH|I|C|H|B|G|OH|I|E|B|G|OH|I|E',
    }

Stefani_1621 = \
    {
        1: {'continuo': '7|723|22245|9579|t9753|735|5t|tt|t975|520 |00|702|775|3242|753|55t|32|0 7|202|7',
            'alfabeto': 'O| CM|C    |O   |H   M|  G|  |H |   G|  K4|  |OLC|A  |   C|O M|G H|M |K4O|L C|A',
            'data': {'key': 'f', 'final':7}},

        2: {'continuo': '7|27|542|0 7|0 2302|7||7|542|0 235|79t35|tt|t52|0 7|00 |0 23027',
            'alfabeto': 'O|EB|G  |K4A|K4CMLC|A||O|G E|K4   |O HMG|H |HGE|K4A|BK4|K4   CA',
            'data': {'key': 'f', 'final':7}},

        3: {'continuo': '772|7|02|77|275|t|4|355|t|550|5|5|7|79|2|275|300|22|7',
            'alfabeto': 'O C|O|BC|O |COG|H|H|MG |H|G B|G| |O|OI|G|GOG|   | C|A',
            'data': {'key': 'f', 'final':7}},

        4: {'continuo': '00|077|7|702|7733|t|tt|005|70',
            # 'alfabeto': 'C |CD |D|DF |I G |B|  |EAI|IC', #written chords
            'alfabeto': 'B |BO |O|OC |A M |H|  |LGA|AB', #fixed chords
            'data': {'key': 'f', 'final':0, 'tuning':-2}},

        5: {'continuo': '7270|2775|t35t|t||52|0 570|5420|27',
            'alfabeto': 'OCOB|CAOG|HMG |H||GC|K4GAB|G+CB|CA',
            'data': {'key': 'f', 'final': 7}},

        6: {'continuo': '945|449|754|7|07|24|9||9|992|72|9|2|779|ee4|02|44|945|40|2|49',
            'alfabeto': 'DFG|F D|  A|A|BA|EF|I||I|I C|AC|I|C|A  |   |D |F |DFG|FB|E|FI',
            'data': {'key': 'n', 'final': 9}},

        7: {'continuo': 'tt|t024|57|3|3|20|t|t024|52|73|07|27|9t|t024|52|0 230|27',
            'alfabeto': 'H |    |GO|M| |CB|H|    |GE|OM|BO|CA|AH|    |GE|K4   |CA',
            'data': {'key': 'f', 'final': 7}},

        8: {'continuo': '79|e0|02|7|52|42|77|00||02|42|79|420|024|97|742|7',
            'alfabeto': 'A |  |C |A|AG|G |A |B ||B |  |AC|F D|DEF|IA|ABC|A',
            'data': {'key': 'n', 'final': 7}},

        9: {'continuo': '55|705|557t|992|2220|245|545970|0230|279205',
            'alfabeto': 'G |OBG|G OH|OIC|E  B|EBG|G+G AB|BM C|CA  BG',
            'data': {'key': 'f', 'final': 5}},

        10: {'continuo': '9|99|66|77|00|55|00|77|00||0|77|99|44|55|00|22|99|t24|49|9',
             'alfabeto': 'O|  |C |A |B |G |B |A |B || |A |D |F |G |H |C |D |H E|EF|I',
             'data': {'key': 'n', 'final': 9}},

        11: {'continuo': 'e|e97|0e9|7ee|457|09e|702|7||22|979|2|0e9|7|027',
             'alfabeto': 'A|   |BAD|A  |B  |D A|A C|A||C |I  |C|ABC|A|BCA',
             'data': {'key': 'n', 'final': 7}},

        12: {'continuo': '7|7|5|t|t97|579|57|0|0t9|754|202|7||724|5|23|2|20|tt|5|t|79t|0t|979|t9|757|97|545|75|424|54|202|30|2|7',
             'alfabeto': 'O| |G|H|H  |G  |GA|B|B  |O  |C  |A|| E |G|EM|C|  |HM|G|H|O  |MH|DO |HD|OGO|DO|G  |OG| C |G |CBC|MB|C|A',
             'data': {'key': 'f', 'final': 7}},

        13: {'continuo': '575|29t0|55t0|57|00|2t0|5||507|0072|7290|0245|795709|t055|7929|t05',
             'alfabeto': 'GAI|CDHB|G HB|GA|B |CHB|G||GKA|B OC|OEHB|BC+G|ADGABD|HBG |AICD|HBG',
             'data': {'key': 'f', 'final': 5}},

        14: {'continuo': '776|77|0e9|9674|5295|7920|e957|000|96|77|9e02|7||79|7|6|7|00e|95|7|0|t|t|9|776|70e|9674|776|77|0e9|9674|5295|7920|e957|000|96|77|9e02|7',
             'alfabeto': 'A  |  |B I|    |GEI |I C |HG A|B  |IC|A |B C |A||AD|A|C|A|BHD|H |A|B|H| |D|A B|ABH|I   |A  |  |B I|    |GEI |I C |HG A|B  |IC|A |B C |A',
             'data': {'key': 'n', 'final': 7}},

        15: {'continuo': '7779|t579|t9|7235tt|57|2t|027t|57|2t|027||7|05|tt055|702|7|55|54|55|79|t9|79|t9|5235|tt|9755|702|7',
             'alfabeto': 'O   |HGOD|HD|M  GH |GO|EH|BCAH|GO|EH|ECA||A|BG|H BG |ABC|A|G |  |  |O |HD|O |HD|O MG|H |HDOG|OBC|A',
             'data': {'key': 'f', 'final': 7}},

        16: {'continuo': '79t9|705|5420|t02t05|5||520235t0|2452702302|77|76|7630|22|0t9|775|3|5|tt|52|03|557|0|77|t0|22|77|27',
             'alfabeto': 'ODH |OBG|G E |H   BG|G||G K MGH |H  COL   C|A |OC|OCMB|C | HD|O  |M|G|H |GE|K |A  |B|OC|M |MC|A |CA',
             'data': {'key': 'f', 'final': 7}},

        17: {'continuo': 't|t|t35|tt|t|0 2|35|tt|7|2|0 |t|5|0 |7|9|2|t20|72|t23|27|72|0 t|57|0|72|0|2|7',
             'alfabeto': 'H| |HMG|H | |K4C|MG|H |A|E|K4|H|G|K4|A|I|C|HCB|OC|HCM|CA|OE|K4H|HA|B|OC|B|C|A',
             'data': {'key': 'f', 'final': 7}},

        18: {'continuo': '7e2|77|542|00|524|99|245|77|542|04e|202|7||2e 9|77|079|4e|07|24|e0|77|542|04e|202|7',
             'alfabeto': 'AHC|A |G E|B |GEF|I |EG |A |E  |B+H|EBG|A||EG4D|A |BAD|FH|BA|C+|HB|A |E  |B+H|CBC|A',
             'data': {'key': 'n', 'final': 7}},

        19: {'continuo': '5|t02|779t0245|735|t|972|7||t5|75|420|05|579|9579|22|77544|570|2759t0|55792|29t|0205',
             'alfabeto': 'G|H C|A       |OMG|H|DOC|A||HG|OG|+E |BG|G I|IGAI|C |A  B |GOB|CAG  B|G OIC|   |B  G',
             'data': {'key': 'f', 'final': 5}},

        20: {'continuo': '7|79e0|224|57975|42499|67|742|00e|997|57|07|220|e979e|0246|892|49|7532|02|7',
             'alfabeto': 'A|A  B|C  |C D  |E FI |CA|A  |B  |B D|DA|BO|C  |     |B DF|F E|FI|O M |BC|A',
             'data': {'key': 'n', 'final': 7}},

        21: {'continuo': '7|579574|59t20|5||5t02t24|52375|t||tt|75320t|07002|7',
             'alfabeto': 'O|G  O  |H   B|G||G   H  |G M G|H||H |M     |OL  C|A',
             'data': {'key': 'f', 'final': 7}},

        22: {'continuo': '76792|75|420e9|775|42|e79|2||29|9896|75|4202|402|7',
             'alfabeto': 'ACADC|A | ACBC|A  |AC| HI|C||ED|DADC|A |A B | BC|A',
             'data': {'key': 'n', 'final': 7}},

        23: {'continuo': '55|t|0|5|32|tt9|00|5||5|t|0|5|9|t|0|5|3|2t|0|55',
             'alfabeto': 'G |H|B|G|BE|H  |B |G||G|H|B|G| |H|B|G|B|E |B|G ',
             'data': {'key': 'f', 'final': 5}},

        24: {'continuo': '7|73|3|2||520t|t97|57|07|32|t024|572|t',
             'alfabeto': 'O|OM|M|C||G  H|A  |  |BO|MC|A  G|OLC|A',
             'data': {'key': 'f', 'final': 7}},

        25: {'continuo': '70|0e2|227|572|7||774|29|547|00|e0|92|77|77|77|9|2|e|00|27',
             'alfabeto': 'AB|B C|C A|G C|A||   |CD|G A|B |HB|DC|A |  |  |I|C| |HB|CA',
             'data': {'key': 'n', 'final': 7}},

        26: {'continuo': '7|9e02|70|57|00|794|90|79|22|9e02|7',
             'alfabeto': 'A|DGBC|AB|GA|B |O F|IB|AI|C |DGBC|A',
             'data': {'key': 'n', 'final': 7}},

        27: {'continuo': '5|t02|t0|5||5320|072|7|7457|05|779|29|t0|5',
             'alfabeto': 'G|HBC|HB|G||G  K|BAC|A|AG A|BG|O I|CD|HB|G',
             'data': {'key': 'f', 'final': 5}},

        28: {'continuo': '77|7300|027|22|29|929|2057|0e|05|002|7',
             # 'alfabeto': 'D |DGEF| D |F |FR|R+R|FCAI|CB|CA|CDF|D', #original
             'alfabeto': 'O |OMLC| O |C |CI|IEI|CBGA|BH|BG|BOC|O', #lowered
             'data': {'key': 'n', 'final': 7}},

        29: {'continuo': '7730|200|027|55|530220|tt5|tt5|5|7|0027|5530|202|7',
             'alfabeto': 'O M |CLC|O  |G | GML C|H G|H P|L|O|L CO|G ML|CLC|A',
             'data': {'key': 'f', 'final': 7}},

        # 30: {'continuo': '00|75|570|tt|t85775|44|4tt|t|0|557|t785|7785|7', #really messed up
        #      'alfabeto': 'E|IOI|E|B|BHAI|G|GL|LE|OIE|BHA|IGOI|E',
        #      'data': {'key': '', 'final':}},

        31: {'continuo': '5|79|t0|5|t|02|35|t5|037|02|72|2t0|5|7|72|24|50|0|07|0|0|5t|50|5|5|5|7|2|3|t|2|79|t9|0|5',
             'alfabeto': 'G|AD|HB|G|H|BC|MG|HG|BMO|BC|AE|EHB|G|O|OC|CF|B | |GA|B| |GH|GB|G| | |O|C|M|H|C|AD|H |B|G',
             'data': {'key': 'f', 'final': 5}},

        32: {'continuo': '2|0|5|5|7|9|t|79|22|2|9|5|44|9e|0|2|7|72|7|72|2||2|05|5|7t|99|2|2|t|0|5|5|7t|9|2|2|2|0|5|5|7t|9|2',
             'alfabeto': 'E|B|G| |A|I|H|AI|C |E|D|G|EF|D |B|C|O|OG|A|O |C||E|B |G|OH|I |C| |H|B|G| |OH|I|E| | |B|G| |OH|I|E',
             'data': {'key': 'n', 'final': 2}},
    }
# aa = Stefani_1621[28]['alfabeto']
# new = []
# for x in aa:
#     if x in lower_tuning:
#         new.append(lower_tuning[x])
#     else:
#         new.append(x)
# print(new)

Stefani_1622 = \
    {
        1: {'continuo': '777|73000|27774|22799|22tt|02302|77||774|22799|22ttt|33255|tt|ttt|tt024|55452|0 2302|7',
            'alfabeto': 'O  | MB  |CA  +|E OI |    |B   C|A ||O +|E OI |C H  |M EG |H |   |     |G   E|K4EMBC|A',
            'data': {'key': 'f', 'final': 7}},

        2: {'continuo': '779|t9753|245975|32022|7||2 27|579tt0|579579|tt35t|t02357|027',
            'alfabeto': 'O D|HDO M|C  DOG|M BC |A||C5 A|G  H B|G   AD|H MGH| BCMGO|BCA',
            'data': {'key': 'f', 'final': 7}},

        3: {'continuo': '727|454|20t|t57|022|7||75t|355|t|520 |577|0|097|022|7',
            'alfabeto': 'OCO|+G+|E H| GO|BC |A||OGH|MG |H|GEK4|A  |B| DO|LG |A',
            'data': {'key': 'f', 'final': 7}},

        4: {'continuo': '92|49|9502|t05||57|92|29|70|294||9',
            'alfabeto': 'DE|FD|G BE|HBG||GA|IG| D|AE|EDF||D',
            'data': {'key': 'n', 'final': 9}},

        5: {'continuo': '05t|t35|t3|t||t|t9|75|02|77|t979|20|5207|0',
            'alfabeto': 'BGH| MG|HM|H|| |HD|OG|BC|AG|HDOI|CB|GEBA|B',
            'data': {'key': 'f', 'final': 0}},

        6: {'continuo': '75302|7597|92||2275|323|0 t97|27',
            'alfabeto': 'OGMBC|AGDA|IC||C OG|MEM|K4HDO|CA',
            'data': {'key': 'f', 'final': 7}},

        7: {'continuo': '5795t|t9t97|757|5t9|05|02404|457|702|7|t9t9753|325|tt024|523230t9|05',
            'alfabeto': 'G   H| DH O| GO|GHD|EG|B +  |+GO| BC|A|H     M|  G|H    |  M  BH |BG',
            'data': {'key': 'f', 'final': 5}},

        8: {'continuo': '0|55227|7542|00|07|67|44|27|427|7792|770|0e0|0|597|0|5|7|0',
            'alfabeto': 'B|G E A|  +C|B | A|CA|DE| A| CA|   D|CAB| HB| |GHA|B|G|A|B',
            'data': {'key': 'n', 'final': 0}},

        9: {'continuo': '29|49|57|92||22|05|59|70|92|49|77|92',
            'alfabeto': 'ED|FD|GO|IE||E |BG|GD|AB|DE|FD|O |IC',
            'data': {'key': 'n', 'final': 2}},

        10: {'continuo': '55|tt3|70|0 |5t|0|5||5|23|5t|t9|t3t|5|2t|05|555|t2|79|92|5|35|t2t|50|5',
             'alfabeto': 'G |H M|BA|K4|GH|B|G||G|EM|GH| D|HMH|G|CH|BG|   |HB|OI| C|G|MG|HCH|GB|G',
             'data': {'key': 'f', 'final':5}},

        11: {'continuo': '55|22|9t|52|77|9t|00|55|3|333|33|33|0 0|2t|55|tt||57|9t|00|55|52|70|22|79|t0|5|229|t9|775|542|0|t0|220|t7|2t|05',
             'alfabeto': 'G |E |DH|GC|O |DH|B |G |M|   |  |  |K4 |EH|G |H ||GO|DH|B |G | E|OL|C |AD|HB|G|E D|HD|O G|  A|B|HB|E B|HO|CH|BG',
             'data': {'key': 'f', 'final': 5}},

        12: {'continuo': '5520|tt0 |07702|9t0|5||3325t|t52779|t92|tt9|7|55|33|22|0 0|t5|57|0|77|5|t02|0|5',
             'alfabeto': 'G EB|H B4|LO BC|DHB|G||M EGH| GEA I|HIC|H D|O|G |M |E |K4 |HG| A|B|O |G|HBE|B|G',
             'data': {'key': 'f', 'final': 5}},

        13: {'continuo': 't|572|230|27|775|790|02t|05|55||0 07|007|27|75|5|597|92|2|20|t2t|79|22',
             'alfabeto': 'H|GOC| MB|CA|  G|ODB|E H|BG|  ||K4 O|B O|CA| G|G|I O|IC| |CB|HCH|OI|C ',
             'data': {'key': 'f', 'final': 2}},

        14: {'continuo': '5|3|0 |0|2|7|5|t|05||5|5|t|0 0|5|t|97|50|5|2|7|0t|7|7|29|t|0|5',
             'alfabeto': 'G|M|K4|B|C|A|G|H|BG||G| |H|K4 |G|H|DO|GB|G|E|A|BH|O| |CD|H|B|G',
             'data': {'key': 'f', 'final': 5}},

        15: {'continuo': 't33|35t|t|tt|355tt55|t055|5702|302|774444|59tt0|5555|5209|t20|5',
             'alfabeto': 'HM | GH| |  |MG H G |HBG | ABE|MBC|A +   |GDH B|G   | EBD|HEB|G',
             'data': {'key': 'f', 'final': 5}},

        16: {'continuo': '702|779e0|27|00245|79|2|24|997|55|57|09|49|e04|27',
             'alfabeto': 'ABC|A    |EA|B    |AI|C|EF|IO |G | A|BD|FD|HB+|CA',
             'data': {'key': 'n', 'final': 7}},

        17: {'continuo': '92|49|92|t79|22|49||9e0|27|702|49',
             'alfabeto': 'DE|FD| C|HOI|E |FD|| HB|CA| BC|FD',
             'data': {'key': 'n', 'final': 9}},

        18: {'continuo': '79e027|079570||00797|72792|5249|7702|7',
             'alfabeto': 'ADGBCA|BADGAB||B ADA| CAIG|GEFD|A BC|A',
             'data': {'key': 'n', 'final': 7}},

        19: {'continuo': '5|55|t3|02|77|77|55|t0|5||0|00|77|24|54|57|00|00|77|2t0|5',
             'alfabeto': 'G|  |HM|LC|AO|  |G |HB|G||B|  |O |E+|G+|GA|B |  |O |CHB|G',
             'data': {'key': 'f', 'final': 5}},

        20: {'continuo': '7|22|27|5|5|5|7|2|2|2|27|5|7|70|2|7',
             'alfabeto': 'O|G | A|G| | |O|C| | | A|G|O| L|C|A',
             'data': {'key': 'f', 'final': 7}},

        21: {'continuo': 't3|5t|5t3|35t||t5|72|37|75tt|57|25t',
             'alfabeto': 'HM|GH|GHM| GH|| G|OC|MO| GH |GO| GH',
             'data': {'key': 'f', 'final': 10}},

        22: {'continuo': '7|77|5|t|t3|44|4|55|t||t|55|70|22|02|00|22|7',
             'alfabeto': 'O|  |G|H| M|  | |G |H||H|G |OL|C |B |  |C |A',
             'data': {'key': 'f', 'final': 7}},

        23: {'continuo': '77|7000|27|72|40|27|55|5eee|05|550|2t|05', #split with next one b/c of key change
             'alfabeto': 'A | B  |CA| C|+B|CA|G | H  |BG|  B|EH|BG',
             'data': {'key': 'n', 'final':5}},

        24: {'continuo': 'tt|3333|5t|t5|t3|5t|55|55|70|00|77|27|55|tt|05||50|2t|05',
             'alfabeto': 'H |M   |GH| G|HM|GH|G |  |AB|  |OL|CA|G |H |BG||GB|EH|BG',
             'data': {'key': 'f', 'final': 5}},

        25: {'continuo': '99|99|00e|999|t92|7700|002249|42|452|49',
             'alfabeto': 'D |  |B  |I  |HIC|A B |B E FD|FE|FFE|FD',
             'data': {'key': 'n', 'final': 9}},
    }

Stefani_1623 = \
    {
        1: {'continuo': '7|7|7|97|7|22|9t79|2||9|97|e04|27',
            'alfabeto': 'A| | |DA| |C |IHAI|C||D| A|B  |CA',
            'data': {'key': 'n', 'final': 7}},

        2: {'continuo': '575|tt5|79|00|57|20|t|205|79|0|5||t|02|57|23|22|20|t5|t2|0t|72|2t0|72|75|790|05',
            'alfabeto': 'GOG|H G|OB|B |GO|CB|H|EBG|OD|B|G||H|LE|GO|CM|C |EB|HG|HC|BH|OC| HB|OC|AG|ODB| G',
            'data': {'key': 'f', 'final': 5}},

        3: {'continuo': '57|55t|35|tt|t7|54|57|024|577|209|t0|5||579|t7|995|79|22|72|70|57|0t9|t70|579|t0|5',
            'alfabeto': 'GO|G H|MG|H | O|GB|GA|B  | O |G  | B|G||   |HO|I G|OI|C |OC|OB|GA|B  |H B|G  | B|G',
            'data': {'key': 'f', 'final': 5}},

        4: {'continuo': '2|97|92|2t|57|02|27||79|tt|79|2|9t|3|5|t||5|5|70|07|7|70|2|7',
            'alfabeto': 'E|IO|IC| H|GO|LC| O|| D|H |OI|C|DH|M|G|H||G| |AB| O| | L|C|A',
            'data': {'key': 'f', 'final': 7}},

        5: {'continuo': '7|t|0|55|5|t|0|5||t|32|35|tt|5|3|35|tt||t|5|57|00|50|55|0|55',
            'alfabeto': 'G|H|B|G | |H|B|G||H|M | G|H |G|M| G|H || |G| A|B |PB|PH|B|G ',
            'data': {'key': 'f', 'final': 5}},

        6: {'continuo': '57|27|75|029|929|205|9t|05|55|54|570|007|72|77|757|292|22|922|05|5|7|32|5t|0|7|0|7|02|7|5|t0|5',
            'alfabeto': 'GO|CA| G|BEI| EI|EBG|DH|BG|  | +|GA |B O| C|A | GO|EIG|  |DE |BG| |O|M |GH|L|A|B|O|LC|A|G|HB|G',
            'data': {'key': 'f', 'final': 5}},

        7: {'continuo': '7|0|5|3|5t|t5|75|5t0|70|7|77|55|tt|t|3t|5|tt|t|t|9|2|4|5|5|t|00|5|7|7|0|00|72|7',
            'alfabeto': 'O|B|G|M|GH| G|OG| OL|AB|O|  |G |H | |MH|G|H | | |I|C|B|G| |H|BG| |O| |L|OL| C|A',
            'data': {'key': 'f', 'final': 7}},

        8: {'continuo': '2|9t|054|20|79|2||29|94|997|54|57|0|9t|t0|554|20t9|t79|2',
            'alfabeto': 'E|DH|BG |CB|OI|C|| D| F|I  |G | A|B|DH| B|G  |  H | OI|C',
            'data': {'key': 'n', 'final': 2}},

        9: {'continuo': '54|703|5t||t3|70|5t|02|75|9t|05',
            'alfabeto': 'GB|HM |GH|| P|AB|GH|BC|AG| H|BG',
            'data': {'key': 'f', 'final': 5}},

        10: {'continuo': '779|t246|772|9|702|7||557|959t|95|579|t235|t7|0230|2|7',
             'alfabeto': 'O D|HG  |O C|D|O C|A||G  |   H|BG| O |HMG |HA|B MB|C|A',
             'data': {'key': 'f', 'final': 7}},

        11: {'continuo': '2|2e95|40|t944|95|0127|999|79e1|12|6704|6796|7e02|4126|7e9|2',
             'alfabeto': 'E|    |FB| D F|DG|B E |I  |A C |BC| A B|C  D|A G |B E |A I|C',
             'data': {'key': 'n', 'final': 2}},

        12: {'continuo': '550|29|79t|05|50|07|20t7|92||9|6|7|052|402|49|9752t|9|12|49|50|29|25|t5|05',
             'alfabeto': 'G B|ED|ODH|BG| B| O|EBHO|IC||I|C|A|BGC|FBE|FI|D  E |I| E|FI|GB|EI|CG|HG|BG',
             'data': {'key': 'n', 'final':5}},

        13: {'continuo': 't|02|77|227|07|0|t5|72|7t|79|2||92|07|0t|5|02|7',
             'alfabeto': 'H|BC|O |C A|BA|B|HG|OC|OH|OI|C||OC|BA|BH|G|LC|A',
             'data': {'key': 'f', 'final': 7}},

        14: {'continuo': '050|570|95|70|0e|97|727|92|24|70',
             'alfabeto': 'BGB|GAB|DG|AB| H|DA| CA|IC| G|AB',
             'data': {'key': 'n', 'final':0}},

        15: {'continuo': '99|9|40|2|4|4||127|92|9|22|40|024|9',
             'alfabeto': 'D | |FB|C|F| ||BCA|IC|D|CA|FB| EF|I',
             'data': {'key': 'n', 'final':9}},

        16: {'continuo': '732t|355tt|29t95|792||79t0|2455|t795|42420|t9t0|570t9|700|79t02|30277',
             'alfabeto': 'OLCH|G  H |EDH G|OIC||ODHB|E+G |H IH|OICEB|HDHB|G A L|AB |O    |L CA ',
             'data': {'key': 'f', 'final':7}},

        17: {'continuo': '5577|9922|55t5|05||5799|7700|7670|27|5t5|0055|02t|05||5577|9922|55t5|05',
             'alfabeto': 'G A |I C |G HG|BG||  D |A B |O  L|GA|GHG|B G |BEH|BG||  A |I C |G HG|BG',
             'data': {'key': 'f', 'final': 5}},

        18: {'continuo': 't|9t|02|7|75|79|0|5|55|59|20|5|55|7t|79|2|22|70|57|05|t7|99|20|55|55|750|tt|57|20|2|7',
             'alfabeto': 'O|DH|BC|A| G|OD|B|G|  | D|EB|G|  |OH|OI|C|  |AB|GO|BG|HO|I |EB|G |  |O B|H |GO|CL|C|A',
             'data': {'key': 'f', 'final':7}},

        19: {'continuo': '7|72|2|25|970|0|2|4|99|9|4454|99|97|27|7|027',
             'alfabeto': 'A| C| | G|DAB|B|C|F|I |D|FGEF|D |A |CA| |BCA',
             'data': {'key': 'n', 'final':7}},

        20: {'continuo': '7|7|7|4|2|2|79|27|77|5|t90|5|54|20|022402|7',
             'alfabeto': 'A| | |F|E| |AI|CA|  |G|HBG| |AI|CB| E  BC|A',
             'data': {'key': 'n', 'final':7}},

        21: {'continuo': '777|02455|272|t022|276|7922|457023|0277||7023|579t|975323|405tt|t9t97|02455|32320|2277',
             'alfabeto': 'A  |B  G |O E| BC | OC|ODC | GAB  | CA ||OM  |G  H| O M  |G  H | DH  |B  G |M   B|C A ',
             'data': {'key': 'f', 'final':7}},

        22: {'continuo': '2|9|2|0|0|2|9|7|5|0|2|9||9|2|0|5|55|7t|79|22',
             'alfabeto': 'E|I|E|B| |E|D|A|G|B|E|I|| |E|B|G|  |OH|OI|C ',
             'data': {'key': 'n', 'final': 2}},

        23: {'continuo': '54|45|542|12|20t7|92||275|420|0t95|70|0e|92|49||92|729|t0|579t|05|5t|05',
             'alfabeto': 'GO| G|  E|BE|  HO|IC||EA |+ B|  G |AB|BC|IE|FI|| C|ABD|HB|GD H|BG| H|BG',
             'data': {'key': 'f', 'final':5}},

        24: {'continuo': '77|70|77e|402|77|70|774|524|9e|02|7|75|42|00|55|797|0e|00|242|7||79e|005|77|00|024|52|44|99|97|54|20|e0|57|9579|22|2|4|9|e0|2|7',
             'alfabeto': 'A | B|A  |+BC|A |AB|A +|GEF|IA|BC|A|G |+C|B |G |ADA|BA|B |C+C|A||ADH|B G|A |B | C+|GC| F|I |DA|G+|CB|HB|GA|IGOI|C |E|F|I| B|C|A',
             'data': {'key': 'n', 'final': 7}},

        25: {'continuo': '7|7|9|4|e|7|2|7|7|7|5|0|7|0|7|0|9|2|7|0|2|7|0|52|4|9|9|2|7|0|7|4|0|2|7|0|9|2|9|4|2|2|9|9|9|0|7|2|7',
             'alfabeto': 'A| |D|F|A| |C|A|A| |G|B|A|B|A|B|I|C|A|B|C|A|B|GA|B|I|D|C|A|B|A|+|B|C|A|B|I|C|D|F|C| |D| | |B|A|C|A',
             'data': {'key': 'n', 'final':7}},

        26: {'continuo': 't|92|29t|05|55|50|70|05|t35|t|t|30|07|0|05|5t|35t',
             'alfabeto': 'H|IC| DH|BG|  |GB|AB| G|HMG|H|H|M |BA|B| G| H|MGH',
             'data': {'key': 'f', 'final':10}},

        27: {'continuo': '000e|9754|92|0||0024|554|24575|4207|0',
             'alfabeto': 'B G |DA B|DC|B||    |G  |C  A |+ BA|B',
             'data': {'key': 'n', 'final': 0}},

        28: {'continuo': '54|520|5|79t|02|7|245|520|t|357|35|t||0975|302|7|99t0|2t0|5',
             'alfabeto': 'G | EB|G|ODH|BC|A|E G| EB|H|MGO|MG|H||BDO | BC|A|D H |  B|G',
             'data': {'key': 'f', 'final': 5}},

        29: {'continuo': '0249|e024|2e4|4002|7||42|00779|220|e049|024e|e029|e002|705|570',
             'alfabeto': 'BCFD|HBC+|GF | B C|A||  |B GAI|C  |  FD|B +A|  CD|  BC|ABG| AB',
             'data': {'key': 'n', 'final': 0}},

        30: {'continuo': '5|79t|00|5|57|9|5|54|57|00|9t|0|5||t|97|54|57|0|002|3579|t357|5t|77|70|2|77|55|5t|0|55',
             'alfabeto': 'G|ODH|B |G| O|I|G|  |GA|B |DH|B|G||H|DO|G | A|B|  L|    |HM  |GH|  |OL|C|A |G | H|B|G ',
             'data': {'key': 'f', 'final':5}},

        31: {'continuo': '79t3|357|54|20t0|2454|2457|957|02|4052|4670|2457|5420|t979|t79|20|t979|t029|t057|5420|t024|5702|302|7',
             'alfabeto': 'ODH |MGA|G |EBHB|E G |E GA|DGA|B |    |  O |C+G | +EB|H O |H I|C |HDOD|B HB|H   |G EB|H B |GO  |L C|A',
             'data': {'key': 'f', 'final': 7}},

        32: {'continuo': 't|tt|55|57|23|22|20t|97|555|523|02|776|79tt|t97|55|523|02|7',
             'alfabeto': 'H|  |GH| M|EG|C | BH|DO|D H| GB| G|A  |CADH|  O|G |E G|BC|A',
             'data': {'key': 'f', 'final':7}},

        33: {'continuo': 't|97|55|57|23|22|20t|97|555|523|02|775|79tt|t97|55|5232|032|7',
             'alfabeto': 'H| O|G | M|EB|C | BH|O |GO | MB| C|A  |CODH|  O|G | EME|BMC|A',
             'data': {'key': 'f', 'final': 7}},

        34: {'continuo': 't|97|55|57|23|22|20t|97|555|57|02|775|79t|t97|55|5232|02|7',
             'alfabeto': 'H|DM|G | O|GM|CE| BH|O |G  |M |BC|A H|MDH| DO|G |  M |BC|A',
             'data': {'key': 'f', 'final': 7}},

        35: {'continuo': 't|tt|55|57|23|22|20t|97|55|553|02|776|79tt|t97|55|523|02|7',
             'alfabeto': 'H|  |G | O| M|C |  H|GA|BG|  M|BC|A  | DHM|H O|GH|  M|BC|A',
             'data': {'key': 'f', 'final': 7}},

        36: {'continuo': '77|7492|772|245|54|2|77|7457|02|4057|957|0e|977|7457|97|5424|524|997|542|0457|00|e02|402|79|t755|542|0e|e02|402|7',
             'alfabeto': 'A |+ DC|A C| +G|CF|C|A | +GA|B |  GA|DGA|B | O |+ GA|DA|  C |GCF|I  |  B|  GA|B |ABC|+BC|A |  G |  A|BA| BC|+BC|A',
             'data': {'key': 'n', 'final': 7}},

        37: {'continuo': '7|2|0|735|tt|t579|tt|t|35|7355|t0|2302|77||79|t35|t5|70|2|7|5|33|20|t02|7',
             'alfabeto': 'O|E|L|OMG|H | GOD|H | |MG|OMG |HB|C MC|A ||OD|HMG|HG|OL|C|O|G|MH|CB|HBG|A',
             'data': {'key': 'f', 'final': 7}},

        38: {'continuo': '72|72|272|92|059|24|92|740|27||72|77|957|00|72|275|70|02|49|70|27',
             'alfabeto': 'AC|AC| OC|IC|BGD|CF|IC|AFB|CA|| C|A |DGA|B |AC|CAG|AB| C|FI|AB|CA',
             'data': {'key': 'n', 'final': 7}},

        39: {'continuo': '579|tt|02|7|9t0|55||335|5t|37|0|055|702|27||7|70|5t|t0|5',
             'alfabeto': 'GOD|H |BC|A|DHB|G ||M G|H |MA|B| G |ABC| A||O| B|GH| B|G',
             'data': {'key': 'f', 'final': 5}},

        40: {'continuo': '7|7|7|72|2|2|2e|02|7',
             'alfabeto': 'A| | | C|C| | A|BC|A',
             'data': {'key': 'n', 'final': 7}}


    }
