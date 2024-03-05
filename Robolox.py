class Player:
    def __init__(self, name, health=100, coins=0):
        self.name = name
        self.health = health
        self.coins = coins

    def take_damage(self, damage):
        self.health -= damage

    def collect_coins(self, amount):
        self.coins += amount

    def display_status(self):
        print(f"Name: {self.name}, Health: {self.health}, Coins: {self.coins}")


def main():
    # Create two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Display initial status
    player1.display_status()
    player2.display_status()

    # Simulate some actions
    player1.take_damage(20)
    player2.collect_coins(50)

    # Display updated status
    player1.display_status()
    player2.display_status()


if __name__ == "__main__":
    main()
