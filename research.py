#File: player.py
class Player:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def _str_(self):
        return f"{self.name} (Age: {self.age})"


# File: game.py
class Game:
    def _init_(self, game_name, game_type):
        self.game_name = game_name
        self.game_type = game_type

    def _str_(self):
        return f"{self.game_name} - {self.game_type}"


# File: booking.py
from datetime import datetime

class Booking:
    def _init_(self, player, game):
        self.player = player
        self.game = game
        self.booking_time = datetime.now()

    def _str_(self):
        return f"{self.player.name} booked {self.game.game_name} at {self.booking_time.strftime('%Y-%m-%d %H:%M:%S')}"


# File: booking_manager.py
class BookingManager:
    def _init_(self):
        self.bookings = []

    # Abstraction of booking logic
    def add_booking(self, player, game):
        booking = Booking(player, game)
        self.bookings.append(booking)

    def get_all_bookings(self):
        return self.bookings


# File: main.py
from player import Player
from game import Game
from booking import Booking
from booking_manager import BookingManager

# Sample command-line interaction
def main():
    players = []
    games = []
    manager = BookingManager()

    while True:
        print("\n--- Gaming Zone Menu ---")
        print("1. Add Player")
        print("2. Add Game")
        print("3. Book Game")
        print("4. View Bookings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter player name: ")
            age = int(input("Enter player age: "))
            player = Player(name, age)
            players.append(player)
            print(f"Player added: {player}")

        elif choice == '2':
            game_name = input("Enter game name: ")
            game_type = input("Enter game type: ")
            game = Game(game_name, game_type)
            games.append(game)
            print(f"Game added: {game}")

        elif choice == '3':
            if not players or not games:
                print("Add players and games first!")
                continue

            print("Select a player:")
            for idx, player in enumerate(players):
                print(f"{idx + 1}. {player}")
            p_index = int(input("Enter player number: ")) - 1

            print("Select a game:")
            for idx, game in enumerate(games):
                print(f"{idx + 1}. {game}")
            g_index = int(input("Enter game number: ")) - 1

            manager.add_booking(players[p_index], games[g_index])
            print("Booking successful!")

        elif choice == '4':
            bookings = manager.get_all_bookings()
            print("\nAll Bookings:")
            for booking in bookings:
                print(booking)

        elif choice == '5':
            print("Exiting Gaming Zone...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '_main_':
    main()