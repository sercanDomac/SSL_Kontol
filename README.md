# SSL Sertifikası Kontrolü

Bu betik, belirtilen web sitesinin SSL sertifikasının sona erme süresini kontrol eder ve gerekirse bir uyarı e-postası gönderir.

## Kullanım

1. Python'u bilgisayarınıza yükleyin. [Python'un resmi web sitesinden](https://www.python.org/) indirebilirsiniz.

2. Gerekli Python kütüphanelerini yükleyin:

    ```bash
    pip install smtplib
    ```

3. Betiği çalıştırın:

    ```bash
    python ssl_certificate_checker.py
    ```

   Program sizi bir web sitesi adresi girmeniz konusunda yönlendirecek. Web sitesinin SSL sertifikasının sona erme süresini kontrol edecek ve sonuca göre bir uyarı mesajı gösterecektir.

4. Uyarı e-postası almak için gerekli bilgileri betik içindeki `send_alert_email` fonksiyonunda düzenleyin:

    - `sender_email`: Uyarı e-postalarının gönderileceği e-posta adresi.
    - `receiver_email`: Uyarı e-postalarının alınacağı e-posta adresi.
    - `password`: Gönderici e-post
