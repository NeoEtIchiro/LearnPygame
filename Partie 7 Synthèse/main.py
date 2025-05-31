from quiz import Quiz
from ui import QuizUI

def main():
  # Crée une instance du quiz en chargeant les questions depuis le fichier JSON
  quiz = Quiz("Partie 7 Synthèse\questions.json")
  # Crée l'interface utilisateur pour le quiz
  ui = QuizUI(quiz)
  # Lance la boucle principale du jeu
  ui.run()

if __name__ == "__main__":
  # Point d'entrée du programme
  main()