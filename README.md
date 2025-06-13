# botlecturevlc

[![Licence](https://img.shields.io/badge/license-MIT-green.svg)]  
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)]  

## Description

**botlecturevlc** est un lecteur basé sur **VLC** et **Tkinter** qui permet de :

- Sélectionner un dossier contenant des fichiers vidéo.
- Scrapper et trier les épisodes par ordre alphabétique.
- Créer une playlist VLC et lire les épisodes à la suite.
- Controler la lecture via boutons : sélection d'épisode, play/pause, suivant/précédent, avance rapide.
- Afficher le temps restant et une barre de progression actualisée chaque seconde.

## Objectifs

1. Automatiser la lecture en continu de séries locales.  
2. Proposer une interface minimale et rapide à lancer.  
3. Expérimentation personnelle pour rattraper ses séries efficacement.

## Installation

```bash
# 1. Cloner ce dépôt
git clone https://github.com/MathieuBal/botlecturevlc.git
cd botlecturevlc

# 2. (Optionnel) Créer un environnement virtuel
python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 3. Installer les dépendances
pip install -r requirements.txt
```

> **Note :** `tkinter` est inclus dans la bibliotèque standard de Python.

## Utilisation

```bash
python main.py
```

1. Choisissez un dossier contenant vos vidéos.  
2. La lecture démarre automatiquement et la barre de progression s'affiche.  
3. Utiliser les boutons pour :
   - Sélectionner un épisode ;
- Play/Pause ;
- Épisode suivant/précédent ;
- Avance de 10 secondes.

## Statut du projet

** En pause ** – non fonctionnel suite aux évolutions de Python et aux dépendances.

## Licence

MIT

---

## Améliorations futures
- Mettre à jour pour Python 3.10/3.11.  
- Fusionner la sélection de dossier et les contrôles dans une seule fenêtre.  
- Ajouter la gestion des sous-titres et le réglage du volume.
