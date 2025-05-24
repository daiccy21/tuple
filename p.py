def semua_sama(t: tuple) -> bool:
    if len(t) <= 1:
        return True
    pertama = t[0]
    for elemen in t[1:]:
        if elemen != pertama:
            return False
    return True

tA = (90, 90, 90, 90)
print("tA =", tA)
print(semua_sama(tA))  