n = 76
k = 22
people = []
current = 1
poped = 0
for i in range(n):
    people.append(current)
    current += 1
while len(people) > 1:
        poped = (poped + k - 1) % len(people)
        people.pop(poped)
print(people[0])