"""
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""
with open("input.txt") as f:
    lines = f.read().splitlines()
score = 0
for item in lines:
    a, b = item.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    # First case
    if (
        int(a1) <= int(b1)
        and int(a2) >= int(b1)
        or int(a1) <= int(b2)
        and int(a2) >= int(b2)
    ):
        score += 1
    # Second case
    elif (
        int(b1) <= int(a1)
        and int(b2) >= int(a1)
        or int(b1) <= int(a2)
        and int(b2) >= int(a2)
    ):
        score += 1
print(score)
