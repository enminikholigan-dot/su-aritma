# Su Arıtma Müşteri Takip — Kurulum Talimatları

## Telefona Nasıl Kurulur?

Bu uygulama bir PWA (Progressive Web App) — uygulama mağazasına gerek yok.
Bir web sunucusuna yüklemeniz yeterli. En kolay yol: **GitHub Pages (ücretsiz)**

---

## ADIM 1: GitHub Hesabı Aç
1. https://github.com adresine git
2. "Sign up" ile ücretsiz hesap oluştur

## ADIM 2: Yeni Repo Oluştur
1. Giriş yaptıktan sonra sağ üstteki "+" → "New repository"
2. Repository name: `su-aritma` (veya istediğiniz isim)
3. "Public" seçili olsun
4. "Create repository" butonuna bas

## ADIM 3: Dosyaları Yükle
1. Oluşturulan sayfada "uploading an existing file" linkine tıkla
2. Şu dosyaları sürükle-bırak ile yükle:
   - index.html
   - manifest.json
   - sw.js
   - icons/ klasörü içindeki icon-192.png ve icon-512.png
3. "Commit changes" butonuna bas

## ADIM 4: GitHub Pages'i Aç
1. Repo sayfasında "Settings" sekmesine git
2. Sol menüden "Pages" seç
3. "Source" bölümünde "Deploy from a branch" seç
4. Branch: "main" → "/ (root)" seç
5. "Save" butonuna bas
6. Birkaç dakika bekle → Adres çıkacak:
   https://KULLANICI_ADIN.github.io/su-aritma/

## ADIM 5: Telefona Kur

### Android (Chrome):
1. Yukarıdaki adresi Chrome'da aç
2. Sağ üst menü (⋮) → "Ana ekrana ekle"
3. "Ekle" ye bas → Uygulama simgesi çıkar!

### iPhone (Safari):
1. Adresi Safari'de aç (Chrome değil, Safari olmalı)
2. Alt ortadaki paylaş butonuna bas (kare + ok)
3. "Ana Ekrana Ekle" → "Ekle"

---

## Önemli Notlar
- Veriler telefonun tarayıcısında saklanır (localStorage)
- İnternet olmadan da çalışır (service worker sayesinde)
- Verileri yedeklemek için Excel'e aktar özelliğini kullanın

## Destek
Sorun yaşarsanız Claude'a danışabilirsiniz!
