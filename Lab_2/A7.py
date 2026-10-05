x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

color1_is_white = (x1 + y1) % 2 == 0
color2_is_white = (x2 + y2) % 2 == 0

same_color = ["NO", "YES"][color1_is_white == color2_is_white]
color_name = ["Black", "White"][color1_is_white]

print(same_color)
print([color_name, ""][same_color == "NO"])
