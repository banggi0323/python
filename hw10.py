import os
import pickle

filepath= 'c:/data/score.bin'

def input_scores():
    print('[점수 입력]')
    scores = []
    i = 1
    while True:
        score = int(input(f'#{i}? '))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print('[점수 출력]')
    print('개인점수:', end=' ')
    for score in scores:
        print(score, end=' ')
    print()
    print(f'평균: {get_average(scores):.1f}')

def save_scores(scores):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)

def load_scores():
    print('[파일 읽기]')
    print()
    with open(filepath, 'rb') as file:
        return pickle.load(file)


scores = input_scores()
show_scores(scores)
save_scores(scores)
print()
r_scores = load_scores()
show_scores(r_scores)
