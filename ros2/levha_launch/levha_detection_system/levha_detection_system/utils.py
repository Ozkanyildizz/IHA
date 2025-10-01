#!/usr/bin/env python3
import json
from datetime import datetime
import os

JSON_FILE = "levha_kayitlari.json"

def kayit_ekle(levha_adi, confidence, uzaklik, durum):
    now = datetime.now()
    kayit = {
        "tarih": now.strftime("%Y-%m-%d"),
        "saat": now.strftime("%H:%M:%S"),
        "levha": levha_adi,
        "confidence": confidence,
        "uzaklik": uzaklik,
        "durum": durum
    }

    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as f:
                content = f.read().strip() # İçeriği okunur ve baştaki/sondaki boşluklar (strip()) temizlenir.
                data = json.loads(content) if content else [] # json formatına dönüştür 
                if not isinstance(data, list): # JSON’dan okunan veri liste değilse (örneğin dict, string vs.) → güvenlik amacıyla data sıfırlanır → boş liste yapılır.
                    data = []
        except Exception:
            data = []
    else:
        data = []

    data.append(kayit)

    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

    # Dosyayı otomatik aç
    os.system(f"xdg-open {JSON_FILE}")  # Linux
    # os.startfile(JSON_FILE)           # Windows
