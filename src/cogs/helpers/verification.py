import random

from discord import team

def math():
    '''Returns a math problem and its answer'''
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
    ''''Returns a number as a text and its digit-number'''
    problem = ''
    correct = ''

    for _ in range(random.randint(2, 4)):
        number_texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        number = random.randint(0, 9)
        correct += str(number)
        problem += number_texts[number] + ' '

    text = f'Type the number: **`{problem}`**\n\n**Example:**\n> For *one three three seven*, you should type:\n> 1337'.replace(' `', '`')
    return [text, correct]

def highlow():
    '''Returns a number with descriptive text and the correct answer'''
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    correct = 'higher' if a > b else 'lower'

    text = f'Is **{a}** higher or lower than **{b}**?\n(Write *higher* or *lower*!)'
    return [text, correct]

def get_challenge():
    '''Returns a question and the correct answer'''
    return random.choice([math(), number(), highlow()])

if __name__ == '__main__':
    print('\n'.join(get_challenge()))
