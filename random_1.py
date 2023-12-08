import random

class BlackjackMultiplayer:
    def __init__(self, num_joueurs):
        self.deck = self.creer_deck()
        self.mains = {f'Joueur {i+1}': [] for i in range(num_joueurs)}
        self.main_croupier = []
        self.jeu_termine = False

    def creer_deck(self):
        couleurs = ['Coeurs', 'Carreaux', 'Trèfles', 'Piques']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        deck = [{'Couleur': couleur, 'Valeur': valeur} for couleur in couleurs for valeur in valeurs]
        random.shuffle(deck)
        return deck

    def piocher_carte(self):
        return self.deck.pop()

    def calculer_score(self, main):
        score = 0
        compte_as = 0
        for carte in main:
            if carte['Valeur'] in ['Valet', 'Dame', 'Roi']:
                score += 10
            elif carte['Valeur'] == 'As':
                compte_as += 1
                score += 11
            else:
                score += int(carte['Valeur'])
        
        while score > 21 and compte_as:
            score -= 10
            compte_as -= 1
        
        return score

    def commencer_jeu(self):
        for main in self.mains.values():
            main.append(self.piocher_carte())
            main.append(self.piocher_carte())

        self.main_croupier.append(self.piocher_carte())
        self.main_croupier.append(self.piocher_carte())

        for joueur, main in self.mains.items():
            print(f"{joueur} main: {main}, Score: {self.calculer_score(main)}")
        print(f"Main du croupier: [{self.main_croupier[0]}, {'Cachée'}]")

    def tour_joueur(self, joueur, main):
        while True:
            choix = input(f"{joueur}, voulez-vous tirer une carte (oui/non) ? ").lower()
            if choix == 'oui':
                main.append(self.piocher_carte())
                score = self.calculer_score(main)
                print(f"{joueur} main: {main}, Score: {score}")
                if score > 21:
                    print(f"{joueur} a dépassé 21. Perdu.")
                    return False
            else:
                return True

    def tour_croupier(self):
        while self.calculer_score(self.main_croupier) < 17:
            self.main_croupier.append(self.piocher_carte())

    def verifier_gagnant(self, joueur, main):
        score_joueur = self.calculer_score(main)
        score_croupier = self.calculer_score(self.main_croupier)

        print(f"{joueur} Score final: {score_joueur}")
        print(f"Score final du croupier: {score_croupier}")

        if score_croupier > 21 or score_joueur > score_croupier:
            print(f"{joueur} a gagné !")
        elif score_croupier == score_joueur:
            print(f"{joueur} et le croupier ont égalité.")
        else:
            print(f"Le croupier gagne contre {joueur}.")

    def jouer(self):
        self.commencer_jeu()
        for joueur, main in self.mains.items():
            if not self.jeu_termine:
                joueur_reste = self.tour_joueur(joueur, main)
                if not joueur_reste:
                    self.jeu_termine = True
        
        if not self.jeu_termine:
            self.tour_croupier()
            print(f"Main finale du croupier: {self.main_croupier}, Score: {self.calculer_score(self.main_croupier)}")

        if not self.jeu_termine:
            for joueur, main in self.mains.items():
                self.verifier_gagnant(joueur, main)

# Lancement du jeu pour 3 joueurs
jeu = BlackjackMultiplayer(3)
jeu.jouer()
