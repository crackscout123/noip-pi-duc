import base64
import requests
from datetime import datetime


# Funktion zur Abfrage der externen IP-Adresse
def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=text')
        if response.status_code == 200:
            return response.text
        else:
            print(f"Fehler bei der IP-Abfrage: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None

# Benutzerinformationen und Hostname - HIER DATEN EINTRAGEN
username = "NOIP-DNS-USERNAME"
password = "NOIP-DNS-PASSWORD"
hostname = "NOIP-HOSTNAME"

# Externe IP-Adresse abrufen
ip_address = get_external_ip()

# Überprüfen, ob die IP erfolgreich abgerufen wurde
if ip_address:
    # URL für den Update-Request
    url = f"http://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip_address}"

    # Benutzername:Passwort als Base64 kodieren
    auth_string = f"{username}:{password}"
    auth_base64 = base64.b64encode(auth_string.encode()).decode()

    # Headers, inklusive Autorisierung und User-Agent
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "User-Agent": "MyCompany MyDevice-Model/1.0 admin@hostname.tld"  # Passe dies an deine Daten an
    }

    # GET-Anfrage senden
    response = requests.get(url, headers=headers)

    # Aktuelles Datum und Uhrzeit auslesen
    now = datetime.now()

    # Formatierung von Datum und Uhrzeit: z.B. "2024-09-21 14:35:10"
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"{current_time}") # Datum für Log
    # Antwort ausgeben
    print(f"Response Code: {response.status_code}")
    print(f"Response Text: {response.text}")
else:
    print("Die externe IP-Adresse konnte nicht abgerufen werden.")
