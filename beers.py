

def buy(lista):
    results = [[], []]
    for i in range(len(lista)):
        results[0].append(0)
        results[1].append([0, 0, 0])
    marka = input("dose marka 1-6: ")
    case = input("dose syskeyasia 1-3: ")
    while marka != -111 and marka != -111:
        results[0][marka-1] += 1
        results[1][marka-1][case-1] += 1
        marka = input("dose marka 1-6: ")
        if marka != -111:
            case = input("dose syskeyasia 1-3: ")
    return results


def nothing(lista, l2):
    pos = []
    for i in range(len(lista[0])):
        for j in range(3):
            if lista[1][i][j] == 0:
                pos.append([i, j])
    names = []
    for k in range(len(pos)):
        name = l2[pos[k][0]]
        typee = pos[k][1]
        if typee == 0:
            typee = "paketo twn 4"
        elif typee == 1:
            typee = "paketo twn 6"
        else:
            typee = "paketo twn 8"

        names.append([name,typee])
    return names

def calc(lista):
    gains = []
    for l in range(len(lista[0])):
        total = 0
        for m in range(3):
            total += lista[1][l][m]
        gains.append(total)
    return gains


supermarket = []


for i in range(3):
    beername = raw_input("Give beer name: ")
    supermarket.append(beername)


res = buy(supermarket)
cbeer = res[0]
ctypes = [0, 0, 0]


for i in range(len(res[0])): #res[[2,3,5],[[1,1,2],[1,1,2],[1,1,2]]]
    for j in range(3):
        ctypes[j] += res[1][i][j]

onomata = nothing(res, supermarket)

profit = calc(res)

print res, profit
for i in range(len(res[0])):
    c = 4
    for j in range(3):
        print "Poylhse type / size",c,":", supermarket[i],res[1][i][j]
        c += 2
print "Poulhse 4/6/8 sizes: ", ctypes
print "Den poylhsan ta Name/Size katholoy mphres: ", onomata
print "Poulhse A/B/C mphres: ", profit
