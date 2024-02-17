#!/bin/bash

# Chemin vers le dossier contenant les fichiers .csv
DATA_FOLDER="./data"

# Vérifiez si le dossier $DATA_FOLDER existe
if [ -d "$DATA_FOLDER" ]; then
    # Trouvez tous les fichiers .csv dans le dossier $DATA_FOLDER
    CSV_FILES=$(find $DATA_FOLDER -type f -name "*.csv")
    
    # Itérez sur chaque fichier .csv trouvé
    for FILE in $CSV_FILES; do
        echo "Exécution d'analyse.py sur $FILE..."
        # Exécutez analyse.py en passant le chemin du fichier .csv comme argument
        python analyse.py "$FILE"
        echo "Traitement terminé pour $FILE"
    done
else
    echo "Le dossier '$DATA_FOLDER' n'existe pas."
fi
