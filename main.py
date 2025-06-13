import botlecturevlcv2
import tkinter.filedialog as fd

# Si aucun index d'épisode n'est spécifié, demander à l'utilisateur de sélectionner un dossier
folder_path = fd.askdirectory()

# Si un dossier est sélectionné, appeler la fonction play_series avec le chemin du dossier
if folder_path:
    botlecturevlcv2.play_series(folder_path)
    # Lancer la boucle principale Tkinter pour afficher l'interface
    botlecturevlcv2.main()
