
import os
from MusicKen.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Selamat datang kembali di {PROJECT_NAME}

📀 {PROJECT_NAME} dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah.

📀 Assistant Music » @{ASSISTANT_NAME}\n\nKlik Next untuk instruksi**

""",

f"""
**PENGATURAN**
        
1. Jadikan bot sebagai admin
2. Mulai obrolan suara / VCG
3. Ketik `/userbotjoin` dan coba /play <nama lagu>
    × Jika Assistant Bot bergabung selamat menikmati musik, 
    × Jika Assistant Bot tidak bergabung Silahkan Tambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi
        
**» Daftar perintah :**
        
× /play <judul lagu> : Untuk Memutar lagu yang Anda minta melalui youtube
× /skip : Untuk Menskip pemutaran lagu ke Lagu berikutnya
× /pause : Untuk Menjeda pemutaran Lagu
× /resume : Untuk Melanjutkan pemutaran Lagu yang di pause
× /end : Untuk Memberhentikan pemutaran Lagu
× /userbotjoin - Untuk Mengundang asisten ke obrolan Anda (khusus admin)
× /admincache - Untuk MemRefresh admin list (khusus admin)  
"""
      ]
