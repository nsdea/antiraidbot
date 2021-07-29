import random

def math():
    problems = [
        f'{random.randint(10, 20)} - {random.randint(0, 10)}',
        f'{random.randint(0, 10)} + {random.randint(0, 10)}',
        f'{random.randint(1, 5)} * {random.randint(1, 4)}',
    ]
    problem = random.choice(problems)
    text = f'Solve this math problem: **`{problem}`**'
    correct = str(eval(problem))
    return [text, correct]

def number():
    problem = ''
    correct = ''

    for _ in range(random.randint(2, 4)):
        number_texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        number = random.randint(0, 9)
        correct += str(number)
        problem += number_texts[number] + ' '

    text = f'Type the number: **`{problem}`**\n\n**Example:**\n> For *one three three seven*, you should type:\n> 1337'.replace(' `', '`')
    return [text, correct]
    
def get_challenge():
    return random.choice([math(), number()])

if __name__ == '__main__':
    print('\n'.join(get_challenge()))