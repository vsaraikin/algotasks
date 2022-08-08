def original(n):
    cards = []
    for i in range(n):
        if len(cards) >= 2:
            last_card = cards.pop()
            cards.insert(0, last_card)
            
        current_card = i % 2
        cards.insert(0, current_card)
    
    return cards

print(original(10))