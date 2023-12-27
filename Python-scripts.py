import os
from pydub import AudioSegment
from pydub.playback import play

def is_muziekbestand(bestandsnaam):
    # Definieer extensies van muziekbestanden
    muziek_extensies=['.mp3','.wav','.flac','.ogg','.m4a']
    return any(bestandsnaam.lower().endswith(ext) for ext in muziek_extensies)

def convert_to_mp3(invoer_map, uitvoer_map):
    # Als de uitvoer_map niet bestaat, maak die dan.
    if not os.path.exists(uitvoer_map):
        os.makedirs(uitvoer_map)

        # Voor elk bestand in de invoer_map.
    for bestandsnaam in os.listdir(invoer_map):
         # Filter de muziek uit de bestanden van de invoer_map.
        if is_muziekbestand(bestandsnaam):
            bestandspad = os.path.join(invoer_map, bestandsnaam)

            try:
                # Converteer elk muziekbestand naar mp3-formaat
                convert_to_mp3(bestandspad, uitvoer_map)

            except Exception as e:
                # Geef error weer voor debugging
                print(f"Error processing {bestandsnaam}: {str(e)}")

if __name__ == "__main__":
    # Maak de invoermap gelijk aan de huidige map.
    invoer_map = os.path.dirname(os.path.realpath(__file__))

    # Vraag de gebruiker waar de uitvoermap moet worden opgeslagen en sla deze op in uitvoermap.
    uitvoer_map = input("Wat is de uitvoermap: ")

    convert_to_mp3(invoer_map, uitvoer_map)
