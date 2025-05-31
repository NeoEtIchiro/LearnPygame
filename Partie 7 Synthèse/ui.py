import pygame
import json
import os

SCORES_FILE = "scores.json"
USERS_FILE = "users.json"
SAVE_FILE = "save.json"

class QuizUI:
    def __init__(self, quiz):
        # Demande le nom de l'utilisateur au lancement
        self.username = self.ask_username()
        pygame.init()
        self.quiz = quiz
        self.screen = pygame.display.set_mode((600, 400))  # Crée la fenêtre du jeu
        pygame.display.set_caption("Quiz Game")             # Titre de la fenêtre
        self.font = pygame.font.SysFont(None, 28)           # Police pour le texte
        self.clock = pygame.time.Clock()                    # Pour gérer le temps/rafraîchissement
        self.selected = 0                                   # Index de la réponse sélectionnée
        self.feedback = ""                                  # Message de retour après validation
        self.waiting_for_validation = True                  # Attend la validation de la réponse
        self.best_score = self.load_best_score()            # Charge le meilleur score sauvegardé
        # Tente de charger une sauvegarde si elle existe
        self.load_progress()

    def ask_username(self):
        # Demande le nom de l'utilisateur dans le terminal
        username = input("Entrez votre nom d'utilisateur : ")
        return username.strip() if username.strip() else "Joueur"

    def load_best_score(self):
        # Charge le meilleur score de l'utilisateur depuis le fichier USERS_FILE
        if os.path.exists(USERS_FILE):
            try:
                with open(USERS_FILE, "r", encoding="utf-8") as f:
                    users = json.load(f)
                # Retourne le meilleur score de l'utilisateur si existant
                return max(users.get(self.username, [])) if self.username in users and users[self.username] else 0
            except Exception:
                return 0
        return 0

    def save_score(self, score):
        # Sauvegarde le score de l'utilisateur dans USERS_FILE
        users = {}
        if os.path.exists(USERS_FILE):
            try:
                with open(USERS_FILE, "r", encoding="utf-8") as f:
                    users = json.load(f)
            except Exception:
                users = {}
        if self.username not in users:
            users[self.username] = []
        users[self.username].append(score)
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f)
        # Met à jour le meilleur score pour l'affichage
        self.best_score = max(users[self.username])

    def save_progress(self):
        # Sauvegarde la progression actuelle dans SAVE_FILE
        data = {
            "username": self.username,
            "current": self.quiz.current,
            "score": self.quiz.score,
            "selected": self.selected
        }
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load_progress(self):
        # Charge la progression si une sauvegarde existe pour cet utilisateur
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # Si la sauvegarde correspond à l'utilisateur courant, on restaure la progression
                if data.get("username") == self.username:
                    self.quiz.current = data.get("current", 0)
                    self.quiz.score = data.get("score", 0)
                    self.selected = data.get("selected", 0)
            except Exception:
                pass

    def delete_progress(self):
        # Supprime la sauvegarde après la fin du quiz
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)

    def draw_question(self, question):
        # Affiche la question courante et les choix de réponses
        self.screen.fill((255, 255, 255))  # Fond blanc
        # Affiche le meilleur score en haut de la fenêtre
        best_score_text = self.font.render(f"Meilleur score ({self.username}) : {self.best_score}", True, (200, 0, 0))
        self.screen.blit(best_score_text, (20, 10))
        y = 40
        # Affiche la question
        question_text = self.font.render(question["question"], True, (0, 0, 0))
        self.screen.blit(question_text, (30, y))
        y += 50
        # Affiche chaque choix de réponse
        for i, choice in enumerate(question["choices"]):
            color = (0, 0, 255) if i == self.selected else (0, 0, 0)  # Bleu si sélectionné
            choice_text = self.font.render(f"{i+1}. {choice}", True, color)
            self.screen.blit(choice_text, (50, y))
            y += 40
        # Affiche le feedback (bonne/mauvaise réponse)
        if self.feedback:
            feedback_text = self.font.render(self.feedback, True, (0, 128, 0))
            self.screen.blit(feedback_text, (30, 300))

    def draw_score(self, score, total):
        # Affiche l'écran de fin avec le score et le meilleur score
        self.screen.fill((255, 255, 255))  # Fond blanc
        best_score_text = self.font.render(f"Meilleur score ({self.username}) : {self.best_score}", True, (200, 0, 0))
        self.screen.blit(best_score_text, (20, 10))
        text = self.font.render(f"Quiz terminé ! Score : {score}/{total}", True, (0, 0, 0))
        self.screen.blit(text, (120, 180))

    def run(self):
        # Boucle principale du jeu
        running = True
        score_saved = False  # Pour ne sauvegarder le score qu'une seule fois
        while running:
            question = self.quiz.get_current_question()  # Récupère la question courante
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Sauvegarde la progression avant de quitter
                    self.save_progress()
                    running = False
                elif event.type == pygame.KEYDOWN and question and self.waiting_for_validation:
                    # Navigation dans les choix avec les flèches
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(question["choices"])
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(question["choices"])
                    # Validation de la réponse avec Entrée
                    elif event.key == pygame.K_RETURN:
                        correct = self.quiz.answer(self.selected)
                        self.feedback = "Bonne réponse !" if correct else "Mauvaise réponse !"
                        self.waiting_for_validation = False  # Attend une touche pour passer à la suite
                elif event.type == pygame.KEYDOWN and not self.waiting_for_validation:
                    # Appuyer sur n'importe quelle touche pour passer à la question suivante
                    self.feedback = ""
                    self.waiting_for_validation = True
                    self.selected = 0  # Réinitialise la sélection pour la prochaine question

            # Affichage de la question ou de l'écran de score final
            if question and not self.quiz.is_finished():
                self.draw_question(question)
            else:
                # Sauvegarde le score une seule fois à la fin du quiz
                if not score_saved:
                    self.save_score(self.quiz.score)
                    self.delete_progress()  # Supprime la sauvegarde à la fin du quiz
                    score_saved = True
                self.draw_score(self.quiz.score, len(self.quiz.questions))
            pygame.display.flip()  # Rafraîchit l'affichage
            self.clock.tick(30)    # Limite à 30 FPS
        pygame.quit()  # Ferme proprement Pygame à la fin