def read_data():
    with open('input.txt') as data:
        return [int(c) for c in data.read().strip()]
