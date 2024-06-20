def get_user_choice():
    user_choice = input("Escolha pedra, papel ou tesoura: ").lower()
    while user_choice not in ['pedra', 'papel', 'tesoura']:
        user_choice = input("Escolha inválida. Por favor, escolha pedra, papel ou tesoura: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['pedra', 'papel', 'tesoura']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == 'pedra' and computer_choice == 'tesoura') or \
         (user_choice == 'papel' and computer_choice == 'pedra') or \
         (user_choice == 'tesoura' and computer_choice == 'papel'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def play_game():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Você escolheu: {user_choice}")
    print(f"O computador escolheu: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
