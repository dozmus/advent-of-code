from benchmark import benchmark
from custom_io import read_lines


def get_layers(pixels, width, height):
    layers = []

    while pixels:
        layer = []

        for i in range(width * height):
            layer.append(pixels.pop(0))

        layers.append(layer)

    return layers


@benchmark
def day8a(input, width, height):
    layers = get_layers(input.copy(), width, height)
    layer_with_least_zeroes = min(layers, key=lambda x: x.count(0))
    num_ones = layer_with_least_zeroes.count(1)
    num_twos = layer_with_least_zeroes.count(2)
    return num_ones * num_twos


@benchmark
def day8b(input, width, height):
    transparent = 2
    white = 1
    black = 0

    # compute final picture
    layers = get_layers(input.copy(), width, height)
    output = [transparent for i in range(width * height)]

    for i in range(width * height):
        for j in range(len(layers)):
            output[i] = layers[j][i]

            if output[i] != transparent:
                break

    # render
    s = '\n'

    for layer in get_layers(output, width, 1):
        for i in layer:
            if i == white:  # initially rendred white and black, picked best one since all output is white-black here
                s += str(i)
            else:
                s += ' '

        s += '\n'

    return s



if __name__ == '__main__':
    input = [int(i) for i in read_lines('data/day8.txt')[0]]
    width = 25
    height = 6

    print('day8a = %s' % day8a(input, width, height))  # 1584
    print('day8b = ' + day8b(input, width, height))  # KCGEC
