import streamlit as st
from web3 import Web3
from eth_account import Account
from datetime import datetime
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hệ thống Ví Web3 Professional", page_icon="🛡️", layout="wide")

# --- KHỞI TẠO BỘ NHỚ TRẠNG THÁI (SESSION STATE) ---
if 'history' not in st.session_state: st.session_state['history'] = []
if 'log_count' not in st.session_state: st.session_state['log_count'] = 0  
if 'wallet' not in st.session_state: st.session_state['wallet'] = None
if 'balance' not in st.session_state: st.session_state['balance'] = None
if 'tx_result' not in st.session_state: st.session_state['tx_result'] = None
if 'perf_metrics' not in st.session_state: st.session_state['perf_metrics'] = None

# --- HÀM GHI NHẬT KÝ ---
def add_log(action, detail, status="Thành công"):
    st.session_state['log_count'] += 1
    now = datetime.now().strftime("%H:%M:%S")
    st.session_state['history'].insert(0, {
        "STT": st.session_state['log_count'],
        "Thời gian": now, 
        "Thao tác": action, 
        "Chi tiết": detail, 
        "Trạng thái": status
    })

# --- CẤU HÌNH KẾT NỐI ---
ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/phWFQvXAE30bsWucx8Q22"
SENDER_PRIVATE_KEY = "0xa2862e643ff0f697e1ea6907c79cf6502769eb66ac1900ef67b1cfc4bae71d5e" 
SENDER_ADDRESS = "0xd1F5B4Ef211f3Ae3BF2C0F7963a4BA085f6c450D"

web3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

# ==========================================
# GIAO DIỆN CHÍNH
# ==========================================
st.title("🛡️ Dashboard Quản trị & Ký số Ví Ethereum")
st.markdown("---")

# TÁCH LỊCH SỬ RA THANH BÊN (SIDEBAR)
# TÁCH LỊCH SỬ RA THANH BÊN (SIDEBAR) ĐỂ DỄ THEO DÕI
with st.sidebar:
    st.header("📜 Lịch sử thao tác")
    st.markdown("Tiến trình xử lý được đánh số thứ tự:")
    if st.session_state['history']:
        for item in st.session_state['history']:
            # Sử dụng hàm .get() để chống lỗi sập ứng dụng nếu dữ liệu cũ không khớp
            icon = "🟢" if item.get('Trạng thái', 'Thành công') == "Thành công" else "🔴"
            stt = item.get('STT', 'Cũ')
            thoi_gian = item.get('Thời gian', '--:--:--')
            thao_tac = item.get('Thao tác', 'Không rõ')
            
            with st.expander(f"[Lần {stt}] {icon} {thoi_gian} - {thao_tac}"):
                st.write(f"**Chi tiết:** {item.get('Chi tiết', 'Trống')}")
                st.write(f"**Trạng thái:** {item.get('Trạng thái', 'Trống')}")
    else:
        st.info("Chưa có thao tác nào.")

# PHẦN A: NGUỒN TIỀN
st.header("A. THÔNG TIN NGUỒN TIỀN (Ví Gửi)")
with st.container(border=True):
    st.markdown(f"**Địa chỉ Ví Gửi cố định:** `{SENDER_ADDRESS}`")
    
    col_btn, col_metric = st.columns([1, 2])
    with col_btn:
        if st.button("🔍 Truy vấn Số dư Sổ cái"):
            try:
                balance_wei = web3.eth.get_balance(SENDER_ADDRESS)
                st.session_state['balance'] = float(web3.from_wei(balance_wei, 'ether'))
                add_log("Truy vấn", f"Số dư: {st.session_state['balance']:.5f} tETH")
            except Exception as e:
                add_log("Truy vấn", str(e), "Lỗi")
    
    with col_metric:
        if st.session_state['balance'] is not None:
            st.metric("Số dư khả dụng (tETH)", f"{st.session_state['balance']:.5f}")

st.markdown("<br>", unsafe_allow_html=True)

# PHẦN B: KHỞI TẠO & GIAO DỊCH
st.header("B. KHỞI TẠO & ĐÓNG GÓI GIAO DỊCH")
with st.container(border=True):
    
    st.subheader("1. Khởi tạo Ví Nhận (Receiver)")
    if st.button("✨ Sinh cặp khóa mới ngẫu nhiên"):
        Account.enable_unaudited_hdwallet_features()
        acct, _ = Account.create_with_mnemonic()
        st.session_state['wallet'] = {"address": acct.address, "key": web3.to_hex(acct.key)}
        st.session_state['tx_result'] = None 
        st.session_state['perf_metrics'] = None
        add_log("Tạo Ví", f"Sinh ví mới: {acct.address}")
    
    if st.session_state['wallet']:
        st.info(f"**Địa chỉ (Public Key):** `{st.session_state['wallet']['address']}`\n\n**Khóa bí mật (Private Key):** `{st.session_state['wallet']['key'][:20]}... [ĐÃ BẢO MẬT]`")
    
    st.markdown("---")

    st.subheader("2. Ký số & Phát sóng")
    amount = st.number_input("Nhập số lượng tETH:", value=0.001, step=0.0005, format="%.4f")
    
    if st.button("🚀 Thực hiện Ký số ECDSA & Broadcast", type="primary"):
        if not st.session_state['wallet']:
            st.error("❌ Vui lòng tạo ví nhận trước!")
        elif st.session_state['balance'] is None or st.session_state['balance'] < amount:
            st.error("❌ Số dư không đủ hoặc chưa ấn nút truy cập sổ cái!")
        else:
            try:
                nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)
                tx = {
                    'nonce': nonce, 'to': st.session_state['wallet']['address'],
                    'value': web3.to_wei(amount, 'ether'), 'gas': 21000,
                    'gasPrice': web3.eth.gas_price, 'chainId': 11155111
                }
                
                start_sign = time.perf_counter()
                signed_tx = web3.eth.account.sign_transaction(tx, SENDER_PRIVATE_KEY)
                end_sign = time.perf_counter()
                
                start_broadcast = time.perf_counter()
                tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
                end_broadcast = time.perf_counter()
                
                hash_hex = web3.to_hex(tx_hash)
                st.session_state['tx_result'] = hash_hex
                
                st.session_state['perf_metrics'] = {
                    'sign_time': (end_sign - start_sign) * 1000,
                    'broadcast_time': (end_broadcast - start_broadcast) * 1000
                }
                
                add_log("Giao dịch", f"Gửi {amount} tETH. Hash: {hash_hex}")
            except Exception as e:
                st.error(f"Lỗi hệ thống: {e}")
                add_log("Giao dịch", str(e), "Lỗi")
    
    if st.session_state['tx_result']:
        st.success("🎉 GIAO DỊCH ĐÃ ĐƯỢC ĐẨY LÊN MEMPOOL THÀNH CÔNG!")
        
        # ĐÃ VÁ LỖI: Chỉ in ra khi perf_metrics thực sự tồn tại
        if st.session_state['perf_metrics'] is not None:
            st.caption(f"⏱️ **Chỉ số hiệu suất:** Thời gian ký ECDSA: `{st.session_state['perf_metrics']['sign_time']:.4f} ms` | Độ trễ mạng: `{st.session_state['perf_metrics']['broadcast_time']:.2f} ms`")
        
        st.code(f"Mã băm (Tx Hash): {st.session_state['tx_result']}", language="text")
        st.markdown(f"**[👉 BẤM VÀO ĐÂY ĐỂ TRA CỨU TRÊN SỔ CÁI ETHERSCAN](https://sepolia.etherscan.io/tx/{st.session_state['tx_result']})**")