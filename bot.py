import requests

# URL de l'API
URL = "https://ourworldoftext.com/_/write"

# Ton message à écrire
TEXT = "TON MESSAGE ICI"

def write_char(x, y, ch):
    payload = {
        "world": "main",
        "tiles": {
            "0,0": {
                "chars": [
                    {"x": x, "y": y, "ch": ch}
                ]
            }
        }
    }
    r = requests.post(URL, json=payload)
    if r.status_code == 200:
        print(f"Écrit '{ch}' en ({x},{y})")
    else:
        print("Erreur:", r.status_code, r.text)

def write_text(text, start_x=0, start_y=0):
    x = start_x
    y = start_y
    for ch in text:
        write_char(x, y, ch)
        x += 1  # avance d'une case vers la droite

if __name__ == "__main__":
    write_text(TEXT, 0, 0)
    print("✅ Message écrit avec succès !")
