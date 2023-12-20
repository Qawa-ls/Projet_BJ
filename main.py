import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blackjack")

# Initialisation des polices
font = pygame.font.SysFont(None, 36)

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (48, 128, 20)
RED = (205, 0, 0)
GOLD = (255, 193, 37)

# Fonctions du jeu
def tirer_carte(deck):
    return deck.pop()

def calculer_score(main):
    score = 0
    as_count = 0
    for carte in main:
        if carte in ['J', 'Q', 'K']:
            score += 10
        elif carte == 'A':
            as_count += 1
            score += 11
        else:
            score += int(carte)

    while score > 21 and as_count:
        score -= 10
        as_count -= 1

    return score

def dessiner_bouton(texte, x, y, largeur, hauteur, couleur):
    bouton = pygame.draw.rect(screen, couleur, (x, y, largeur, hauteur))
    text = font.render(texte, True, WHITE)
    screen.blit(text, (x + (largeur - text.get_width()) / 2, y + (hauteur - text.get_height()) / 2))
    return bouton

def selection_nombre_joueurs():
    nb_joueurs = 0
    boutons_nb_joueurs = []
    for i in range(1, 5):
        boutons_nb_joueurs.append(dessiner_bouton(f"{i} Joueur(s)", 150 * i, 100, 100, 50, GOLD))

    pygame.display.flip()

    while nb_joueurs == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i, bouton in enumerate(boutons_nb_joueurs):
                    if bouton.collidepoint(mouse_x, mouse_y):
                        nb_joueurs = i + 1
                        return nb_joueurs

def main():
    nb_joueurs = selection_nombre_joueurs()
    mains_joueurs = [[] for _ in range(nb_joueurs)]
    scores_joueurs = [0] * nb_joueurs
    joueur_actuel = 0
    jeu_termine = [False] * nb_joueurs

    # Initialisation du deck de cartes
    valeurs_cartes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = valeurs_cartes * 4
    random.shuffle(deck)

    # Distribution des cartes initiales
    for main in mains_joueurs:
        main.extend([tirer_carte(deck), tirer_carte(deck)])

    main_croupier = [tirer_carte(deck), tirer_carte(deck)]

    while not all(jeu_termine):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if oui_bouton.collidepoint(mouse_x, mouse_y) and not jeu_termine[joueur_actuel]:
                    mains_joueurs[joueur_actuel].append(tirer_carte(deck))
                    scores_joueurs[joueur_actuel] = calculer_score(mains_joueurs[joueur_actuel])
                    if scores_joueurs[joueur_actuel] >= 21:
                        jeu_termine[joueur_actuel] = True
                        joueur_actuel = (joueur_actuel + 1) % nb_joueurs
                elif non_bouton.collidepoint(mouse_x, mouse_y):
                    jeu_termine[joueur_actuel] = True
                    joueur_actuel = (joueur_actuel + 1) % nb_joueurs

        screen.fill(GREEN)

        # Affichage des mains et des scores des joueurs
        for i, main in enumerate(mains_joueurs):
            main_str = ' + '.join(str(carte) for carte in main)  # Convertir chaque carte en chaîne de caractères
            score_joueur = calculer_score(main)
            text = font.render(f"Joueur {i + 1}: {main_str} = {score_joueur}", True, WHITE if i == joueur_actuel else BLACK)
            screen.blit(text, (50, 50 + i * 30))

        # Affichage de la main du croupier
        text_croupier = font.render("Croupier: " + ' + '.join(main_croupier) + " = " + str(calculer_score(main_croupier)), True, WHITE)
        screen.blit(text_croupier, (50, screen_height - 100))

        # Dessin des boutons
        oui_bouton = dessiner_bouton("Oui", 450, screen_height - 150, 100, 50, RED)
        non_bouton = dessiner_bouton("Non", 600, screen_height - 150, 100, 50, RED)

        pygame.display.flip()

    # Tirage des cartes pour le croupier
    while calculer_score(main_croupier) < 17:
        main_croupier.append(tirer_carte(deck))
        screen.fill(GREEN)
        for i, main in enumerate(mains_joueurs):
            text = font.render(f"Joueur {i + 1}: {' + '.join(main)} = {scores_joueurs[i]}", True, BLACK)
            screen.blit(text, (50, 50 + i * 30))
        text_croupier = font.render("Croupier: " + ' + '.join(main_croupier) + " = " + str(calculer_score(main_croupier)), True, WHITE)
        screen.blit(text_croupier, (50, screen_height - 100))
        pygame.display.flip()
        pygame.time.wait(1000)

    # Affichage du résultat
    screen.fill(BLACK)
    score_croupier = calculer_score(main_croupier)
    for i, score in enumerate(scores_joueurs):
        if score > 21:
            resultat = f"Joueur {i + 1} a dépassé 21. Vous perdez."
        elif score_croupier > 21 or score > score_croupier:
            resultat = f"Joueur {i + 1} gagne!"
        elif score < score_croupier:
            resultat = f"Joueur {i + 1} perd."
        else:
            resultat = f"Joueur {i + 1} : Égalité."
        text_resultat = font.render(resultat, True, WHITE)
        screen.blit(text_resultat, (screen_width / 2 - text_resultat.get_width() / 2, 30 + i * 30))

    recommencer_bouton = dessiner_bouton("Recommencer", screen_width / 2 - 100, screen_height - 100, 200, 50, GOLD)
    pygame.display.flip()

    # Attente de l'action de l'utilisateur
    recommencer = False
    while not recommencer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if recommencer_bouton.collidepoint(mouse_x, mouse_y):
                    recommencer = True

    return recommencer

# Boucle de jeu
jeu_en_cours = True
while jeu_en_cours:
    jeu_en_cours = main()

pygame.quit()
