import random

N = 1000000


def h9q1():
  n = N
  r_count = 0
  for i in range(n):
    n1 = random.randint(1, 6)
    if n1 == 3:
      n2 = random.randint(1, 6)
      if (n1 + n2) % 2 == 0:
        r_count += 1
  print(r_count)
  print(r_count / N)


# Arriving at ~0.4990..., very close to half, but not exactly
def h9q5():
  n = N
  r_count = 0
  for i in range(n):
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    k = n1 + n2
    if k == 11 or k == 12:
      r_count += 1
      continue
    elif k == 2:
      continue
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    if k < n1 + n2:
      r_count += 1

  print(r_count)
  print(r_count / n)