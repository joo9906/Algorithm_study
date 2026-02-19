import heapq


def solution(genres, plays):
    answer = []
    n = len(genres)
    playlist = {genres[i]: [0, []] for i in range(n)}

    for i in range(n):
        heapq.heappush(playlist[genres[i]][1], (plays[i], i))
        playlist[genres[i]][0] += plays[i]

    ranked_list = []
    for g, val in playlist.items():
        print(g, val)
        ranked_list.append((val[0], g))

    ranked_list.sort(reverse=True)

    for _, genre in ranked_list:
        for j in range(1, 3):
            answer.append(playlist[genre][1][-j][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))