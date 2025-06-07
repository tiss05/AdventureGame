import re
import numpy as np
import random
from typing import List

class AdventureGame:
    def __init__(self):
        self.grid_size = 10
        self.grid = np.full((self.grid_size, self.grid_size), True)
        self.row = self.col = self.grid_size // 2
        self.grid[self.row, self.col] = False
        self.adopted = ['Labrador']
        self.animals_list = self._initialize_animals_list()
        self.visited = set()
        self.visited.add((self.row, self.col))
        self.marker = 'U'

    def _initialize_animals_list(self) -> List[str]:
        return [
            'Golden Retriever', 'Bulldog', 'Beagle', 'Poodle', 'Rottweiler',
            'Siamês', 'Persa', 'Maine Coon', 'Bengal', 'Sphynx',
            'Shih Tzu', 'Pug', 'Dálmata', 'Yorkshire', 'Pastor Alemão',
            'Chihuahua', 'Boxer', 'Maltês', 'Husky', 'Street Cat',
            'Basset', 'Cocker Spaniel', 'Pomeranian', 'Doberman', 'Vira-lata',
            'Scottish Fold', 'Abyssinian', 'Siberian', 'Ragdoll', 'British Shorthair',
            'Angora', 'Birman', 'Chartreux', 'Norwegian Forest', 'Russian Blue',
            'Exotic Shorthair', 'Oriental', 'Japanese Bobtail', 'Manx', 'Cornish Rex',
            'Devon Rex', 'Turkish Angora', 'Wild Cat', 'Sphynx', 'Ocicat',
            'American Shorthair', 'Burmese', 'Tonkinese', 'Munchkin', 'Ragamuffin'
        ]

    def ask_user_name(self) -> None:
        self.user_name = input("Qual é o seu nome? ").strip()
        if len(self.user_name) > 0:
            self.marker = self.user_name[0].upper()
        else:
            self.marker = 'U'

    def print_welcome_message(self) -> None:
        print(f"\n~~~~~~ \033[1mAventura Animal: Busca por um Lar ~~~~~~\033[0m \n")
        self._print_grid()
        print(f"\n*** O {self.user_name} inicia na casa {self.row}, {self.col} com um Labrador adotado ***\n")

    def _print_grid(self) -> None:
        display = np.full((self.grid_size, self.grid_size), '.', dtype='<U1')
        for (r, c) in self.visited:
            display[r, c] = self.marker
        for i in range(self.grid_size):
            print(' '.join(display[i]))

    def move_player(self, direction: str) -> bool:
        direction = direction.upper()
        new_row, new_col = self.row, self.col

        if direction == 'N' and self.row > 0:
            new_row = self.row - 1
        elif direction == 'S' and self.row < self.grid_size - 1:
            new_row = self.row + 1
        elif direction == 'E' and self.col < self.grid_size - 1:
            new_col = self.col + 1
        elif direction == 'O' and self.col > 0:
            new_col = self.col - 1
        else:
            print(f"Movimento {direction} inválido.")
            return False

        if (new_row, new_col) != (self.row, self.col):
            self.row, self.col = new_row, new_col
            self.visited.add((self.row, self.col))
            if self.grid[self.row, self.col]:
                self.grid[self.row, self.col] = False
                self.adopted.append(random.choice(self.animals_list))
        return True

    def get_user_directions(self) -> str:
        while True:
            directions = input("Coordenadas (NSEO): ").strip().upper()
            if re.fullmatch(r'^[NSEO]+$', directions):
                return directions
            print("Indicações incorretas. Use apenas N, S, E ou O. Tente novamente!\n")

    def print_results(self) -> None:
        print("\n======= Resultado Final da Aventura =======")
        self._print_grid()
        print(f"\n\033[1mTotal de animais adotados:\033[0m {len(self.adopted)}")
        print("Animais adotados:", ', '.join(self.adopted), "\n")

    def play(self) -> None:
        self.ask_user_name()
        self.print_welcome_message()
        directions = self.get_user_directions()
        for direction in directions:
            if not self.move_player(direction):
                break
        self.print_results()

if __name__ == "__main__":
    game = AdventureGame()
    game.play()
