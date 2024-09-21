
# Python DUC (NOIP)

Ein Python Skript zum Updaten von IPs für das DNS-Netzwerk von NOIP.



## Füge deine Daten von noip.com hier ein

```py
# Benutzerinformationen und Hostname - HIER DATEN EINTRAGEN
username = "NOIP-DNS-USERNAME"
password = "NOIP-DNS-PASSWORD"
hostname = "NOIP-HOSTNAME"
```


## Ausführen

Benutze crownjobs

```bash
 #*/5 * * * * /usr/bin/python3 /path/to/duc.py >> /path/to/duc.log 2>&1
```
sendet alle 5min die aktuelle IP des Gerätes an noip.com 
Es wird auch eine .log datei erstellt.
