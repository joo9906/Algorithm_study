
def dnapw():
    S, P = map(int, input().split())
    DNA = input()
    DNA_list =[]
    DNA_list.extend(DNA)
    A, C, G, T = map(int, input().split())
    count_dna = {'A':0, 'C' : 0, 'G' : 0, 'T' : 0}
    cnt = 0

    for i in range(P):
        count_dna[DNA_list[i]] += 1

    if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
            cnt += 1

    for j in range(P, S):
        count_dna[DNA_list[j]] += 1
        count_dna[DNA_list[j-P]] -= 1
        if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
            cnt += 1

    return cnt

print(dnapw())