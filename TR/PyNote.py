###@alierenkose


from datetime import datetime, date, timedelta
import os


while True:
    disk = input("Hangi diskte kullanmak istiyorsun (C , D vb.): ")

    disk_yolu = f"{disk}:\\"
    var_mi = os.path.exists(disk_yolu)
    if var_mi == False:
        print("Disk Bulunamadı!")
    else:
        break

database_folder = f"{disk}:/PyNote"

if not os.path.exists(database_folder):
    os.makedirs(database_folder)

database = f"{disk}:/PyNote/Database.txt"
version = "2.11"

if not os.path.isfile(database):
    with open(database, "w") as file:
        tarih = datetime.today().strftime("%d.%m.%Y")
        not_icerik = f"Pynote {version} e hoş geldin!"
        file.write(f"{tarih}: {not_icerik}\n")
        print(f"Pynote {version} e hoş geldin!")


def not_sil():
    with open(database, "r") as file:
        notlar = file.readlines()
        if notlar:
            print("Notlar:")
            for i, not_ in enumerate(notlar, 1):
                print(f"{i}. {not_}")
            secim = input("Silmek istediğiniz notun numarasını girin (0: Geri dön): ")
            if secim.isdigit():
                secim = int(secim)
                if 0 < secim <= len(notlar):
                    with open(database, "w") as file:
                        for i, not_ in enumerate(notlar, 1):
                            if i != secim:
                                file.write(not_)
                    print(f"{secim}. not silindi.")
                elif secim == 0:
                    print("İşlem iptal edildi.")
                else:
                    print("Geçersiz seçim.")
            else:
                print("Geçersiz seçim.")
        else:
            print("Henüz not eklenmedi.")


def not_ekle():
    while True:
        tarih_str = input("Notun son uygulanması gereken tarih (gg.aa.yyyy): ")
        try:
            tarih = datetime.strptime(tarih_str, "%d.%m.%Y")
            break
        except ValueError:
            print("Hatalı tarih formatı! Lütfen gg.aa.yyyy şeklinde girin.")

    not_icerik = input("Not içeriği: ")
    with open(database, "a") as file:
        file.write(f"{tarih_str}: {not_icerik}\n")
    print("Not başarıyla kaydedildi.")


def notlari_goster():
    with open(database, "r", encoding="ansi") as file:
        notlar = file.readlines()
    if not notlar:
        print("Henüz not eklenmedi.")
    else:
        print("Notlarınız:\n")
        today = date.today()
        notlar.sort(key=lambda x: datetime.strptime(x.split(": ")[0], "%d.%m.%Y").date())
        for not_ in notlar:
            not_bilgileri = not_.split(": ")
            tarih_str = not_bilgileri[0]
            not_icerik = not_bilgileri[1].strip()
            tarih = datetime.strptime(tarih_str, "%d.%m.%Y").date()
            
            if tarih < today:
                print("(Tarihi Geçmiş!) ", end="")
            elif tarih == today:
                print("(Bugün!) ", end="")
            elif tarih <= today + timedelta(days=365):
                kalan_gun = (tarih - today).days
                print(f"(Son {kalan_gun} gün kaldı!) ", end="")
            else:
                kalan_gun = (tarih - today).days
                print(f"(Son {kalan_gun} gün kaldı!) ", end="")
                
            print(not_)


def notlari_hepsini_sil():
    while True:
        with open(database, "r", encoding="ansi") as file:
            notlar = file.readlines()
            if not notlar:
                print("Henüz not eklenmedi.")
                break
            else:
                secim = input("Tüm notları silmek istediğinize emin misiniz(E/H): ").upper()
                if secim == "E":
                    with open(database, "w") as file:
                        file.write("")
                    print("Tüm notlar silindi!")
                    break
                elif secim == "H":
                    print("Seçim iptal edildi!")
                    break
                else:
                    print("Lütfen 'E' veya 'H' cevabını verin.")
    
      

while True:
    print("""
    Ne yapmak istersiniz?
    1. Not ekle
    2. Notları görüntüle
    3. Not Sil
    4. Tüm Notları Sil
    5. Çıkış
    """)
    secim = input("Seçiminiz: ")
    if secim == "1":
        not_ekle()
        
    elif secim == "2":
        notlari_goster()

    elif secim == "3":
        not_sil()

    elif secim == "4":
        notlari_hepsini_sil()

    elif secim == "5":
        print("Uygulamadan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim!")
        
        
###@alierenkose
