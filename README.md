# 🛡️ Hệ thống Ví Web3 Python & Ký số ECDSA (Sepolia Testnet)

Dự án mô phỏng kiến trúc hoạt động cốt lõi của ví tiền điện tử phi tập trung, tập trung vào thuật toán chữ ký số Đường cong Elliptic (ECDSA), quản lý khóa ngoại tuyến (Offline Signing) và giao tiếp trực tiếp với Node mạng lưới Ethereum thông qua chuẩn JSON-RPC. 

Đây là đồ án nghiên cứu thuộc môn học Mật mã và An toàn Thông tin.
---

## 🆕 Tài liệu dành cho người mới bắt đầu (Crypto Basics)

Nếu bạn chưa từng tiếp xúc với thị trường tiền điện tử hoặc muốn tìm hiểu cách tạo ví trên các ứng dụng đại chúng, hãy đọc qua cuốn cẩm nang hướng dẫn chi tiết của dự án tại đây:

👉 **[ĐỌC CẨM NANG: Hướng dẫn cơ bản về Ví Crypto & Binance/MetaMask](CRYPTO_BASICS.md)**

---

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
python -m streamlit run app.py
Trình duyệt sẽ tự động mở trang Dashboard tại địa chỉ http://localhost:8501. Giao diện được chia làm 2 khối quản trị Nguồn tiền và Giao dịch độc lập, tích hợp xuất báo cáo chỉ số hiệu năng tự động.

🔒 Tuyên bố Bảo mật
Mã nguồn này được viết vì mục đích giáo dục và thử nghiệm trên mạng lưới Sepolia Testnet. Không bao giờ hard-code Private Key thật chứa tài sản Mainnet vào bên trong mã nguồn.
---

## ☁️ Hướng dẫn Triển khai lên Đám mây (Cloud Deployment)

Nếu bạn muốn tự đưa ứng dụng này lên mạng Internet để truy cập từ bất kỳ đâu (điện thoại, máy tính khác) mà không tốn chi phí thuê máy chủ, bạn có thể sử dụng **Streamlit Community Cloud**.

**Bước 1: Fork kho lưu trữ này**
Nhấn vào nút **Fork** ở góc trên cùng bên phải của trang GitHub này để tạo một bản sao dự án về tài khoản GitHub của riêng bạn.

**Bước 2: Chuẩn bị tệp thư viện**
Hệ thống đã có sẵn tệp `requirements.txt` với cấu hình tương thích vạn năng (không fix cứng phiên bản để tránh xung đột trên Cloud):
```text
web3
eth-account
streamlit
```
Bước 3: Kết nối và Triển khai (Deploy)

Truy cập vào Streamlit Community Cloud và đăng nhập bằng tài khoản GitHub của bạn.

Nhấn nút New app (Tạo ứng dụng mới).

Điền các thông tin cấp phép trỏ về kho chứa của bạn:

Repository: [Tên-GitHub-của-bạn]/web3-wallet-guide

Branch: main

Main file path: app.py

Nhấn Deploy!

Hệ thống sẽ tự động cấp phát máy chủ, cài đặt thư viện phần mềm và khởi chạy. Quá trình này mất khoảng 1-2 phút. Sau khi hoàn tất, bạn sẽ nhận được một đường link Public (ví dụ: https://your-app-name.streamlit.app) để sử dụng và chia sẻ với mọi người.
🆕 Dành cho người mới bắt đầu: Nếu bạn chưa từng tiếp xúc với tiền điện tử, hãy đọc qua cuốn cẩm nang nhỏ của dự án: 👉 Hướng dẫn cơ bản về Ví Crypto & Binance/MetaMask

⚠️ Lưu ý Bảo mật khi Deploy:
Môi trường Cloud là môi trường công khai. Nếu bạn có ý định phát triển tiếp để giao dịch tiền thật (Mainnet), tuyệt đối không để Private Key dạng text trong mã nguồn. Hãy sử dụng tính năng Secrets Management (Quản lý biến môi trường bảo mật) của nền tảng Streamlit Cloud để lưu trữ khóa.
