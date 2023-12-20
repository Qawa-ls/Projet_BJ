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
font = pygame.font.SysFont(None, 60)

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

def main():
    # Initialisation du deck de cartes
    valeurs_cartes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = valeurs_cartes * 4
    random.shuffle(deck)

    # Initialisation des mains
    main_joueur = [tirer_carte(deck), tirer_carte(deck)]
    main_croupier = [tirer_carte(deck), tirer_carte(deck)]

    joueur_termine = False
    jeu_termine = False

    while not jeu_termine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if oui_bouton.collidepoint(mouse_x, mouse_y) and not joueur_termine:
                    main_joueur.append(tirer_carte(deck))
                elif non_bouton.collidepoint(mouse_x, mouse_y):
                    joueur_termine = True

        screen.fill(GREEN)

        # Affichage des mains et des scores
        text_joueur = font.render("Joueur: " + ' + '.join(main_joueur) + " = " + str(calculer_score(main_joueur)), True, BLACK)
        text_croupier = font.render("Croupier: " + ' + '.join(main_croupier) + " = " + str(calculer_score(main_croupier)), True, WHITE)
        screen.blit(text_joueur, (50, screen_height - 500))
        screen.blit(text_croupier, (50, 50))

        # Dessin des boutons
        oui_bouton = dessiner_bouton("Oui", 450, screen_height - 150, 100, 50, RED)
        non_bouton = dessiner_bouton("Non", 600, screen_height - 150, 100, 50, RED)

        pygame.display.flip()

        # Logique de tirage des cartes pour le croupier
        score_joueur = calculer_score(main_joueur)
        score_croupier = calculer_score(main_croupier)

        if joueur_termine and not jeu_termine:
            while score_croupier < 19:
                main_croupier.append(tirer_carte(deck))
                score_croupier = calculer_score(main_croupier)
                screen.fill(GREEN)
                screen.blit(text_joueur, (50, screen_height - 100))
                text_croupier = font.render("Croupier: " + ' + '.join(main_croupier) + " = " + str(calculer_score(main_croupier)), True, WHITE)
                screen.blit(text_croupier, (50, 50))
                pygame.display.flip()
                pygame.time.wait(1000)
            jeu_termine = True

    # Affichage du résultat et du bouton Recommencer
    screen.fill(BLACK)
    if score_joueur > 21:
        resultat = "Vous avez dépassé 21. Vous perdez."
    elif score_croupier > 21 or score_joueur > score_croupier:
        resultat = "Vous gagnez!"
    elif score_joueur < score_croupier:
        resultat = "Vous perdez."
    else:
        resultat = "Égalité."
    text_resultat = font.render(resultat, True, WHITE)
    screen.blit(text_resultat, (screen_width / 2 - text_resultat.get_width() / 2, screen_height / 2 - text_resultat.get_height() / 2))

    recommencer_bouton = dessiner_bouton("Recommencer", screen_width / 2 - 100, screen_height / 2 + 100, 200, 50, GOLD)
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
