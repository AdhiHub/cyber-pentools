from pathlib import Path
import platform
import shutil as _shutil

# ── Repository ────────────────────────────────────────────────────────────────
REPO_OWNER   = "AdhiHub"
REPO_NAME    = "cyber-pentools"
REPO_URL     = f"https://github.com/{REPO_OWNER}/{REPO_NAME}.git"
REPO_WEB_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}"

# ── Command / app name ────────────────────────────────────────────────────────
APP_NAME = "pentools"

# ── Versioning ────────────────────────────────────────────────────────────────
VERSION         = "1.0.0"
VERSION_DISPLAY = f"v{VERSION}"

# ── Python requirement ────────────────────────────────────────────────────────
MIN_PYTHON = (3, 10)

# ── User-scoped paths (cross-platform, always computed at runtime) ─────────────
# NEVER hardcode /home/username — use Path.home() so it works for any user,
# including root (/root), regular users (/home/alice), macOS (/Users/alice).
USER_CONFIG_DIR  = Path.home() / f".{APP_NAME}"
USER_TOOLS_DIR   = USER_CONFIG_DIR / "tools"
USER_CONFIG_FILE = USER_CONFIG_DIR / "config.json"
USER_LOG_FILE    = USER_CONFIG_DIR / f"{APP_NAME}.log"

# ── System install paths (set per OS) ─────────────────────────────────────────
_system = platform.system()

if _system == "Darwin":
    # macOS — Homebrew convention
    APP_INSTALL_DIR = Path("/usr/local/share") / APP_NAME
    APP_BIN_PATH    = Path("/usr/local/bin")   / APP_NAME
elif _system == "Linux":
    APP_INSTALL_DIR = Path("/usr/share") / APP_NAME
    APP_BIN_PATH    = Path("/usr/bin")   / APP_NAME
else:
    # Fallback (Windows, FreeBSD, etc.)
    APP_INSTALL_DIR = USER_CONFIG_DIR / "app"
    APP_BIN_PATH    = USER_CONFIG_DIR / "bin" / APP_NAME

# ── UI theme (cyber neon palette) ─────────────────────────────────────────────
THEME_PRIMARY  = "bold #00ffff"
THEME_BORDER   = "#ff00ff"
THEME_SUCCESS  = "bold #00ff88"
THEME_ERROR    = "bold #ff3355"
THEME_WARNING  = "bold #ffaa00"
THEME_DIM      = "dim #888888"
THEME_ARCHIVED = "dim #aa8800"
THEME_URL      = "underline #4488ff"
THEME_ACCENT   = "bold #ff8800"

# ── Default config values ──────────────────────────────────────────────────────
DEFAULT_CONFIG: dict = {
    "tools_dir":      str(USER_TOOLS_DIR),
    "version":        VERSION,
    "theme":          "magenta",
    "show_archived":  False,
    "sudo_binary":    "sudo",
    "go_bin_dir":     str(Path.home() / "go" / "bin"),
    "gem_bin_dir":    str(Path.home() / ".gem" / "ruby"),
}

# ── Privilege escalation ───────────────────────────────────────────────────────
# Prefer doas if present (OpenBSD/some Linux setups), else sudo
PRIV_CMD = "doas" if _shutil.which("doas") else "sudo"