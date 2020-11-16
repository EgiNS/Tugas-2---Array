menang = []
timA = input("Klub A: ")
timB = input("Klub B: ")
skorA, skorB =map(int, input("Pertandingan 1: ").split())
i = 2

while skorA >= 0 and skorB >= 0:
    if skorA > skorB:
        menang.append(timA)
    elif skorA < skorB:
        menang.append(timB)
    elif skorA == skorB:
        menang.append("Draw")
    skorA, skorB = map(int, input("Pertandingan {}: ".format(i)).split())
    i += 1
    if skorA < 0 or skorB < 0:
        k = 1
        for j in menang:
            print("Hasil {}: ".format(k), j)
            k += 1
        print("Pertandingan Selesai")
        break