import sys

for i in sys.stdin:
    ab = i.split()
    a = [int(ab[0]), int(ab[1]), int(ab[2]), int(ab[3])]
    if len(a) != 4:
        exit()
    if int(ab[0]) <= int(ab[1]) and int(ab[2]) <= int(ab[3]):
        lead = sum(a)
        for j in sys.stdin:
            ab = j.split()
            b = [int(ab[0]), int(ab[1]), int(ab[2]), int(ab[3])]
            if len(b) != 4:
                exit()
            if int(ab[0]) <= int(ab[1]) and int(ab[2]) <= int(ab[3]):
                if lead > sum(b):
                    print("Gunnar")
                elif sum(b) > lead:
                    print("Emma")
                else:
                    print("Tie")
            exit()
    exit()
