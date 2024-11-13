import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def image_to_svg_base64(image_path):
    # فتح الصورة باستخدام Pillow
    with Image.open(image_path) as img:
        buffer = BytesIO()
        img.save(buffer, format="PNG")  # نحفظ الصورة بصيغة PNG في الذاكرة
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        # إنشاء كود SVG مع الصورة كـ base64
        svg_data = f"""
        <svg xmlns="http://www.w3.org/2000/svg" width="{img.width}" height="{img.height}">
            <image href="data:image/png;base64,{img_base64}" width="{img.width}" height="{img.height}" />
        </svg>
        """
        return svg_data

# واجهة Streamlit
st.title("محول الصور إلى SVG")
st.write("قم بتحميل صورة وسيتم تحويلها إلى SVG يمكنك تنزيله.")

# تحميل الصورة
uploaded_file = st.file_uploader("اختر صورة", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # تحويل الصورة إلى SVG
    svg_data = image_to_svg_base64(uploaded_file)

    # عرض زر التنزيل
    svg_output = BytesIO(svg_data.encode("utf-8"))
    st.download_button(
        label="تنزيل الصورة بصيغة SVG",
        data=svg_output,
        file_name="image.svg",
        mime="image/svg+xml"
    )

    # عرض SVG في الصفحة
    st.write("معاينة الصورة المحوّلة إلى SVG:")
    st.image(uploaded_file, caption="الصورة الأصلية")
    st.markdown(f'<div>{svg_data}</div>', unsafe_allow_html=True)
