from core import HackingTool, HackingToolsCollection, console
from rich.prompt import Prompt


class Hydra(HackingTool):
    TITLE = "Hydra (Network Logon Cracker)"
    DESCRIPTION = (
        "Fast parallelized network logon cracker supporting 50+ protocols.\n"
        "Usage: hydra -l admin -P wordlist.txt ssh://target"
    )
    SUPPORTED_OS = ["linux", "macos"]
    INSTALL_COMMANDS = ["sudo apt-get install -y hydra || sudo pacman -S hydra || brew install hydra"]
    RUN_COMMANDS = ["hydra --help"]
    PROJECT_URL = "https://github.com/vanhauser-thc/thc-hydra"


class Medusa(HackingTool):
    TITLE = "Medusa (Parallel Network Login Auditor)"
    DESCRIPTION = (
        "Massively parallel network login brute-forcer.\n"
        "Usage: medusa -h target -u admin -P wordlist.txt -M ssh"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y medusa"]
    RUN_COMMANDS = ["medusa --help"]
    PROJECT_URL = "https://github.com/jmk-foofus/medusa"


class CeWL(HackingTool):
    TITLE = "CeWL (Custom Wordlist Generator)"
    DESCRIPTION = (
        "Spider a website and generate custom wordlists from its content.\n"
        "Usage: cewl https://example.com -w wordlist.txt"
    )
    SUPPORTED_OS = ["linux", "macos"]
    INSTALL_COMMANDS = ["sudo gem install cewl || brew install cewl"]
    RUN_COMMANDS = ["cewl --help"]
    PROJECT_URL = "https://github.com/digininja/CeWL"
    REQUIRES_RUBY = True


class Crunch(HackingTool):
    TITLE = "Crunch (Wordlist Generator)"
    DESCRIPTION = (
        "Generate wordlists with custom character sets and patterns.\n"
        "Usage: crunch 8 8 abcdef123 -o wordlist.txt"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y crunch"]
    RUN_COMMANDS = ["crunch --help"]
    PROJECT_URL = "https://github.com/jim3ma/crunch"


class LaZagne(HackingTool):
    TITLE = "LaZagne (Password Recovery)"
    DESCRIPTION = (
        "Extract stored passwords from browsers, chats, databases, wifi, and more.\n"
        "Usage: laZagne.exe all or python3 laZagne.py all"
    )
    SUPPORTED_OS = ["linux", "macos", "windows"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/AlessandroZ/LaZagne.git",
        "cd LaZagne && pip install --user -r requirements.txt",
    ]
    RUN_COMMANDS = ["cd LaZagne && python3 laZagne.py --help"]
    PROJECT_URL = "https://github.com/AlessandroZ/LaZagne"


class DomainPasswordSpray(HackingTool):
    TITLE = "DomainPasswordSpray (AD Password Spray)"
    DESCRIPTION = (
        "Password spraying tool for Active Directory — low-and-slow to avoid lockouts.\n"
        "Usage: Invoke-DomainPasswordSpray -UserList users.txt -Password Winter2024"
    )
    SUPPORTED_OS = ["linux", "macos"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/dafthack/DomainPasswordSpray.git",
    ]
    PROJECT_URL = "https://github.com/dafthack/DomainPasswordSpray"

    def __init__(self):
        super().__init__(runnable=False)


class ASREPRoast(HackingTool):
    TITLE = "ASREPRoast (Kerberos Pre-Auth Attack)"
    DESCRIPTION = (
        "Find and exploit Kerberos pre-authentication disabled accounts.\n"
        "Usage: python3 GetNPUsers.py domain/ -usersfile users.txt -format hashcat"
    )
    SUPPORTED_OS = ["linux", "macos"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/HarmJ0y/ASREPRoast.git",
    ]
    PROJECT_URL = "https://github.com/HarmJ0y/ASREPRoast"

    def __init__(self):
        super().__init__(runnable=False)


class SprayingToolkit(HackingTool):
    TITLE = "SprayingToolkit (Password Spray Automation)"
    DESCRIPTION = (
        "Automated password spraying against OWA, Lync, and O365.\n"
        "Usage: atomizer -u users.txt -p passwords.txt -t outlook.office365.com"
    )
    SUPPORTED_OS = ["linux", "macos"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/byt3bl33d3r/SprayingToolkit.git",
        "cd SprayingToolkit && pip install --user -r requirements.txt",
    ]
    RUN_COMMANDS = ["cd SprayingToolkit && python3 atomizer.py --help"]
    PROJECT_URL = "https://github.com/byt3bl33d3r/SprayingToolkit"


class Rubeus(HackingTool):
    TITLE = "Rubeus (Kerberos Abuse Tool)"
    DESCRIPTION = (
        "Kerberos authentication abuse toolkit — ASREP roasting, Kerberoasting,\n"
        "pass-the-ticket, silver/golden tickets, and more."
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/GhostPack/Rubeus.git",
    ]
    PROJECT_URL = "https://github.com/GhostPack/Rubeus"

    def __init__(self):
        super().__init__(runnable=False)


class Mimikatz(HackingTool):
    TITLE = "Mimikatz (Windows Credential Dumper)"
    DESCRIPTION = (
        "Extract plaintext passwords, hashes, PINs, and Kerberos tickets from memory.\n"
        "Load via: mimikatz.exe -> privilege::debug -> sekurlsa::logonpasswords"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/gentilkiwi/mimikatz.git",
    ]
    PROJECT_URL = "https://github.com/gentilkiwi/mimikatz"

    def __init__(self):
        super().__init__(runnable=False)


class Psudohash(HackingTool):
    TITLE = "psudohash (Keyword-based Wordlist Generator)"
    DESCRIPTION = (
        "Generates password lists from a single base keyword with mutations.\n"
        "Usage: python3 psudohash.py -kw company -y 2020-2024"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/t3l3machus/psudohash.git"]
    RUN_COMMANDS = ["cd psudohash && python3 psudohash.py --help"]
    PROJECT_URL = "https://github.com/t3l3machus/psudohash"


class Mentalist(HackingTool):
    TITLE = "Mentalist (Wordlist Mutation GUI)"
    DESCRIPTION = (
        "Graphical wordlist mutation tool with case permutation, leet speak,\n"
        "append/prepend, and character substitution rules."
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/sc0tfree/mentalist.git",
        "cd mentalist && pip install --user -r requirements.txt",
    ]
    RUN_COMMANDS = ["cd mentalist && python3 mentalist.py --help"]
    PROJECT_URL = "https://github.com/sc0tfree/mentalist"


class PACK(HackingTool):
    TITLE = "PACK (Password Analysis & Cracking Kit)"
    DESCRIPTION = (
        "Password analysis and rule generation toolkit for hashcat.\n"
        "Includes statsgen, maskgen, policygen, and more."
    )
    INSTALL_COMMANDS = ["git clone https://github.com/iphelix/pack.git"]
    PROJECT_URL = "https://github.com/iphelix/pack"

    def __init__(self):
        super().__init__(runnable=False)


class Statsgen(HackingTool):
    TITLE = "statsgen (Password Stats Generator)"
    DESCRIPTION = (
        "Analyze password lists and generate statistical reports.\n"
        "Usage: python3 statsgen.py wordlist.txt"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/iphelix/pack.git"]
    RUN_COMMANDS = ["cd pack && python3 statsgen.py --help"]
    PROJECT_URL = "https://github.com/iphelix/pack"


class Maskgen(HackingTool):
    TITLE = "maskgen (Hashcat Mask Generator)"
    DESCRIPTION = (
        "Generate hashcat masks from password lists for targeted cracking.\n"
        "Usage: python3 maskgen.py wordlist.txt"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/iphelix/pack.git"]
    RUN_COMMANDS = ["cd pack && python3 maskgen.py --help"]
    PROJECT_URL = "https://github.com/iphelix/pack"


class Policygen(HackingTool):
    TITLE = "policygen (Password Policy Generator)"
    DESCRIPTION = (
        "Generate passwords that match specific complexity policies.\n"
        "Usage: python3 policygen.py --minlength 8 --maxlength 12 --minlower 1 --minupper 1 --mindigit 1"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/iphelix/pack.git"]
    RUN_COMMANDS = ["cd pack && python3 policygen.py --help"]
    PROJECT_URL = "https://github.com/iphelix/pack"


class SearchPass(HackingTool):
    TITLE = "SearchPass (Password Search Tool)"
    DESCRIPTION = (
        "Search for passwords matching patterns across multiple data sources.\n"
        "Usage: python3 searchpass.py --input hashes.txt --rules rules.rule"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/hak5/searchpass.git",
    ]
    PROJECT_URL = "https://github.com/hak5/searchpass"

    def __init__(self):
        super().__init__(runnable=False)


class Tiknr(HackingTool):
    TITLE = "TiKNR (Password Mutator)"
    DESCRIPTION = (
        "Password mutation tool that combines keywords, numbers, and rules.\n"
        "Usage: python3 tiknr.py -w wordlist.txt"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/psychomario/tiknr.git",
    ]
    PROJECT_URL = "https://github.com/psychomario/tiknr"

    def __init__(self):
        super().__init__(runnable=False)


class PasswordAttackTools(HackingToolsCollection):
    TITLE = "Password Attacks & Cracking"
    DESCRIPTION = "Tools for password cracking, wordlist generation, credential spraying, and Kerberos attacks."
    TOOLS = [
        Hydra(),
        Medusa(),
        CeWL(),
        Crunch(),
        LaZagne(),
        DomainPasswordSpray(),
        ASREPRoast(),
        SprayingToolkit(),
        Rubeus(),
        Mimikatz(),
        Psudohash(),
        Mentalist(),
        PACK(),
        Statsgen(),
        Maskgen(),
        Policygen(),
        SearchPass(),
        Tiknr(),
    ]


if __name__ == "__main__":
    tools = PasswordAttackTools()
    tools.show_options()
