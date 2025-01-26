# a = input()
# b = 'ads'
# count = 0
# print(a)
# compare = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# while True:
#     if a.find('nj') == True:
#         count +=1
#         a1 = a.replace('nj', '')
#     elif a.find('c=') == True:
#         count +=1
#         a2 = a1.replace('c=', '')
#     elif a.find('c-') == True:
#         count +=1
#         a3 = a2.replace('c-', '')
#     elif a.find('dz=') == True:
#         count +=1
#         a4 = a3.replace('dz=', '')
#     elif a.find('d-') == True:
#         count +=1
#         a5 = a4.replace('d-', '')
#     elif a.find('lj') == True:
#         count +=1
#         a6 = a5.replace('lj', '')
#     elif a.find('s=') == True:
#         count +=1
#         a7 = a6.replace('s=', '')
#     elif a.find('z=') == True:
#         count +=1
#         a8 = a7.replace('z=', '')
#         break
# print(a8)

# # last = len(list(a))
# # count += last
# # print(count)

# a = input()
# count = 0
# a_list = ()
# compare = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in compare:
#     if i in a:
#         count+=1
#         a_list.append(i)

# b = list(a)
# total = count + len(b)
# print(total)

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')
    print(word)# input 변수와 동일한 이름의 변수
print(len(word))