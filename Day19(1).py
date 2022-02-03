# I give up, idk how to do this and I cbb.    - Me (19-12-BIO2021)
# I DID IT. Actually wasn't as hard as I thought it'd be. - Me (29-12-BIO2021)
# This is definitely not an efficient method, took my laptop a couple mins to finish running it.
# However, I did do this entire thing on my own using a lot of the stuff I've learnt in the past month. :D


def getd(o, t):
    return ((o[0]-t[0])**2)+((o[1]-t[1])**2)+((o[2]-t[2])**2)


def findcommon(od, td):
    ci = []
    for i in range(len(od)):
        for j in range(len(td)):
            if od[i] == td[j]:
                ci.append(i)
    return ci


def findo(oc, rc):
    v = [oc[1][i] - oc[0][i] for i in range(3)]
    u = [rc[1][i] - rc[0][i] for i in range(3)]
    o = []
    for i in range(3):
        for j in range(3):
            for k in [-1, 1]:
                if v[i] == u[j]*k:
                    o.append([j, k])
    return o


c = []
scanners = []

s = input()
while True:
    s = input()
    if s == '': break
    c.append(list(map(int, s.split(','))))

d = [[getd(b, b_) for b_ in c] for b in c]


while True:
    s = input()
    if s == '': break
    ncoords = []
    while True:
        s = input()
        if s == '': break
        ncoords.append(list(map(int, s.split(','))))
    scanners.append(ncoords)

while scanners:
    print(len(scanners))
    for x in range(len(scanners)):
        ncoords = scanners[x]
        o = []
        for i in range(len(d)):
            for nc in ncoords:
                nd = [getd(nc, oc) for oc in ncoords]
                if len(findcommon(d[i], nd)) > 10:
                    o.append([c[i][:], nc[:]])
        if len(o) > 11:
            co = findo([o[2][0], o[3][0]], [o[2][1], o[3][1]])
            for i, [_, nc] in enumerate(o[:2]):
                o[i][1][:] = [nc[j] * k for j, k in co]
            pos = [o[0][0][i] - o[0][1][i] for i in range(3)]
            print(pos)
            dextension = []
            ncoords[:] = [[nc[j] * k for j, k in co] for nc in ncoords]
            ncoords[:] = [[nc[i] + pos[i] for i in range(3)] for nc in ncoords]
            ncoords_ = []
            for nc in ncoords:
                if nc not in c:
                    ncoords_.append(nc[:])
            ncoords[:] = ncoords_[:]
            for i in range(len(c)):
                for nc in ncoords:
                    d[i].append(getd(c[i], nc))
            c += ncoords_
            dextension = [[getd(nc, c_) for c_ in c] for nc in ncoords]
            d += dextension
            scanners.remove(ncoords)
            break
print(len(c))



# Example input:
# --- scanner 0 ---
# 404,-588,-901
# 528,-643,409
# -838,591,734
# 390,-675,-793
# -537,-823,-458
# -485,-357,347
# -345,-311,381
# -661,-816,-575
# -876,649,763
# -618,-824,-621
# 553,345,-567
# 474,580,667
# -447,-329,318
# -584,868,-557
# 544,-627,-890
# 564,392,-477
# 455,729,728
# -892,524,684
# -689,845,-530
# 423,-701,434
# 7,-33,-71
# 630,319,-379
# 443,580,662
# -789,900,-551
# 459,-707,401
#
# --- scanner 1 ---
# 686,422,578
# 605,423,415
# 515,917,-361
# -336,658,858
# 95,138,22
# -476,619,847
# -340,-569,-846
# 567,-361,727
# -460,603,-452
# 669,-402,600
# 729,430,532
# -500,-761,534
# -322,571,750
# -466,-666,-811
# -429,-592,574
# -355,545,-477
# 703,-491,-529
# -328,-685,520
# 413,935,-424
# -391,539,-444
# 586,-435,557
# -364,-763,-893
# 807,-499,-711
# 755,-354,-619
# 553,889,-390
#
# --- scanner 2 ---
# 649,640,665
# 682,-795,504
# -784,533,-524
# -644,584,-595
# -588,-843,648
# -30,6,44
# -674,560,763
# 500,723,-460
# 609,671,-379
# -555,-800,653
# -675,-892,-343
# 697,-426,-610
# 578,704,681
# 493,664,-388
# -671,-858,530
# -667,343,800
# 571,-461,-707
# -138,-166,112
# -889,563,-600
# 646,-828,498
# 640,759,510
# -630,509,768
# -681,-892,-333
# 673,-379,-804
# -742,-814,-386
# 577,-820,562
#
# --- scanner 3 ---
# -589,542,597
# 605,-692,669
# -500,565,-823
# -660,373,557
# -458,-679,-417
# -488,449,543
# -626,468,-788
# 338,-750,-386
# 528,-832,-391
# 562,-778,733
# -938,-730,414
# 543,643,-506
# -524,371,-870
# 407,773,750
# -104,29,83
# 378,-903,-323
# -778,-728,485
# 426,699,580
# -438,-605,-362
# -469,-447,-387
# 509,732,623
# 647,635,-688
# -868,-804,481
# 614,-800,639
# 595,780,-596
#
# --- scanner 4 ---
# 727,592,562
# -293,-554,779
# 441,611,-461
# -714,465,-776
# -743,427,-804
# -660,-479,-426
# 832,-632,460
# 927,-485,-438
# 408,393,-506
# 466,436,-512
# 110,16,151
# -258,-428,682
# -393,719,612
# -211,-452,876
# 808,-476,-593
# -575,615,604
# -485,667,467
# -680,325,-822
# -627,-443,-432
# 872,-547,-609
# 833,512,582
# 807,604,487
# 839,-516,451
# 891,-625,532
# -652,-548,-490
# 30,-46,-14
