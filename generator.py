import json
import random
import argparse


def generate_instance(num_requests):
    instance = {
        'InstanceName': 'vrplc9_5_10_s1',
        'T': 3450,
        'R': 20,
        'Q': 15,
        'C': 10,
        'locations': {
            'L-D': [0, 0],
            'L-1': [-299, 253],
            'L-2': [207, -161],
            'L-3': [-345, 184],
            'L-4': [-368, -345],
            'L-5': [-184, 345]
        },
        'requests': {},
    }

    for i in range(1, num_requests + 1):
        a=random.randint(200, 2500)
        s=random.randint(200,500)
        b=a+random.randint(s,1500)
        request = {
            'R-' + str(i): {
                'L': random.choice(list(instance['locations'].keys())[1:]),
                'A': a,
                'B': b,
                'S': s,
                'Q': random.randint(1, 5)
            }
        }
        instance['requests'].update(request)

    return instance

if __name__ == '__main__':
# Generate instance with 150 requests
    parser = argparse.ArgumentParser(description='Generate a vehicle routing problem')
    parser.add_argument('-s', '--seed', help="The seed used for randomisation", default=0, type=int)
    parser.add_argument('-r', '--no_reqs', help="The number of jobs on the instance", default=60, type=int)
    parser.add_argument('instance', help='Path to instance that is created', type=str)
    args = parser.parse_args()

    random.seed(args.seed)
    #num_requests = 50
    instance = generate_instance(args.no_reqs)
    print(instance)
    #filename = 'instance.txt'
    with open(args.instance, 'w') as file:
        file.write("InstanceName: {}\n".format(instance['InstanceName']))
        file.write("T: {}\n".format(instance['T']))
        file.write("R: {}\n".format(instance['R']))
        file.write("Q: {}\n".format(instance['Q']))
        file.write("C: {}\n\n".format(instance['C']))

        file.write("      L         X         Y\n")
        for location, coordinates in instance['locations'].items():
            file.write("{:>8}   {:>8}   {:>8}\n".format(location, coordinates[0], coordinates[1]))
        file.write("\n")

        file.write("      R         L         A         B         S         Q\n")
        for request, details in instance['requests'].items():
            file.write("{:>8}   {:>8}   {:>8}   {:>8}   {:>8}   {:>8}\n".format(
                request, details['L'], details['A'], details['B'], details['S'], details['Q']))

    print("Instance saved to", args.instance)
