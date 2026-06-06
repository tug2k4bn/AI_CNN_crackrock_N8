# 🪨 Crack Detection on Natural Stone Surface using CNN (LeNet)

## 📌 Mô tả dự án

Dự án này thực hiện bài toán **phân loại vết nứt (crack detection)** trên bề mặt đá tự nhiên (như granite, marble) bằng cách sử dụng mô hình **Convolutional Neural Network (CNN)**. Cụ thể, nhóm lựa chọn kiến trúc **LeNet** – một mô hình nhẹ, đơn giản nhưng hiệu quả – để huấn luyện và đánh giá trên bộ dữ liệu **Concrete-Crack Image Dataset**.

Dự án bao gồm các bước:
- Tiền xử lý và tăng cường dữ liệu
- Xây dựng và huấn luyện mô hình LeNet bằng TensorFlow
- Triển khai mô hình qua API RESTful sử dụng **FastAPI**
- Xây dựng giao diện người dùng với **Streamlit**

---

## 🧠 Kiến trúc mô hình

Mô hình LeNet bao gồm:

- 2 lớp Convolution (ReLU)  
- 2 lớp Pooling  
- 2 lớp Fully Connected  
- 1 lớp đầu ra Sigmoid (phân loại nhị phân)


# Cài đặt thư viện cần thiết
pip install -r requirements.txt
🚀 HƯỚNG DẪN SỬ DỤNG
bash
Sao chép
Chỉnh sửa
# Huấn luyện mô hình (nếu cần)
python train_model.py


> ✅ Accuracy trên tập test: **98.6%**


Giao diện trực quan, thao tác dễ dàng

Thời gian nhận diện nhanh, kết quả chính xác

👥 THÀNH VIÊN
NGÔ XUÂN TÙNG

ĐOÀN VĂN CHƯƠNG

NGUYỄN QUANG ĐẠT

ĐỖ HẢI ĐĂNG

---

