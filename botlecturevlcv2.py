import tkinter as tk
import tkinter.filedialog as fd
import vlc
import os

# Constantes pour les options de lecture
PAUSE = 1
RESUME = 2
NEXT_EPISODE = 3
PREVIOUS_EPISODE = 4
SEEK_FORWARD = 5
SELECT_EPISODE = 6
QUIT = 7

# Création de la fenêtre principale
root = tk.Tk()
root.title("Lecteur de séries")

# Initialisation de VLC
instance = vlc.Instance('--no-xlib')  
player = instance.media_list_player_new()
media_player = instance.media_player_new()

# Création de la barre de progression et du label de temps
progress_bar = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.001)
progress_label = tk.Label(root, text="Temps restant : 0 secondes")
# Extensions vidéo prises en charge
video_extensions = ('.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv')
# Variable globale pour stocker la liste des épisodes
episode_list = []


def update_progress():
    mp = player.get_media_player()
    total_duration = mp.get_length() / 1000
    current_position = mp.get_position()

    if total_duration > 0:
        time_remaining = total_duration * (1 - current_position)
        hours, seconds = divmod(time_remaining, 3600)
        minutes, seconds = divmod(seconds, 60)
        progress_label.config(
            text="Temps restant : {:02d}h {:02d}m {:02d}s".format(
                int(hours), int(minutes), int(seconds))
        )
        progress_bar.set(current_position)

    root.after(1000, update_progress)


def play_series(folder_path, episode_index=None):
    global episode_list

    episode_list = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith(video_extensions) and os.path.isfile(os.path.join(folder_path, f))
    ])

    if not episode_list:
        print("Aucun fichier vidéo valide trouvé dans ce dossier.")
        return

    media_list = instance.media_list_new()
    for episode in episode_list:
        full_path = os.path.abspath(os.path.join(folder_path, episode))

        try:
            media = instance.media_new_path(full_path)
            if media is not None:
                media_list.add_media(media)
            else:
                print(f"[ERREUR] Impossible de créer un média pour : {full_path}")
        except Exception as e:
            print(f"[EXCEPTION] Fichier ignoré : {full_path}")
            print(f"Raison : {e}")

    player.set_media_list(media_list)

    if episode_index is not None:
        player.play_item_at_index(episode_index)
    else:
        player.play()
        update_progress()



def select_folder():
    folder_path = fd.askdirectory()
    if folder_path:
        play_series(folder_path)


def select_episode():
    selector = tk.Toplevel(root)
    selector.title("Sélectionner un épisode")
    selector.geometry("300x200")

    listbox = tk.Listbox(selector, selectmode=tk.SINGLE)
    for episode in episode_list:
        listbox.insert(tk.END, episode)

    def on_select(event):
        selected_index = listbox.curselection()[0]
        selector.destroy()
        player.play_item_at_index(selected_index)

    listbox.bind("<<ListboxSelect>>", on_select)
    listbox.pack()


def pause_resume():
    mp = player.get_media_player()
    if mp.is_playing():
        mp.pause()
    else:
        mp.play()


def navigate(option):
    if option == NEXT_EPISODE:
        player.next()
    elif option == PREVIOUS_EPISODE:
        player.previous()


def seek():
    mp = player.get_media_player()
    mp.set_time(mp.get_time() + 10000)


def quit_series():
    player.stop()
    root.destroy()


# Création des boutons
folder_button = tk.Button(root, text="Choisir un dossier", command=select_folder)
pause_button = tk.Button(root, text="Play/Pause", command=pause_resume)
next_button = tk.Button(root, text="Épisode suivant", command=lambda: navigate(NEXT_EPISODE))
previous_button = tk.Button(root, text="Épisode précédent", command=lambda: navigate(PREVIOUS_EPISODE))
seek_button = tk.Button(root, text="Avancer 10s", command=seek)
select_episode_button = tk.Button(root, text="Sélectionner épisode", command=select_episode)
quit_button = tk.Button(root, text="Quitter", command=quit_series)

# Placement des boutons
folder_button.grid(row=0, column=0)
select_episode_button.grid(row=0, column=1)
pause_button.grid(row=1, column=0)
seek_button.grid(row=1, column=1)
next_button.grid(row=2, column=0)
previous_button.grid(row=2, column=1)
progress_label.grid(row=3, column=0, columnspan=2)
progress_bar.grid(row=4, column=0, columnspan=2)
quit_button.grid(row=5, column=0, columnspan=2)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
