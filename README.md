# Unicode Decoder for Burp Suite

A Burp Suite extension that decodes `\uXXXX` Unicode escape sequences into readable characters (e.g., Persian/Arabic text).  

This makes working with internationalized web apps easier, since encoded Unicode text is displayed in plain form inside Burp.

---

## ✨ Features
- Adds a **"Unicode Decoded"** tab to all Burp message editors (Proxy, Repeater, Intruder, etc.).
- Automatically decodes `\uXXXX` sequences to human-readable characters.
- Non-intrusive: original requests/responses are not modified.
- Works with **Jython-based Burp extensions**.

---

## 📦 Installation
1. Install **Jython standalone JAR** (Burp → Extender → Options → Python Environment).  
   Download from: https://www.jython.org/download  
2. Clone this repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/unicode-decoder-burp.git
