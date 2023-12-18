import os
from PIL import Image


def convert_images(invoermap, uitvoermap):
    if not os.path.exists(uitvoermap):
        os.makedirs(uitvoermap)

    for invoer_bestandsnaam in os.listdir(invoermap):
        if invoer_bestandsnaam.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(invoermap, invoer_bestandsnaam)
            try:
                with Image.open(file_path) as img:
                    uitvoer_bestandsnaam = invoer_bestandsnaam.split(".")[0] + ".png"
                    img.save(os.path.join(uitvoermap, uitvoer_bestandsnaam), 'PNG')
            except Exception as e:
                print(f"Error processing {invoer_bestandsnaam}: {str(e)}")

#Maak de input folder gelijk aan huidige map
invoermap = os.path.dirname(os.path.realpath(__file__))

#Vraag de gebruiker waar de uitvoer moet worden opgeslaan.
uitvoermap = input("Wat is de uitvoer map: ")

convert_images(invoermap, uitvoermap)