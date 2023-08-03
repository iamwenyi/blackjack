import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cards_total_user = []
cards_total_comp = []
score_user = 0
score_comp = 0
show_everything = False
exit_game = False

def draw_card(cards):
    card_user_index = random.randint(0,12)
    card_user = cards[card_user_index]
    
    card_comp_index = random.randint(0,12)
    card_comp = cards[card_comp_index]
    
    cards_list = [card_user,card_comp]
    return cards_list

def calculate_score(card_user,card_comp,score_user,score_comp):
    score_user = score_user + card_user
    if score_comp < 19:
        score_comp = score_comp + card_comp
    
    score_list = [score_user,score_comp]
    return score_list

def hider(cards_total_comp):
    new_cards_comp = []
    num = 0
    
    while num < len(cards_total_comp) - 1:
        new_cards_comp.append(cards_total_comp[num])
        num = num + 1
        
    new_cards_comp.append("x")
    return new_cards_comp

def display(score_list,cards_total_user,cards_total_comp,show_everything):
    new_cards_comp = hider(cards_total_comp)
    if show_everything == True:
        print("")
        
        print("End results: ")
        print(f"Your cards: {cards_total_user}")
        print(f"Your score: {score_list[0]}")
        
        print(f"Computer's cards: {cards_total_comp}")
        print(f"Computer's score: {score_list[1]}")
    else:
        print(f"Your cards: {cards_total_user}")
        print(f"Your score: {score_list[0]}")
        print(f"Computer's cards: {new_cards_comp}")
 
play_game = input("Do you want to play Blackjack? Yes or no: ").lower()
if play_game == "yes":
    cards_list = draw_card(cards)
    cards_total_user.append(cards_list[0])
    if score_comp < 19:
        cards_total_comp.append(cards_list[1])
    score_list = calculate_score(cards_list[0],cards_list[1],score_user,score_comp)
    
    while exit_game == False: 
        if len(cards_total_user) == 1:
            cards_list = draw_card(cards)
            cards_total_user.append(cards_list[0])
            if score_comp < 19:
                cards_total_comp.append(cards_list[1])
            score_list = calculate_score(cards_list[0],cards_list[1],score_list[0],score_list[1])

        display(score_list,cards_total_user,cards_total_comp,show_everything)
        
        if score_list[0] < 21 and score_list[1] < 21:
            another_card = input("Do you want another card?: ").lower()
            print("")
            if another_card == "yes":
                cards_list = draw_card(cards)
                cards_total_user.append(cards_list[0])
                if score_comp < 19:
                    cards_total_comp.append(cards_list[1])
                score_list = calculate_score(cards_list[0],cards_list[1],score_list[0],score_list[1])
            else:
                if score_list[0] > score_list[1]:
                    exit_game = True
                    show_everything = True
                    display(score_list,cards_total_user,cards_total_comp,show_everything)
                    print("You win")
                    
                elif score_list[1] > score_list[0]:
                    exit_game = True
                    show_everything = True
                    display(score_list,cards_total_user,cards_total_comp,show_everything)
                    print("Computer wins")
                    
                else:
                    exit_game = True
                    show_everything = True
                    display(score_list,cards_total_user,cards_total_comp,show_everything)
                    print("Tied round")
                    
        elif score_list[0] == score_list[1]:
            print("")
            exit_game = True
            show_everything = True
            display(score_list,cards_total_user,cards_total_comp,show_everything)
            print("Tied round")
                
        elif score_list[0] == 21:
            exit_game = True
            show_everything = True
            display(score_list,cards_total_user,cards_total_comp,show_everything)
            print("")
            print("You win")
            
        elif score_list[0] > 21:
            exit_game = True
            show_everything = True
            display(score_list,cards_total_user,cards_total_comp,show_everything)
            print("")
            print("You lose")
            
        elif score_list[1] == 21:
            exit_game = True
            show_everything = True
            display(score_list,cards_total_user,cards_total_comp,show_everything)
            print("")
            print("Computer wins")
        
        elif score_list[1] > 21:
            exit_game = True
            show_everything = True
            display(score_list,cards_total_user,cards_total_comp,show_everything)
            print("")
            print("Computer loses")  
else:
    print("Goodbye")