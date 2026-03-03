import requests
import threading
import time
import random
import sys
import os

# =============================
# Load .env if exists
BRIDGE_IP = os.getenv("IP", "")
USERNAME = os.getenv("API", "")
# =============================

party_running = False
LIGHT_IDS = []

# Fixed BPM (adjustable)
BPM = 138
BEAT_INTERVAL = 60 / BPM  # seconds per beat (~0.435s)

# -----------------------------
# Functions
# -----------------------------
def get_lights():
    """Fetch all lights from the bridge and display their IDs and names."""
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights"
    try:
        response = requests.get(url, timeout=3)
        lights = response.json()
        print("\nAvailable lights:")
        for lid, info in lights.items():
            print(f"{lid}: {info['name']} ({info['type']})")
        return lights
    except Exception as e:
        print("Failed to get lights:", e)
        sys.exit(1)

def set_light(light_id, data):
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/{light_id}/state"
    try:
        requests.put(url, json=data, timeout=0.2)
    except:
        pass

def party_loop():
    global party_running
    while party_running:
        # Pick a single random hue for all lights
        hue = random.randint(0, 65535)
        state = {
            "on": True,
            "hue": hue,
            "sat": 254,
            "bri": 254,
            "transitiontime": 0
        }
        for light in LIGHT_IDS:
            set_light(light, state)
        time.sleep(BEAT_INTERVAL)

def party_on():
    global party_running
    if not party_running:
        party_running = True
        threading.Thread(target=party_loop, daemon=True).start()
        print("\n💃 PARTY MODE ACTIVATED\n")

def party_off():
    global party_running
    party_running = False
    time.sleep(0.2)
    calm = {
        "on": True,
        "hue": 8418,
        "sat": 140,
        "bri": 200,
        "transitiontime": 10
    }
    for light in LIGHT_IDS:
        set_light(light, calm)
    print("\n😌 Party mode deactivated\n")

# -----------------------------
# Main
# -----------------------------
def main():
    global BRIDGE_IP, USERNAME, LIGHT_IDS

    print("===== PHILIPS HUE PARTYMODE (Random Color, Fixed BPM) =====")

    # Prompt if env variables not set
    if not BRIDGE_IP:
        BRIDGE_IP = input("Enter your Hue Bridge IP: ").strip()
    else:
        print(f"Using IP from .env: {BRIDGE_IP}")
    if not USERNAME:
        USERNAME = input("Enter your Hue API key: ").strip()
    else:
        print("Using API key from .env")

    lights = get_lights()
    ids = input("\nEnter the light IDs to include (comma-separated, e.g., 1,2,3): ")
    LIGHT_IDS[:] = [x.strip() for x in ids.split(",")]

    print("\nPress P to toggle party mode.")
    print("Press Q to quit.\n")

    while True:
        key = input().lower()
        if key == "p":
            if party_running:
                party_off()
            else:
                party_on()
        elif key == "q":
            party_off()
            sys.exit()

if __name__ == "__main__":
    main()