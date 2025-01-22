def main():
    # Chemin vers le fichier contenant le texte du livre
    book_path = "books/frankenstein.txt"

    # Lire le texte du livre
    text = get_book_text(book_path)

    # Compter le nombre de mots dans le texte
    num_words = get_num_words(text)

    # Compter la fréquence de chaque caractère
    character_counts = get_num_characters(text)

    # Générer et afficher un rapport formaté
    print_report(book_path, num_words, character_counts)


def get_num_words(text):
    """
    Compte le nombre de mots dans une chaîne de caractères.

    Args:
        text (str): Le texte à analyser.

    Returns:
        int: Le nombre de mots dans le texte.
    """
    words = text.split()  # Diviser le texte en mots
    return len(words)  # Retourner le nombre total de mots


def get_num_characters(text):
    """
    Compte le nombre de fois que chaque caractère apparaît dans une chaîne,
    en ignorant la casse et en regroupant les majuscules et minuscules.

    Args:
        text (str): Le texte à analyser.

    Returns:
        dict: Un dictionnaire où chaque clé est un caractère (str),
              et la valeur associée est le nombre de fois où ce caractère apparaît (int).
    """
    text = text.lower()  # Convertir le texte en minuscules
    characters = {}  # Initialiser un dictionnaire pour les fréquences

    for char in text:  # Parcourir chaque caractère dans le texte
        if char in characters:  # Si le caractère est déjà dans le dictionnaire
            characters[char] += 1  # Incrémenter sa fréquence
        else:
            characters[char] = 1  # Ajouter le caractère au dictionnaire avec une fréquence de 1

    return characters  # Retourner le dictionnaire des fréquences


def print_report(book_path, num_words, character_counts):
    """
    Génère et affiche un rapport contenant le nombre de mots et la fréquence des caractères.

    Args:
        book_path (str): Le chemin vers le fichier du livre.
        num_words (int): Le nombre total de mots dans le livre.
        character_counts (dict): Un dictionnaire contenant la fréquence de chaque caractère.
    """
    # Filtrer les caractères alphabétiques et trier par fréquence décroissante
    sorted_characters = sorted(
        [{"char": char, "num": count} for char, count in character_counts.items() if char.isalpha()],
        key=lambda x: x["num"],  # Trier par le nombre d'occurrences
        reverse=True  # Trier en ordre décroissant
    )

    # Afficher le rapport formaté
    print(f"--- Début du rapport pour {book_path} ---")
    print(f"{num_words} mots trouvés dans le document\n")

    for item in sorted_characters:  # Parcourir les caractères triés
        print(f"Le caractère '{item['char']}' apparaît {item['num']} fois")

    print(f"--- Fin du rapport ---")


def get_book_text(path):
    """
    Lit le contenu d'un fichier et le retourne sous forme de chaîne de caractères.

    Args:
        path (str): Le chemin du fichier à lire.

    Returns:
        str: Le contenu du fichier ou une chaîne vide en cas d'erreur.
    """
    try:
        with open(path) as f:  # Ouvrir le fichier en mode lecture
            return f.read()  # Lire et retourner le contenu
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{path}' est introuvable.")
        return ""  # Retourner une chaîne vide si le fichier n'existe pas
    except PermissionError:
        print(f"Erreur : Permission refusée pour lire le fichier '{path}'.")
        return ""  # Retourner une chaîne vide si les permissions sont insuffisantes
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
        return ""  # Retourner une chaîne vide en cas d'autre erreur


# Point d'entrée principal du script
if __name__ == "__main__":
    main()


