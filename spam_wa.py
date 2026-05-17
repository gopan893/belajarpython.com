import pyautogui
import time
import random

# === SETUP ===
target_message = "11112121121"
jumlah_pesan = 50
hapus_setelah_terkirim = True  # True = pesan dihapus setelah 5-10 detik

time.sleep(5)  # waktu pindah ke jendela chat

for i in range(jumlah_pesan):
    # Ketik pesan
    pyautogui.typewrite(target_message)
    pyautogui.press('enter')
    
    if hapus_setelah_terkirim:
        time.sleep(random.uniform(5, 10))  # tunggu sebentar biar kebaca dulu
        # Klik kanan pada pesan terakhir (koordinat perlu disesuaikan)
        pyautogui.click(x=875, y=933, button='right')
        time.sleep(0.5)
        # Tekan panah bawah 2x lalu enter untuk "Hapus untuk semua"
        pyautogui.press('down', presses=2, interval=0.2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')  # konfirmasi hapus
    
    # Jeda acak antara 3-7 detik
    time.sleep(random.uniform(3, 7))