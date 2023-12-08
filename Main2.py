import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blackjack")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Charger les images des cartes (à remplacer par les chemins de vos images)
# Exemple : card_images['A'] = pygame.image.load('chemin_vers_image_as.png')
card_images = {}

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

def dessiner_main(main, x, y):
    for carte in main:
        screen.blit(card_images[carte], (x, y))
        x += 70  # Espacement entre les cartes

# Boucle principale du jeu
def jeu_blackjack():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    main_joueur = [tirer_carte(deck), tirer_carte(deck)]
    main_croupier = [tirer_carte(deck), tirer_carte(deck)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GREEN)

        # Afficher les mains
        dessiner_main(main_joueur, 50, screen_height - 150)
        dessiner_main(main_croupier, 50, 50)

        pygame.display.flip()

jeu_blackjack()
pygame.quit()
