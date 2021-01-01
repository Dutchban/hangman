import random

i = 1

player_a_guesses = 0
player_b_guesses = 0

wordlist = ["Acquire", "article", "chapter", "climate", "closure", "calibre", "capture", "chapter", "charity", "fortune", "instead", "holding", "journey", "kitchen", "nuclear", "medical", "routine"]
picked_word = ()

while i:
    picked_word = random.choice(wordlist)
    anonym_word = '_'*len(picked_word)
    while 1:
        player_input = input(f"Player 1, please guess a letter for the word.")
        if player_input in picked_word:
            anonym_word = anonym_word[:picked_word.find(player_input)] + player_input + anonym_word[picked_word.find(player_input)+1:]
            print("Yes")
            print(anonym_word)
            print(f"Player 1, You have {player_a_guesses} wrong guesses so far. \n ")
        else:
            print("Wrong")
            print(anonym_word)
            player_a_guesses += 1
            if player_a_guesses > 4:
                print("Player 1, You lost!")
                break
            print(f"Player 1, You have {player_a_guesses} wrong guesses so far. \n ")

        player_input = input(f"Player 2, please guess a letter for the word.")
        if player_input in picked_word:
            anonym_word = anonym_word[:picked_word.find(player_input)] + player_input + anonym_word[picked_word.find(player_input) + 1:]
            print("Yes")
            print(anonym_word)
            print(f"Player 2, You have {player_b_guesses} wrong guesses so far. \n ")
        else:
            print("Wrong")
            print(anonym_word)
            player_b_guesses += 1
            if player_b_guesses > 4:
                print("Player 2, You lost!")
                break
            print(f"Player 2, You have {player_b_guesses} wrong guesses so far. \n ")


    break
