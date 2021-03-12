red = int(input("Enter the red color:"))
green = int(input("Enter the green color"))
blue = int(input("Enter the blue color"))


# //Manera # 1 de convertir
hex_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
print('Hexadecimal valur using format:', hex_color)

# //Manera antigua de convertir
hexa_oldway = '#%02x%02x%02x' % (red, green, blue)
print("Your value using the old way:", hexa_oldway)

# Manera moderna de converit rgb a hexadecimal
rgb = [red, green, blue]
rgb_string = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
print('This is the coolest:', rgb_string)

