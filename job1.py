
def draw_rectangle(width, height):
 
    print("|"+"-" * width+"|")
    for _ in range(height-2):
        print("|" + " " * (width) + "|")

    print("|"+"-" * width+"|")


draw_rectangle(10, 3)


