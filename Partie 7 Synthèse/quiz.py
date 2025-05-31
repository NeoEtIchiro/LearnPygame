import json

class Quiz:
  def __init__(self, questions_file):
    # Charge les questions depuis un fichier JSON
    with open(questions_file, "r", encoding="utf-8") as f:
      self.questions = json.load(f)
    self.current = 0  # Index de la question courante
    self.score = 0    # Score du joueur

  def get_current_question(self):
    # Retourne la question courante ou None si terminé
    if self.current < len(self.questions):
      return self.questions[self.current]
    return None

  def answer(self, choice_index):
    # Vérifie si la réponse est correcte et passe à la question suivante
    question = self.get_current_question()
    if question and choice_index == question["answer"]:
      self.score += 1
      correct = True
    else:
      correct = False
    self.current += 1
    return correct

  def is_finished(self):
    # Indique si le quiz est terminé
    return self.current >= len(self.questions)