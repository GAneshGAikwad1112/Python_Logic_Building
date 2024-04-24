'''
20 random cards are placed in a row, all face down. A move consists of turning a face
down card, face up and turning over the card immediately to the right. show that no matter what the choice of cards to turn, this sequence of moves must  terminate...

'''
def transform(b):
    for i in range(len(b)-1):
        if b[i]=='1':
            b[i]='0'
            if b[i + 1]=='0':
                b[i + 1] = '1'
            else:
                b[i+1] = '1'

    return b

if __name__=="__main__":
    a = list("01111110000")
    print(a)
    while a != transform(a.copy()):
       a = transform(a.copy())

    print(a)




#2nd solution

def simulate_termination(cards):
    
    # Initialize the list to keep track of face-up and face-down cards
    card_states = [False] * len(cards)  # False represents face down, True represents face up

    # Perform moves until all cards are face up
    while False in card_states:
        for i in range(len(cards)):
            if not card_states[i]:  # If the card is face down
                card_states[i] = True  # Turn it face up
                if i + 1 < len(cards):  # If there's a card to the right
                    card_states[i + 1] = not card_states[i + 1]  # Turn it over
        print(card_states)  # Print the current state of cards after each move

simulate_termination([1] * 20)  # Replace [1] * 20 with any list of 20 elements to represent the cards
