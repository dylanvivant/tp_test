"""Module de gestion des notes d'étudiants."""


class Etudiant:
    """Classe représentant un étudiant avec ses notes."""

    def __init__(self, nom, age):
        """
        Initialise un nouvel étudiant.
        
        Args:
            nom (str): Le nom de l'étudiant
            age (int): L'âge de l'étudiant
        """
        self.nom = nom
        self.age = age
        self.notes = []

    def ajouter_note(self, note):
        """
        Ajoute une note à l'étudiant.
        
        Args:
            note (float): La note à ajouter
        """
        self.notes.append(note)

    def moyenne(self):
        """
        Calcule la moyenne des notes de l'étudiant.
        
        Returns:
            float: La moyenne des notes, ou 0 si aucune note
        """
        if not self.notes:
            return 0
        total = 0
        for note in self.notes:
            total += note
        return total / len(self.notes)


def afficher_infos(etudiant):
    """
    Affiche les informations d'un étudiant.
    
    Args:
        etudiant (Etudiant): L'étudiant dont afficher les informations
    """
    print("Nom de l'étudiant :", etudiant.nom)
    print("Âge :", etudiant.age)
    print("Moyenne :", etudiant.moyenne())


def main():
    """Fonction principale du programme."""
    etudiant = Etudiant("Alice", 20)
    etudiant.ajouter_note(14)
    etudiant.ajouter_note(16)
    etudiant.ajouter_note(18)  # Corrigé : 18 au lieu de "18"
    afficher_infos(etudiant)


if __name__ == "__main__":
    main()
