from pathlib import Path

racine = Path(__file__).parent
#racine = current_directory.parent 


 

path_data_set = racine / "dataset"/"royal_fitness.db"

path_profils_images = racine/"images"/"profiles"

logo_path = racine/"images"/"logos"/"logoa.png"


background_path = racine / "style"/"image.jpg"
arrowdrop = racine/"images"/"logos"/"ic_arrow_drop_down_black_18dp_1x.png"

print(str(background_path).replace("\\", "/"))

def set_styles():
    try:
        with open(racine/"style"/"style.qss", "r") as file:
            style = file.read()
            style = style.replace("background_image", "'"+str(background_path)+"'")
            style = style.replace("arrowdrop", "'"+str(arrowdrop)+"'")
            return style
    except FileNotFoundError:
        print("Style file not found. Using default styles.")
