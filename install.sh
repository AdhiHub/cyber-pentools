#!/usr/bin/env bash
set -e

RED='\033[1;31m'; GREEN='\033[1;32m'; CYAN='\033[1;36m'; YELLOW='\033[1;33m'; RESET='\033[0m'

REPO_URL="https://github.com/AdhiHub/cyber-pentools.git"
INSTALL_DIR="/opt/cyber-pentools"

echo -e "${RED}"
echo "╔══════════════════════════════════════╗"
echo "║    CYBER-PENTOOLS INSTALLER v1.1    ║"
echo "╚══════════════════════════════════════╝"
echo -e "${RESET}"
echo -e "${YELLOW}Use at your own risk, developer assume NO liability${RESET}"
echo ""

# Check deps
for cmd in git python3 curl; do
    if ! command -v "$cmd" &>/dev/null; then
        echo -e "${RED}[!] $cmd is required but not installed.${RESET}"
        echo -e "${YELLOW}[*] Install with: sudo apt install $cmd${RESET}"
        exit 1
    fi
done

# Install rich (needed by install.py)
echo -e "${CYAN}[*] Installing Python dependencies...${RESET}"
if command -v pip3 &>/dev/null; then
    pip3 install rich --quiet 2>/dev/null || true
elif command -v pip &>/dev/null; then
    pip install rich --quiet 2>/dev/null || true
fi

# Clone repo
if [ -d "$INSTALL_DIR" ]; then
    echo -e "${YELLOW}[!] $INSTALL_DIR already exists. Removing...${RESET}"
    rm -rf "$INSTALL_DIR"
fi

echo -e "${CYAN}[*] Cloning repository...${RESET}"
git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"

# Run the real installer
echo -e "${CYAN}[*] Running installer...${RESET}"
cd "$INSTALL_DIR"
python3 install.py

echo -e "${GREEN}[+] Done! Run: pentools${RESET}"
