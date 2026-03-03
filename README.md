# 🎉 Philips Hue PartyMode

Turn your Philips Hue lights into a synchronized, random-color party!

## ✨ Features

- **Fixed BPM flashing** (default 138 BPM, adjustable)
- **Random color per beat**, applied to all selected lights
- **Supports multiple bulbs** (all synchronized)
- **Detects and displays available lights** automatically
- **Supports .env file** for IP and API key
- **Toggle party mode** (P) / quit (Q)
- **Calms lights on exit**

## 📋 Requirements

- **Python 3.7+**
- **requests library** (install with `pip install requests`)
- **Philips Hue Bridge + color bulbs**
- **.env file** with IP and API key

## 🚀 Installation

1. Copy `party.py` and this README into a folder
2. Install dependencies: `pip install requests`
3. Create a `.env` file in the same folder containing:

```env
IP=Hub_IP
API=your_hue_api_key_here
```

> 💡 **Tip**: You can get your API key by pressing the button on your Hue Bridge and following Hue API instructions.

**PowerShell API Key Generation**:
```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://YOUR_HUE_BRIDGE_IP/api" `
  -Body '{"devicetype":"partymode#pc"}' `
  -ContentType "application/json"
```

## 🎮 Usage

- **Run the script**: `python party.py`
- If `.env` contains IP and API, they will be used automatically
- If not, you will be prompted for Hue Bridge IP and API key
- The script will list all detected lights
- Enter the light IDs you want to include (comma-separated)

### 🎛️ Controls

| Key | Action |
|-----|--------|
| **P** | Toggle party mode on/off |
| **Q** | Quit and return lights to calm state |

## ⚙️ Configuration

- **BPM**: Change the BPM variable in the script to adjust flash speed
- **Brightness / Saturation**: Modify `bri` and `sat` in `party_loop()` for different effects
- **All bulbs synchronized**: All selected bulbs get the same color per beat

## 📝 Notes

- ⚠️ **Rapid flashing may strain bulbs**; if you notice lag, increase `BEAT_INTERVAL` slightly
- 🎬 **Perfect for recording eurodance-style videos** — adjust video speed in post to match song tempo

## 📄 License

**MIT License** — free to use and customize
