import svgwrite

def create_palestine_flag(filename="palestine_flag.svg"):
    # Create an SVG drawing with the flag's typical proportions (width-to-height ratio of 3:2)
    width, height = 300, 200
    dwg = svgwrite.Drawing(filename, profile="tiny", size=(width, height))
    
    # Define the colors of the Palestinian flag
    black = "#000000"
    white = "#FFFFFF"
    green = "#007A3D"
    red = "#CE1126"
    
    # Draw the black stripe
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height / 3), fill=black))
    
    # Draw the white stripe
    dwg.add(dwg.rect(insert=(0, height / 3), size=(width, height / 3), fill=white))
    
    # Draw the green stripe
    dwg.add(dwg.rect(insert=(0, 2 * height / 3), size=(width, height / 3), fill=green))
    
    # Draw the red triangle
    dwg.add(dwg.polygon(points=[(0, 0), (width * 0.4, height / 2), (0, height)], fill=red))
    
    # Save the SVG
    dwg.save()
    print(f"Palestinian flag SVG created: {filename}")

# Run the function to create the Palestinian flag SVG
create_palestine_flag()
