from web3 import Web3
from eth_account import Account
import time

Account.enable_unaudited_hdwallet_features()

# ==========================================
# 1. ĐIỀN THÔNG TIN CỦA BẠN VÀO 3 DÒNG DƯỚI ĐÂY
# ==========================================
ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/phWFQvXAE30bsWucx8Q22"

# Đã thêm chữ "0x" vào đầu Private Key của bạn
SENDER_PRIVATE_KEY = "0xa2862e643ff0f697e1ea6907c79cf6502769eb66ac1900ef67b1cfc4bae71d5e" 

SENDER_ADDRESS = "0xd1F5B4Ef211f3Ae3BF2C0F7963a4BA085f6c450D"
# ==========================================

web3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

print("="*60)
print("🚀 HỆ THỐNG MÔ PHỎNG VÍ ETHEREUM - MẠNG SEPOLIA 🚀")
print("="*60)
if web3.is_connected():
    print("[+] Kết nối thành công đến Node Alchemy!")
else:
    print("[-] Lỗi kết nối API!")
    exit()

# BƯỚC 1: TẠO VÍ NHẬN
input("\n[Enter] Bước 1: Khởi tạo một ví nhận tiền (Receiver Wallet) mới...")
acct, mnemonic = Account.create_with_mnemonic()
RECEIVER_ADDRESS = acct.address
print(f"   -> Địa chỉ ví (Public Key): {RECEIVER_ADDRESS}")
print(f"   -> Khóa bí mật (Private): {web3.to_hex(acct.key)[:10]}...[ĐÃ CHE]")

# BƯỚC 2: KIỂM TRA SỐ DƯ
input("\n[Enter] Bước 2: Truy vấn số dư của ví gửi tiền...")
balance_wei = web3.eth.get_balance(SENDER_ADDRESS)
balance_eth = web3.from_wei(balance_wei, 'ether')
print(f"   -> Địa chỉ ví gửi: {SENDER_ADDRESS}")
print(f"   -> Số dư hiện tại: {balance_eth} tETH")

# BƯỚC 3: GIAO DỊCH
input("\n[Enter] Bước 3: Ký số ECDSA và Phát sóng giao dịch (Chuyển 0.001 tETH)...")

if balance_eth < 0.001:
    print("   [-] THẤT BẠI: Ví của bạn không đủ 0.001 tETH. Hãy lên Faucet xin thêm!")
    exit()

try:
    nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)
    tx = {
        'nonce': nonce,
        'to': RECEIVER_ADDRESS,
        'value': web3.to_wei(0.001, 'ether'),
        'gas': 21000,
        'gasPrice': web3.eth.gas_price,
        'chainId': 11155111
    }

    print("   [*] Đang ký giao dịch (Offline Signing)...")
    signed_tx = web3.eth.account.sign_transaction(tx, SENDER_PRIVATE_KEY)
    time.sleep(1)

    print("   [*] Đang phát sóng (Broadcast) lên mạng lưới...")
    # Đã sửa rawTransaction thành raw_transaction cho tương thích Web3 v6
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    print("\n[+] GIAO DỊCH ĐÃ ĐƯỢC ĐẨY LÊN MEMPOOL THÀNH CÔNG!")
    print(f"👉 Mã băm (Tx Hash): {web3.to_hex(tx_hash)}")
    print("Hãy copy mã này và tra cứu trên: https://sepolia.etherscan.io/")

except ValueError as e:
    print(f"\n[-] LỖI BLOCKCHAIN: {e}")
    print("👉 Gợi ý: Có thể ví của bạn đủ 0.001 tETH nhưng không đủ tiền trả phí Gas mạng. Hãy đảm bảo số dư lớn hơn 0.005 tETH.")
except Exception as e:
    print(f"\n[-] LỖI DỮ LIỆU: {e}")
    print("👉 Gợi ý: Lỗi xảy ra trong quá trình ký. Hãy kiểm tra lại Private Key.")