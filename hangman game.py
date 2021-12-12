import random 

def hangman():
    list_of_word=['india','laptop','monkey','hangman',"C++","Python","HtmlCss","JavaScript"]
    word=random.choice(list_of_word)
    turns=5
    
    guessmade= " "
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=" "
        missed=0
        
        for letter in word:
            if letter in guessmade:
                main_word+=letter
            else:
                main_word+="_ "
        if main_word==word:
            print(main_word)
            print('you won')
            break
        
        print('guess the word',main_word)
        guess=input()
        if guess in valid_entry:
            guessmade+=guess
        else:
            print('enter again')
            guess=print()
        if guess not in word:
            turns-=1
            if turns==5:
                print("5 turns left")
            if turns==4:
                print("4 turns left")
                print("   \O/  ")
            if turns==3:
                print("3 turns left")
                print("   \O/  ")
                print("    |   ")
                print("   / \   ")
            
            if turns==2:
                print("2 turns left")
                print("   \O/ -----| ")
                print("    |       |")
                print("   / \   ")     
            if turns==1:
                print("only 1 turns left_Save the person")
                print("   \O/ -----| ")
                print("    |       |")
                print("   / \   ")  
            if turns==0:
                print("you lose") 
                break          
                            
    
    

name=input('Enter your name --> ')
print("Welcome...",name)
print("*.................*")
print('Try guessing the word in 5 attempts...')

hangman()