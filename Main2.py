import pygame
import random

pygame.init()

# Paramètres de la fenêtre
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blackjack")

# Initialisation des polices
font = pygame.font.SysFont(None, 48)

# Initialisation du deck de cartes
valeurs_cartes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = valeurs_cartes * 4
random.shuffle(deck)

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

# Initialisation des mains
main_joueur = [tirer_carte(deck), tirer_carte(deck)]
main_croupier = [tirer_carte(deck), tirer_carte(deck)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # h pour "hit"
                main_joueur.append(tirer_carte(deck))
            elif event.key == pygame.K_s:  # s pour "stand"
                running = False

    screen.fill((0, 0, 0))

    # Afficher les mains et les scores
    text_joueur = font.render("Joueur: " + ' '.join(main_joueur) + " Score: " + str(calculer_score(main_joueur)), True, (255, 255, 255))
    text_croupier = font.render("Croupier: " + ' '.join(main_croupier) + " Score: " + str(calculer_score(main_croupier)), True, (255, 255, 255))
    screen.blit(text_joueur, (50, screen_height - 50))
    screen.blit(text_croupier, (50, 50))

    pygame.display.flip()

# Logique de fin de jeu
score_joueur = calculer_score(main_joueur)
score_croupier = calculer_score(main_croupier)

while score_croupier < 17:
    main_croupier.append(tirer_carte(deck))
    score_croupier = calculer_score(main_croupier)

# Déterminer le gagnant
screen.fill((0, 0, 0))
if score_joueur > 21:
    resultat = "Vous avez dépassé 21. Vous perdez."
elif score_croupier > 21 or score_joueur > score_croupier:
    resultat = "Vous gagnez!"
elif score_joueur < score_croupier:
    resultat = "Vous perdez."
else:
    resultat = "Égalité."

text_resultat = font.render(resultat, True, (255, 255, 255))
screen.blit(text_resultat, (screen_width / 2 - text_resultat.get_width() / 2, screen_height / 2 - text_resultat.get_height() / 2))
pygame.display.flip()

pygame.time.wait(5000)
pygame.quit()
