# 🛡️ Hệ thống Ví Web3 Python & Ký số ECDSA (Sepolia Testnet)

Dự án mô phỏng kiến trúc hoạt động cốt lõi của ví tiền điện tử phi tập trung, tập trung vào thuật toán chữ ký số Đường cong Elliptic (ECDSA), quản lý khóa ngoại tuyến (Offline Signing) và giao tiếp trực tiếp với Node mạng lưới Ethereum thông qua chuẩn JSON-RPC. 

Đây là đồ án nghiên cứu thuộc môn học Mật mã và An toàn Thông tin.

## 🚀 Quá trình phát triển (Changelog)

Dự án được xây dựng qua 2 giai đoạn để chứng minh sự tách biệt giữa lõi thuật toán và giao diện người dùng:

* **V1.0 - Core Terminal (`demo.py`):** Xây dựng lõi mật mã học. Thao tác 100% qua Command Line. Gạt bỏ hoàn toàn giao diện đồ họa để can thiệp trực tiếp vào dữ liệu thô (raw data), tự tay đóng gói từng byte dữ liệu và đẩy thẳng lên Node.
* **V2.0 - Web GUI Dashboard (`app.py`):** Nâng cấp lên giao diện quản trị Web App chuyên nghiệp bằng Streamlit. Tích hợp quản lý trạng thái (Session State), ghi nhận lịch sử thao tác theo thời gian thực và trích xuất chỉ số hiệu suất mật mã chi tiết (Thời gian ký ECDSA, Độ trễ mạng Broadcast).

## ⚙️ Yêu cầu hệ thống (Prerequisites)

* Python 3.8 trở lên.
* Trình quản lý gói `pip`.
* Có kết nối Internet ổn định để gọi API Node.

## 🛠️ Hướng dẫn cài đặt (Installation)

**1. Clone repository này về máy:**
```bash
git clone [https://github.com/chienprovjp/web3-wallet-guide.git](https://github.com/chienprovjp/web3-wallet-guide.git)
cd web3-wallet-guide
