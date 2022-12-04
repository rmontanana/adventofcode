"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

Your puzzle answer was 195292.
"""
with open("input.txt") as f:
    lines = f.readlines()
elfos = [0]
n_elfos = 0
max_food = 0
for item in lines:
    if item == "\n":
        if elfos[n_elfos] > max_food:
            max_food = elfos[n_elfos]
        n_elfos += 1
        elfos.append(0)
    else:
        elfos[n_elfos] += int(item)
elfos.sort(reverse=True)
print(sum(elfos[:3]))
