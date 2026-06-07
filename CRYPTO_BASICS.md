# 📖 Hướng Dẫn Cơ Bản: Nhập Môn Ví Tiền Điện Tử & Web3

Tài liệu này dành cho những người mới bắt đầu tìm hiểu về không gian tiền điện tử (Cryptocurrency). Trước khi đi sâu vào mã nguồn Python của dự án, chúng ta sẽ cùng phân biệt và thực hành tạo ví trên các ứng dụng phổ biến nhất hiện nay.

---

## 🧠 1. Kiến Thức Cốt Lõi: Sàn Tập Trung (CEX) vs. Ví Phi Tập Trung (DEX)

Trong thế giới Crypto, có một nguyên tắc vàng: **"Not your keys, not your coins"** (Không giữ khóa bí mật, không sở hữu tài sản). Dựa vào nguyên tắc này, các loại ví được chia làm 2 dạng chính:

### A. Sàn Giao Dịch Tập Trung (Custodial Wallet - ví dụ: Binance)
* **Bản chất:** Giống như một ngân hàng truyền thống. Bạn gửi tiền vào đó, Binance giữ **Khóa bí mật (Private Key)** của bạn. Bạn đăng nhập bằng Email/Mật khẩu.
* **Ưu điểm:** Rất dễ sử dụng, quên mật khẩu có thể xin cấp lại, hỗ trợ mua bán (P2P), giao dịch phái sinh cực nhanh.
* **Nhược điểm:** Nếu sàn sập hoặc chặn tài khoản, bạn sẽ mất tiền. Bạn không thực sự "nắm giữ" tài sản trên mạng lưới Blockchain.

### B. Ví Phi Tập Trung (Non-Custodial Wallet - ví dụ: MetaMask, Đồ án Python này)
* **Bản chất:** Bạn là người duy nhất nắm giữ **Khóa bí mật (Private Key) / Cụm từ phục hồi (Seed Phrase)**.
* **Ưu điểm:** Toàn quyền kiểm soát tài sản. Khả năng tương tác với các ứng dụng Web3 (DeFi, NFT). Không ai có thể đóng băng tài khoản của bạn.
* **Nhược điểm:** Mất Cụm từ phục hồi = Mất toàn bộ tiền mãi mãi. Không có tổng đài hỗ trợ hay nút "Quên mật khẩu".

---

## 🏦 2. Hướng dẫn tạo ví trên Binance (Dành cho Giao dịch & Đầu tư)

Binance là sàn giao dịch tiền điện tử lớn nhất thế giới, thích hợp để bạn dùng tiền VNĐ mua các đồng coin đầu tiên.

**Bước 1: Đăng ký tài khoản**
* Truy cập trang chủ [Binance.com](https://www.binance.com/) hoặc tải ứng dụng Binance trên App Store / Google Play.
* Nhấn **Đăng ký** bằng Email hoặc Số điện thoại.
* Tạo mật khẩu mạnh và xác thực mã OTP gửi về máy.

**Bước 2: Xác minh danh tính (KYC - Bắt buộc)**
* Theo luật phòng chống rửa tiền quốc tế, bạn cần xác minh danh tính.
* Chụp ảnh CCCD/Hộ chiếu mặt trước, mặt sau.
* Quét khuôn mặt (Face Recognition) theo hướng dẫn trên ứng dụng.
* *Thời gian duyệt thường mất từ 15 phút đến vài tiếng.*

**Bước 3: Mua coin bằng tiền pháp định (P2P)**
* Vào mục **Giao dịch P2P** (Peer-to-Peer).
* Chọn mua USDT, ETH hoặc BTC bằng cách chuyển khoản ngân hàng (VNĐ) cho người bán trên hệ thống. Sàn sẽ làm trung gian đảm bảo an toàn.

---

## 🦊 3. Hướng dẫn tạo ví Ethereum qua MetaMask (Dành cho Web3)

MetaMask là chiếc "hộ chiếu" phổ biến nhất để bạn bước vào thế giới Web3 và tương tác trực tiếp với mạng lưới Ethereum.

**Bước 1: Cài đặt Tiện ích mở rộng (Extension)**
* Truy cập [Metamask.io](https://metamask.io/).
* Tải tiện ích MetaMask cài đặt vào trình duyệt Chrome, Edge hoặc Cốc Cốc.

**Bước 2: Khởi tạo Ví Mới**
* Bấm vào biểu tượng con cáo 🦊 trên trình duyệt, chọn **"Tạo ví mới"** (Create a new wallet).
* Tạo một mật khẩu cục bộ (Mật khẩu này chỉ dùng để mở app trên máy tính hiện tại).

**Bước 3: Lưu trữ Cụm Từ Phục Hồi (QUAN TRỌNG NHẤT) 🚨**
* Màn hình sẽ hiện ra **12 từ tiếng Anh ngẫu nhiên** (Secret Recovery Phrase).
* **BẮT BUỘC:** Lấy giấy bút chép lại 12 từ này theo đúng thứ tự và cất vào két sắt. 
* *Tuyệt đối không chụp ảnh màn hình, không lưu vào Word/Note hay gửi qua Zalo. Bất kỳ ai có 12 từ này đều có thể lấy sạch tiền của bạn.*

**Bước 4: Nhận và Gửi Tiền**
* Ở trên cùng màn hình MetaMask, bạn sẽ thấy một dãy mã bắt đầu bằng `0x...` - Đây chính là **Địa chỉ ví (Public Key)** dùng để người khác chuyển tiền cho bạn.

---

## 🔗 4. Liên kết với Đồ án này (Tại sao lại cần code Python?)

Sau khi đã hiểu về ví MetaMask ở phần trên, bạn sẽ nhận ra một điều: **MetaMask đã làm ẩn đi quá trình toán học cực kỳ phức tạp bên dưới.** Nó gói gọn việc chuyển tiền thành một nút bấm "Xác nhận".

Đồ án Python trong kho lưu trữ này chính là một phiên bản "mổ xẻ" của ví MetaMask. Thay vì dùng giao diện kéo thả, hệ thống của chúng ta:
1. Tự sinh ra Cặp khóa bằng thuật toán.
2. Tự tính toán số dư thông qua việc giao tiếp bằng ngôn ngữ máy (JSON-RPC) với mạng lưới.
3. Tự lấy Private Key bọc quanh gói dữ liệu giao dịch để tạo ra **Chữ ký điện tử (Offline Signing)** trước khi đẩy lên Blockchain.

Việc hiểu và vận hành được mã nguồn của dự án này sẽ giúp bạn hiểu tận gốc bản chất cốt lõi của công nghệ chuỗi khối!
