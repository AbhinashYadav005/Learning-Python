def create_character(name, strength, intelligence, charisma):
    
    stats = (strength, intelligence, charisma)
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    if not bool(name):
        return 'The character should have a name'
    
    if len(name) > 10:
        return 'The character name is too long'
    
    if " " in name:
        return 'The character name should not contain spaces'
    
    if not all(isinstance(value, int) for value in stats):
        return 'All stats should be integers'
    
    if not all(n>=1 for n in stats):
        return 'All stats should be no less than 1'
    
    if not all(n<5 for n in stats):
        return 'All stats should be no more than 4'
    
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    
    full_dot = '●'
    empty_dot = '○'
    stren = full_dot*strength + empty_dot*(10-strength)
    intelli= full_dot*intelligence + empty_dot*(10-intelligence)
    charis = full_dot*charisma + empty_dot*(10-charisma)
    return f"{name}\nSTR {stren}\nINT {intelli}\nCHA {charis}"

print(create_character('ram',3,3,1))
