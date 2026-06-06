# 🔥 Cyber Pentools — All-in-One Penetration Testing Toolkit

**200+ hacking tools** organized into 21 categories — information gathering, web exploitation, wireless attacks, password cracking, forensics, reverse engineering, and more.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-lightgrey)

---

## 🚀 Quick Install

```bash
git clone https://github.com/AdhiHub/cyber-pentools.git
cd cyber-pentools
sudo python3 install.py
```

Then run:
```bash
hackingtool
```

### One-liner (Linux/macOS)
```bash
curl -sSL https://raw.githubusercontent.com/AdhiHub/cyber-pentools/main/install.py | sudo python3
```

---

## 📂 Tool Categories

| # | Category | Tools |
|---|----------|-------|
| 1 | 🛡 Anonymously Hiding | anonsurf, multitor |
| 2 | 🔍 Information Gathering | nmap, masscan, rustscan, theHarvester, amass, subfinder, spiderfoot, gau, gospider, naabu + 25 more |
| 3 | 📚 Wordlist Generator | cupp, crunch, cewl, hashcat, john, haiti, psudohash, mentalist + 10 more |
| 4 | 📶 Wireless Attack | wifiphisher, wifite, fluxion, airgeddon, bettercap, hcxdumptool + 12 more |
| 5 | 🧩 SQL Injection | sqlmap, nosqlmap, dsss, explo, blisqy, leviathan |
| 6 | 🎣 Phishing Attack | setoolkit, socialfish, hiddeneye, evilginx, blackeye + 16 more |
| 7 | 🌐 Web Attack | nuclei, ffuf, feroxbuster, nikto, gobuster, wpscan, joomscan, katana + 22 more |
| 8 | 🔧 Post Exploitation | pwncat, sliver, havoc, peass, ligolo, chisel, evil-winrm, mythic + 10 more |
| 9 | 🕵 Forensics | wireshark, volatility3, binwalk, autopsy, bulk_extractor, pspy + 8 more |
| 10 | 📦 Payload Creation | thefatrat, msfpc, venom, stitch, enigma + 8 more |
| 11 | 🧰 Exploit Framework | routersploit, websploit, commix |
| 12 | 🔁 Reverse Engineering | ghidra, radare2, jadx, androguard, apk2gold |
| 13 | ⚡ DDOS Attack | slowloris, ufonet, goldeneye, saphyra |
| 14 | 🖥 Remote Admin (RAT) | pyshell |
| 15 | 💥 XSS Attack | dalfox, xsstrike, xspear, rvuln + 8 more |
| 16 | 🖼 Steganography | steghide, stegcracker |
| 17 | 🏢 Active Directory | bloodhound, netexec, impacket, responder, certipy, kerbrute |
| 18 | ☁ Cloud Security | prowler, scoutsuite, pacu, trivy |
| 19 | 📱 Mobile Security | mobsf, frida, objection |
| 20 | 🔑 Password Attacks | hydra, medusa, lazagne, rubeus, mimikatz, sprayingtoolkit + 16 more |
| 21 | ✨ Other Tools | social media, android, hash cracking, wifi jamming + 10 more |

---

## 🧭 How to Use

1. **Navigate** — Enter the number of a category to open it
2. **Select** — Pick a tool by its number
3. **Install** — Option 1 installs the tool automatically
4. **Run** — Option 2 launches the tool
5. **Search** — Type `/<query>` to search all tools
6. **Filter** — Press `t` to filter by tags (osint, web, scanner, etc.)
7. **Recommend** — Press `r` to get tool recommendations for your task

```
  ╰─> 7        ← open Web Attack category
  ╰─> 3        ← select nuclei
  ╰─> 1        ← install
  ╰─> 2        ← run nuclei
```

---

## 🔍 Search & Tag System

- **Search**: Type `/subdomain` to instantly find all subdomain enumeration tools
- **Tags**: Press `t` to browse by tag — osint, scanner, bruteforce, web, wireless, c2, cloud, mobile, etc.
- **Recommend**: Press `r`, pick a task, and get curated tool suggestions

---

## ⚙ Requirements

- **OS**: Linux (primary) / macOS (partial)
- **Python**: 3.10+
- **Python packages**: `rich`, `requests`
- **System**: git, curl, wget, go (optional), ruby (optional)

---

## 📦 Features

- **200+ tools** across 21 categories
- **One-command install** — dependencies, venv, and launcher
- **Smart search** — `/query` to find tools instantly
- **Tag filtering** — filter by osint, scanner, web, c2, credentials, and more
- **Task recommendations** — tell it what you want to do, get tool suggestions
- **Install all** — batch install all tools in a category
- **Auto-update** — git pull, pip upgrade, and go install detection
- **Archived tools** — preserved but flagged as unmaintained
- **OS-aware** — automatically hides incompatible tools

---

## ⚠️ Legal Disclaimer

```diff
+ This tool is provided for EDUCATIONAL PURPOSES ONLY.
+ It is intended for:
+   • Authorized security testing of your own systems
+   • Penetration testing engagements with written permission
+   • Security research in controlled environments
+
- Any unauthorized use of these tools against systems you
- do not own or have explicit permission to test is ILLEGAL.
- The developers assume NO LIABILITY for misuse.
```

By using this software, you agree to use it **only for lawful purposes** and in compliance with all applicable local, state, and federal laws.

---

## 🙌 Credits

Originally based on [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) with extensive modifications, additional tools, bug fixes, and a redesigned menu system.
