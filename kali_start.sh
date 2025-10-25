#!/bin/bash
# X WIRELESS - Kali Linux Quick Start
# Creato da: Adil Fayyaz
# Instagram: @Infinityx_20257

echo "X WIRELESS - Kali Linux Edition"
echo "==============================="
echo "Creato da: Adil Fayyaz"
echo "Instagram: @Infinityx_20257"
echo "SOLO PER SCOPI EDUCATIVI"
echo "==============================="
echo ""

# Controlla se siamo nella directory corretta
if [ ! -f "xwirless/__init__.py" ]; then
    echo "ERRORE: Non sei nella directory xwirless"
    echo "Esegui: cd xwirless"
    exit 1
fi

# Attiva ambiente virtuale se esiste
if [ -d "venv" ]; then
    echo "Attivando ambiente virtuale..."
    source venv/bin/activate
fi

echo "Scegli modalita di avvio:"
echo "1. Test Sandbox (Sicuro)"
echo "2. Test Dry-Run (Simulazione)"
echo "3. Interfaccia Interattiva"
echo "4. Informazioni Sistema"
echo "5. CLI Completa"
echo ""

read -p "Scegli (1-5): " choice

case $choice in
    1)
        echo "Avviando test sandbox..."
        python3 -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --format json
        ;;
    2)
        echo "Avviando test dry-run..."
        python3 -m xwirless scan --dry-run --format md
        ;;
    3)
        echo "Avviando interfaccia interattiva..."
        python3 interfaccia_interattiva.py
        ;;
    4)
        echo "Mostrando informazioni sistema..."
        python3 -m xwirless info
        ;;
    5)
        echo "Avviando CLI completa..."
        python3 -m xwirless --help
        ;;
    *)
        echo "Scelta non valida"
        ;;
esac

echo ""
echo "Ricorda: Solo per scopi educativi su reti autorizzate!"
