""" 
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
store = []
n = 9
# Initialize store
for i in range(n):
    store.append([])
translate_column = {1: 0, 5: 1, 9: 2, 13: 3, 17: 4, 21: 5, 25: 6, 29: 7, 33: 8}
with open("input.txt") as f:
    # Set Initial state
    for i in range(8):
        line = f.readline()
        for j in range(1, 34, 4):
            if line[j] != " ":
                store[translate_column[j]].insert(0, line[j])
    f.readline()
    f.readline()  # Skip empty lines
    # Process moves
    lines = f.read().splitlines()
    for line in lines:
        data = line.split(" ")
        num_ = int(data[1])
        from_ = int(data[3]) - 1
        to_ = int(data[5]) - 1
        temp = []
        for i in range(num_):
            temp.insert(0, store[from_].pop())
        store[to_].extend(temp)
word = ""
for i in range(n):
    word += store[i].pop()
print("word:", word)
