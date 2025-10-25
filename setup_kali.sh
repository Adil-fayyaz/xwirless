#!/bin/bash
# X WIRELESS - Setup Script per Kali Linux
# Creato da: Adil Fayyaz

echo "X WIRELESS - Setup Automatico"
echo "=============================="
echo "Creato da: Adil Fayyaz"
echo "Instagram: @Infinityx_20257"
echo ""

# Controlla se siamo root
if [ "$EUID" -eq 0 ]; then
    echo "ERRORE: Non eseguire come root"
    echo "Il script usera sudo quando necessario"
    exit 1
fi

# Controlla sistema operativo
if command -v apt &> /dev/null; then
    OS="debian"
elif command -v yum &> /dev/null; then
    OS="redhat"
elif command -v pacman &> /dev/null; then
    OS="arch"
else
    echo "ERRORE: Sistema operativo non supportato"
    exit 1
fi

echo "Sistema rilevato: $OS"

# Installa dipendenze di sistema
echo ""
echo "Installando dipendenze di sistema..."
case $OS in
    "debian")
        sudo apt update
        sudo apt install -y python3 python3-pip python3-venv git
        ;;
    "redhat")
        sudo yum install -y python3 python3-pip git
        ;;
    "arch")
        sudo pacman -S --noconfirm python python-pip git
        ;;
esac

# Verifica Python
echo ""
echo "Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    echo "Python $PYTHON_VERSION trovato"
else
    echo "ERRORE: Python3 non installato"
    exit 1
fi

# Clona repository
echo ""
echo "Clonando repository..."
if [ -d "xwirless" ]; then
    echo "Directory xwirless gia esistente"
    cd xwirless
else
    git clone https://github.com/Adil-fayyaz/xwirless.git
    cd xwirless
fi

# Crea ambiente virtuale
echo ""
echo "Creando ambiente virtuale..."
python3 -m venv venv
source venv/bin/activate

# Installa dipendenze Python
echo ""
echo "Installando dipendenze Python..."
pip install --upgrade pip
pip install click pydantic requests

# Testa installazione
echo ""
echo "Testando installazione..."
python3 -c "
try:
    import click, pydantic, requests
    print('OK: Tutte le dipendenze installate')
except ImportError as e:
    print(f'ERRORE: {e}')
    exit(1)
"

# Testa interfaccia
echo ""
echo "Testando interfaccia..."
python3 interfaccia_ascii.py --help 2>/dev/null || echo "Interfaccia pronta per l'uso"

echo ""
echo "SETUP COMPLETATO!"
echo "=================="
echo ""
echo "Per avviare X WIRELESS:"
echo "1. cd xwirless"
echo "2. source venv/bin/activate"
echo "3. python3 interfaccia_ascii.py"
echo ""
echo "O direttamente:"
echo "python3 interfaccia_ascii.py"
echo ""
echo "Ricorda: Solo per scopi educativi!"
