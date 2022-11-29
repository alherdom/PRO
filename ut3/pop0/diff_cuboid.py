# ********************
# CUBOIDES Y VOLÚMENES
# ********************


def run(cuboid1: list, cuboid2: list) -> float:
    vol1 = cuboid1[0]
    vol2 = cuboid2[0]
    for values1, values2 in zip(cuboid1[1:], cuboid2[1:]):
        vol1 *= values1
        vol2 *= values2
    vol_diff = abs(vol1 - vol2)
    return vol_diff


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])
