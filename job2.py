h = int(input("Entrez la hauteur du triangle : "))

def draw_triangle(height):
    print(" " * (height - 1) + "_")
    for i in range(1, height - 1):       
        space_left=" "+(height-1 -i)
        space_in=" "+(2*i-1)
        print(space_left+"/"+space_in+"\\")

    if height > 1:
        print("/" + "_" * (2 * height - 3) + "\\")
        

draw_triangle(h)