import svgwrite

try:
    import cairosvg
    cairosvg_available = True
except ImportError:
    cairosvg_available = False

def create_palestine_flag(filename="palestine_flag", format="svg"):
    # الأبعاد والنسب الافتراضية للعلم
    width, height = 300, 200
    black, white, green, red = "#000000", "#FFFFFF", "#007A3D", "#CE1126"
    
    # إنشاء ملف SVG
    svg_filename = f"{filename}.svg"
    dwg = svgwrite.Drawing(svg_filename, size=(width, height))
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height / 3), fill=black))
    dwg.add(dwg.rect(insert=(0, height / 3), size=(width, height / 3), fill=white))
    dwg.add(dwg.rect(insert=(0, 2 * height / 3), size=(width, height / 3), fill=green))
    dwg.add(dwg.polygon(points=[(0, 0), (width * 0.4, height / 2), (0, height)], fill=red))
    dwg.save()
    
    print(f"تم إنشاء الملف بصيغة SVG: {svg_filename}")

    # Check if additional format conversion is requested
    if format.lower() == "svg":
        return  # Already saved as SVG, so no further conversion needed

    if not cairosvg_available:
        print("cairosvg library is not available. Only SVG format is supported.")
        return
    
    # Convert SVG to other formats if CairoSVG is available
    if format.lower() == "png":
        with open(svg_filename, "rb") as svg_file:
            cairosvg.svg2png(file_obj=svg_file, write_to=f"{filename}.png")
        print(f"تم إنشاء الملف بصيغة PNG: {filename}.png")
    
    elif format.lower() == "pdf":
        with open(svg_filename, "rb") as svg_file:
            cairosvg.svg2pdf(file_obj=svg_file, write_to=f"{filename}.pdf")
        print(f"تم إنشاء الملف بصيغة PDF: {filename}.pdf")
    else:
        print(f"Unsupported format '{format}'. Only 'svg', 'png', and 'pdf' are supported.")

# Example usage
create_palestine_flag(filename="palestine_flag", format="png")
