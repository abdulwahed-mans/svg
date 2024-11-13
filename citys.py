import streamlit as st
import svgwrite
from io import BytesIO

def create_cityscape(width=500, height=300, num_houses=3, num_trees=3, sun_radius=30):
    # إنشاء مساحة العمل بصيغة SVG
    dwg = svgwrite.Drawing(size=(width, height))
    
    # إضافة الأرضية
    dwg.add(dwg.rect(insert=(0, height * 0.6), size=(width, height * 0.4), fill="green"))

    # إضافة الشمس
    sun_position = (width * 0.8, height * 0.2)
    dwg.add(dwg.circle(center=sun_position, r=sun_radius, fill="yellow"))

    # إضافة المنازل
    house_width, house_height = 50, 40
    for i in range(num_houses):
        x = 30 + i * (house_width + 20)
        y = height * 0.6 - house_height
        dwg.add(dwg.rect(insert=(x, y), size=(house_width, house_height), fill="blue"))
        
        # سقف المنزل
        roof_points = [(x, y), (x + house_width / 2, y - 20), (x + house_width, y)]
        dwg.add(dwg.polygon(points=roof_points, fill="brown"))

    # إضافة الأشجار
    tree_width, tree_height = 15, 30
    for i in range(num_trees):
        x = 200 + i * (tree_width + 30)
        y = height * 0.6 - tree_height
        # جذع الشجرة
        dwg.add(dwg.rect(insert=(x + 5, y + tree_height), size=(5, 15), fill="saddlebrown"))
        # أوراق الشجرة
        dwg.add(dwg.circle(center=(x + tree_width / 2, y + tree_height), r=tree_width, fill="darkgreen"))

    return dwg

# واجهة Streamlit
st.title("مولد مدينة بسيطة")
st.write("يمكنك تخصيص عناصر المدينة من الأسفل.")

# إعدادات المدينة
width = st.slider("عرض المدينة", 400, 800, 500)
height = st.slider("ارتفاع المدينة", 300, 600, 300)
num_houses = st.slider("عدد المنازل", 1, 5, 3)
num_trees = st.slider("عدد الأشجار", 1, 5, 3)
sun_radius = st.slider("حجم الشمس", 20, 50, 30)

# إنشاء المدينة بناءً على الإعدادات
cityscape = create_cityscape(width, height, num_houses, num_trees, sun_radius)

# حفظ الرسم في الذاكرة للتحميل
svg_output = BytesIO(cityscape.tostring().encode("utf-8"))

# عرض زر تحميل
st.download_button(
    label="تنزيل المدينة بصيغة SVG",
    data=svg_output,
    file_name="cityscape.svg",
    mime="image/svg+xml"
)
