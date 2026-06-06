import streamlit as st
import requests
from PIL import Image


API_URL = "http://localhost:8000/api/rock/lenet/inference"


st.set_page_config(
    page_title="Rock Crack Classifier",
    page_icon="🪨",
    layout="centered",
)

st.title("🪨 Rock Crack vs. No Crack Classifier")
st.write("Upload một tấm ảnh đá để xem mô hình dự đoán “crack” hay “not crack”.")
st.write("---")

#File uploader
uploaded_file = st.file_uploader(
    label="Chọn ảnh (PNG/JPG/JPEG)",
    type=["png", "jpg", "jpeg"]
)

# Khi có file, hiển thị preview và nút Predict
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Ảnh bạn đã chọn", use_column_width=True)

        if st.button("Predict"):
            with st.spinner("Đang gửi ảnh lên API và chờ kết quả..."):
                
                uploaded_file.seek(0)
                files = {
                    "file": (uploaded_file.name, uploaded_file.read(), uploaded_file.type)
                }
                try:
                    response = requests.post(API_URL, files=files)
                except requests.exceptions.RequestException as e:
                    st.error(f"Lỗi khi kết nối tới API: {e}")
                else:
                    if response.status_code == 200:
                        data = response.json()
                        prediction = data.get("prediction", "Unknown")
                        st.success(f"Kết quả dự đoán: **{prediction.upper()}**")
                    else:
                        try:
                            error_msg = response.json().get("error", response.text)
                        except Exception:
                            error_msg = response.text
                        st.error(f"API trả về lỗi (status {response.status_code}): {error_msg}")
    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh: {e}")
else:
    st.info("Vui lòng upload 1 file ảnh để dự đoán.")

st.write("---")
st.markdown(
    "Mô hình LeNet đã được train để phân biệt ảnh đá có vết nứt (crack) và không có vết nứt (no crack)."
)
