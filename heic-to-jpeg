#importeer de nodige onderdelen
import os
from PIL import Image


def convert_images(invoer_map, uitvoer_map):
    # Als de uitvoer_map niet bestaat, maak die dan.
    if not os.path.exists(uitvoer_map):
        os.makedirs(uitvoer_map)

    # Voor elk bestand in de invoer_map.
    for invoer_bestandsnaam in os.listdir(invoer_map):

        # Filter de foto's uit de bestanden van de invoer_map.
        if invoer_bestandsnaam.lower().endswith(('.heic')):
            file_path = os.path.join(invoer_map, invoer_bestandsnaam)
            try:
                with Image.open(file_path) as img:
                    # Maak bestandsnaam met jpeg inplaats van
                    uitvoer_bestandsnaam = invoer_bestandsnaam.split(".")[0] + ".jpeg"

                    # Sla de foto op in het JPEG-formaat met de nieuwe bestandsnaam.
                    img.save(os.path.join(uitvoer_map, uitvoer_bestandsnaam), 'JPEG')

            except Exception as e:
                # Geef error weer voor debugging
                print(f"Error processing {invoer_bestandsnaam}: {str(e)}")


# Maakt de invoer_map gelijk aan huidige map
invoer_map = os.path.dirname(os.path.realpath(__file__))

# Vraag de gebruiker waar de uitvoer bewaart moet worden en bewaar in uitvoer_map.
uitvoer_map = input("Wat is de uitvoer map: ")

convert_images(invoer_map, uitvoer_map)