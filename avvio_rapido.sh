#!/bin/bash
# X WIRELESS - Avvio Rapido Kali Linux
# Creato da: Adil Fayyaz
# Instagram: @Infinityx_20257

echo "X WIRELESS - Avvio Rapido"
echo "========================="
echo "Creato da: Adil Fayyaz"
echo "Instagram: @Infinityx_20257"
echo ""

# Controlla se siamo nella directory corretta
if [ ! -f "interfaccia_kali.py" ]; then
    echo "ERRORE: File interfaccia_kali.py non trovato"
    echo "Assicurati di essere nella directory xwirless"
    echo ""
    echo "Per clonare il repository:"
    echo "git clone https://github.com/Adil-fayyaz/xwirless.git"
    echo "cd xwirless"
    echo "./avvio_rapido.sh"
    exit 1
fi

# Controlla Python
if ! command -v python3 &> /dev/null; then
    echo "ERRORE: Python3 non installato"
    echo "Installa con: sudo apt install python3 python3-pip"
    exit 1
fi

# Controlla dipendenze
echo "Controllando dipendenze..."
python3 -c "import click, pydantic, requests" 2>/dev/null || {
    echo "Installando dipendenze..."
    pip3 install click pydantic requests
}

# Avvia interfaccia
echo ""
echo "Avviando X WIRELESS..."
echo "======================"
echo ""

python3 interfaccia_kali.py
