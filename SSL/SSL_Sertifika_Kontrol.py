import ssl
import socket
import datetime
import smtplib

def main():
    website = input("Sertifika süresini kontrol etmek istediğiniz web sitesinin adresini girin: ")
    remaining_days = check_ssl_expiry(website)
    
    if remaining_days > 30:
        print(f"Sertifika {remaining_days} gün sonra sona erecek. Hala geçerli.")
    elif remaining_days > 0:
        print(f"Sertifika {remaining_days} gün sonra sona erecek. Yakında yenilenmesi gerekecek.")
        # Uyarı mesajı ekle
        send_alert_email(website, remaining_days)
    else:
        print("Sertifika süresi dolmuş. Hemen yenilenmesi gerekiyor!")
        # Uyarı mesajı ekle
        send_alert_email(website, remaining_days)

def check_ssl_expiry(hostname):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.settimeout(10)  # Timeout'u ayarlayabilirsiniz
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    expiration_date = ssl_info['notAfter']
    expiry_datetime = datetime.datetime.strptime(expiration_date, "%b %d %H:%M:%S %Y %Z")
    remaining_days = (expiry_datetime - datetime.datetime.now()).days
    return remaining_days

def send_alert_email(website, remaining_days):
    # E-posta göndermek için gereken bilgileri girin
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    password = "your_password"
    
    # E-posta başlığı ve içeriği oluşturun
    subject = f"SSL Sertifikası Uyarısı: {website}"
    body = f"Uyarı: {website} sitesinin SSL sertifikası {remaining_days} gün içinde dolacak!"
    message = f"Subject: {subject}\n\n{body}"
    
    # E-posta sunucusuna bağlanın ve e-posta gönderin
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

main()
