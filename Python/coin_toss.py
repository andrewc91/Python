import random

def coinToss():
    head_count = 0
    tail_count = 0
    attempt_count = 0

    for num in range(1,501):
        if random.randint(0,1) == 0:
            head_count += 1
            attempt_count += 1
            print('Attempt #{}: Throwing a coin...Its a head!...Got {} head(s) so far and {} tail(s) so far').format(attempt_count, head_count, tail_count)
        else:
            tail_count += 1
            attempt_count += 1
            print('Attempt #{}: Throwing a coin...Its a tail!...Got {} head(s) so far and {} tail(s) so far').format(attempt_count, head_count, tail_count)

coinToss()
