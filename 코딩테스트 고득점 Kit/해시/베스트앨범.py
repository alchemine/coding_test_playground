# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from collections import defaultdict

def solution(genres, plays):
    table    = defaultdict(list)
    tot_play = defaultdict(int)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        table[genre].append((play, idx))
        tot_play[genre] += play

    answer = []
    for genre in sorted(tot_play, key=lambda k: -tot_play[k]):
        n_musics_in_genre = 0
        for play, idx in sorted(table[genre], key=lambda key: (-key[0], key[1])):  # max play, min idx
            answer.append(idx)
            n_musics_in_genre += 1
            if n_musics_in_genre == 2:
                break

    return answer

args = [
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
]
print(solution(*args))
