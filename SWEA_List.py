T = int(input())



def Worker():
    h, w = map(int, input().split())
    worker_list_ext = []
    final_list = {}
    num = 0

    for _ in range(h):
        worker_list = list(map(int, input().split()))
        worker_list_ext.extend(worker_list)
        for i in range(len(worker_list)):
            final_list[worker_list[i]] = 0

    for k in range(len(worker_list_ext)):
        if worker_list_ext[k] in final_list.keys():
            final_list[worker_list_ext[k]] += 1

    final_key = sorted(list(final_list.keys()))
    for i in range(len(final_key)):
        if num < final_list[final_key[i]]:
            num = final_list[final_key[i]]
            worker = final_key[i]
            continue

        if num == final_list[final_key[i]]:
            worker = final_key[i]

    return worker, worker_list_ext, final_list, max(final_list)


for n in range(1, T + 1):
    print(f'#{n} {Worker()}')