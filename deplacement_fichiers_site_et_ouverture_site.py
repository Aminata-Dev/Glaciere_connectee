import shutil, os, webbrowser

os.chdir("site") #On change de dossier

files = ['fonctions.php', 'temperatures_glaciere.php', 'style.css']

for file in files:
    try:
        shutil.copy(file, r'C:\xampp\htdocs')
    except shutil.Error: #Si le fichier a deja été déplacé
        pass

print("Veuillez attendre l'ouverture du site")
os.system(r"c: && cd C:\xampp && xampp_start") #On lance xampp dans l'invite de commande

webbrowser.open("http://localhost/temperatures_glaciere.php") #On ouvre le site en local