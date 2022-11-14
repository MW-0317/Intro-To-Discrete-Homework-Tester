import random
N = 1000000

def q5():
  r_count = 0
  n = N
  for i in range(1, n):
    red = ['r' for j in range(0, 20)]
    green = ['g' for j in range(0, 20)]
    full_ = red + green
  
    hand = []
  
    for j in range(0, 5):
      hand += full_.pop(random.randint(0, len(full_) - 1))
  
    # print(sorted(hand))
    r_count += sorted(hand) == ['g', 'g', 'r', 'r', 'r'
                                ] or sorted(hand) == ['g', 'g', 'g', 'r', 'r']

  print(r_count / n)



# Question 6: Arriving around 0.466... as the answer
def q6():
  r_count = 0
  n = N
  for i in range(0, n):
    # set_a = []
    # set_b = []
    # both_ = [set_a,set_b]
  
    # for i in range(1,16):
    #   random.choice(both_).append(i)
    all_n = list(range(1, 16))
    random.shuffle(all_n)
    set_a = all_n[0:8]
    # print(set_a)
    set_b = all_n[8:16]
    # print(set_b)
    r_count += ((1 in set_a and 2 in set_a) or (1 in set_b and 2 in set_b))
  
  print(r_count / n)

# Question 7: Arriving around 0.023... as the answer
def q7():
  r_count = 0
  n = N
  def check_dice(d):
    if 1 in dice or 5 in dice:
      return True
    elif dice == [2,2,3,3,4,4] or dice == [2,2,3,3,6,6] or dice == [3,3,4,4,6,6] or dice == [2,2,4,4,6,6]:
      return True
    elif any([dice.count(k) >= 3 for k in [2,3,4,6]]):
      return True
    return False
  
  for i in range(0, n):
    points = 0
  
    dice = []
    for j in range(0,6):
      dice.append(random.randint(1,6))
    dice = sorted(dice)
    
    r_count += 1 - int(check_dice(dice))
  print(r_count)
  print(r_count / n)