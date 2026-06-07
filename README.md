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
```
2. (Tùy chọn) Tạo môi trường ảo Virtual Environment:

Bash
python -m venv venv

# Kích hoạt trên Windows:
venv\Scripts\activate

# Kích hoạt trên Mac/Linux:
source venv/bin/activate
3. Cài đặt các thư viện lõi:

Bash
pip install web3 eth-account streamlit
💻 Hướng dẫn sử dụng (Usage)
Trước khi chạy, hãy mở file mã nguồn và cấu hình lại biến SENDER_PRIVATE_KEY và SENDER_ADDRESS bằng ví thử nghiệm của riêng bạn.

Cách 1: Chạy phiên bản Terminal lõi (V1)
Mở terminal và gõ lệnh:

Bash
python demo.py
Giao diện dòng lệnh sẽ yêu cầu bạn nhấn Enter lần lượt để đi qua 3 bước: Tạo ví -> Kiểm tra sổ cái -> Ký số giao dịch.

Cách 2: Chạy phiên bản Giao diện Web (V2 - Khuyên dùng)
Mở terminal và khởi động server Streamlit:

Bash
streamlit run app.py
Trình duyệt sẽ tự động mở trang Dashboard tại địa chỉ http://localhost:8501. Giao diện được chia làm 2 khối quản trị Nguồn tiền và Giao dịch độc lập, tích hợp xuất báo cáo chỉ số hiệu năng tự động.

🔒 Tuyên bố Bảo mật
Mã nguồn này được viết vì mục đích giáo dục và thử nghiệm trên mạng lưới Sepolia Testnet. Không bao giờ hard-code Private Key thật chứa tài sản Mainnet vào bên trong mã nguồn.


Sau khi bạn lưu lại (Commit), GitHub sẽ render các khối code (
