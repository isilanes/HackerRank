import math
import os
import random
import re
import sys

def climbingLeaderboard(scores, alice):
    pre = [scores[0]]
    for score in scores[1:]:
        if score != pre[-1]:
            pre.append(score)
    
    alice_ranks = []
    i_score = 0
    i_alice = len(alice) - 1
    while True:
        alice_score = alice[i_alice]

        try:
            while alice_score < pre[i_score]:
                i_score += 1
        except IndexError:
            break

        alice_ranks.append(i_score+1)
        i_alice -= 1

        if i_alice < 0:
            break

    for _ in alice[:i_alice+1]:
        alice_ranks.append(len(pre)+1)
    
    return alice_ranks[::-1]


if __name__ == '__main__':
    with open("input08.txt") as f:
        scores_count = int(f.readline())
        scores = list(map(int, f.readline().rstrip().split()))
        alice_count = int(f.readline())
        alice = list(map(int, f.readline().rstrip().split()))
        result = climbingLeaderboard(scores, alice)
        print(result)

    with open("output08.txt") as f:
        output = []
        for line in f:
            output.append(int(line.strip()))

    print()
    print(output)

    print()
    print(result == output)
