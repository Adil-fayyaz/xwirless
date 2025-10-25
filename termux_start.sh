#!/bin/bash
# X WIRELESS - Termux Quick Start
# Creato da: Adil Fayyaz
# Instagram: @Infinityx_20257

echo "X WIRELESS - Termux Edition"
echo "=========================="
echo "Creato da: Adil Fayyaz"
echo "Instagram: @Infinityx_20257"
echo "SOLO PER SCOPI EDUCATIVI"
echo ""

# Vai nella directory del progetto
cd ~/xwirless 2>/dev/null || {
    echo "Repository non trovato. Clona prima con:"
    echo "git clone https://github.com/Adil-fayyaz/xwirless.git"
    exit 1
}

echo "Test in modalita sandbox..."
python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --format json

echo ""
echo "Test completato!"
echo "Per altri comandi: python -m xwirless --help"
