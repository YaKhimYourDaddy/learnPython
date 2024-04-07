import itertools
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def circle_center(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def circle_radius(p1, p2):
    return distance(p1, p2) / 2

def points_within_circle(points, center, radius):
    for point in points:
        if distance(point, center) > radius:
            return False
    return True

def main():
    with open("fin.txt", "r") as fin:
        lines = fin.readlines()

    points = [tuple(map(float, line.strip().split())) for line in lines]

    pairs = []
    for pair in itertools.combinations(points, 2):
        center = circle_center(*pair)
        radius = circle_radius(*pair)
        if points_within_circle(points, center, radius):
            pairs.append(pair)

    if not pairs:
        print(0)
        return

    with open("fout.txt", "w") as fout:
        for pair in pairs:
            p1, p2 = pair
            if p1 < p2:  # Sắp xếp tọa độ của điểm trong cặp trước khi in ra
                fout.write(f"({p1[0]}, {p1[1]}), ({p2[0]}, {p2[1]})\n")
            else:
                fout.write(f"({p2[0]}, {p2[1]}), ({p1[0]}, {p1[1]})\n")

if __name__ == "__main__":
    main()
