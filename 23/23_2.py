from common import create_network

network = create_network(nat=True)

while True:
    for c in network:
        result = network[c].run()
    if result:
        print(result)
        break
