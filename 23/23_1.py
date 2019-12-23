from common import create_network

network = create_network()

result = None
while True and not result:
    for c in network:
        result = network[c].run(monitor_nat=True)
        if result:
            print(result)
            break
