# Cyberdeck Audit Hub

Interface locale pour orchestrer des outils d’audit sans copier leur code source.

## Sécurité

- Usage uniquement sur des réseaux possédés ou explicitement autorisés.
- Le mode actif exige une liste blanche de SSID/BSSID.
- Les actions perturbatrices, le phishing réel et la collecte de secrets sont désactivés.
- Les outils externes doivent être installés séparément et respecter leurs licences.

## Démarrage

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Ouvrir http://127.0.0.1:8080.
