from common import read_data

sequence = 10000 * read_data()

offset = int("".join(str(i) for i in sequence[:7]))
sequence = sequence[len(sequence) // 2:]

for n in range(100):
    for i in range(1, len(sequence)):
        sequence[-1 - i] += sequence[-i]
    sequence = [abs(s) % 10 for s in sequence]

begin = offset - len(sequence)
print("".join(str(i) for i in sequence[begin:begin + 8]))
