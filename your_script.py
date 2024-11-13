# your_script.py

import streamlit as st
import svgwrite
from PIL import Image
from wand.image import Image as WandImage
import os

# وظيفة لإنشاء علم فلسطين وحفظه بصيغة SVG
def create_palestine_flag(width, height, filename="palestine_flag"):
    black, white, green, red = "#000000", "#FFFFFF", "#007A3D", "#CE1126"


    # إنشاء ملف SVG
    svg_filename = f"{filename}.svg"
    dwg = svgwrite.Drawing(svg_filename, size=(width, height))
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height / 3), fill=black))
    dwg.add(dwg.rect(insert=(0, height / 3), size=(width, height / 3), fill=white))
    dwg.add(dwg.rect(insert=(0, 2 * height / 3), size=(width, height / 3), fill=green))
    dwg.add(dwg.polygon(points=[(0, 0), (width * 0.4, height / 2), (0, height)], fill=red))
    dwg.save()
    return svg_filename

# تحويل SVG إلى PNG أو PDF باستخدام Wand
def convert_svg_to_format(svg_filename, format):
    output_filename = f"{svg_filename.split('.')[0]}.{format}"
    with WandImage(filename=svg_filename) as img:
        img.format = format
        img.save(filename=output_filename)
    return output_filename

# واجهة Streamlit
st.title("مولد علم فلسطين")
st.write("اختر حجم العلم والصيغة التي ترغب بتنزيلها.")

# اختيارات حجم العلم
size = st.selectbox("اختر حجم العلم", [("صغير", (150, 100)), ("متوسط", (300, 200)), ("كبير", (600, 400))])
width, height = size[1]

# اختيار الصيغة
format = st.selectbox("اختر الصيغة", ["svg", "png", "pdf"])

# إنشاء العلم وحفظه
if st.button("إنشاء وتنزيل العلم"):
    svg_filename = create_palestine_flag(width, height)
    if format != "svg":
        # تحويل SVG إلى الصيغة المطلوبة
        output_filename = convert_svg_to_format(svg_filename, format)
    else:
        output_filename = svg_filename

    # عرض زر تحميل
    with open(output_filename, "rb") as file:
        btn = st.download_button(
            label=f"تنزيل العلم بصيغة {format.upper()}",
            data=file,
            file_name=output_filename,
            mime=f"image/{format}" if format == "png" else "application/pdf"
        )

    # حذف الملفات المؤقتة
    os.remove(svg_filename)
    if format != "svg":
        os.remove(output_filename)