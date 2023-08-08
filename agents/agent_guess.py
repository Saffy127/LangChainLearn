class GuessingAgent:
    def __init__(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.guess = 50

    def get_guess(self):
        return self.guess

    def update_guess(self, feedback):
        if feedback == "higher":
            self.lower_bound = self.guess + 1
        elif feedback == "lower":
            self.upper_bound = self.guess - 1
        
        self.guess = (self.lower_bound + self.upper_bound) // 2


# Simulate the agent guessing a number
target_number = 72  # The number the agent is trying to guess
agent = GuessingAgent()

for _ in range(10):  # Limit the number of guesses to 10
    guess = agent.get_guess()
    print(f"Agent guesses: {guess}")

    if guess < target_number:
        agent.update_guess("higher")
    elif guess > target_number:
        agent.update_guess("lower")
    else:
        print("Agent guessed the correct number!")
        break
else:
    print("Agent did not guess the number within 10 tries.")
