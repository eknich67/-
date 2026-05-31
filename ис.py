import random

styles = ['мартов', 'сентябрь', 'ультрамартов']
months = {'января': 31, 'февраля': 28, 'марта': 31, 'апреля': 30, 'мая': 31, 'июня': 30, 'июля': 31, 'августа': 31, 'сентября': 30, 'октября': 31, 'ноября': 30, 'декабря': 31}
months_names = list(months.keys())

def is_leap_year(year_sm):
    modern_year_approx = year_sm - 5508
    return modern_year_approx % 4 == 0

def calculate_indict(year_sm, style, month):
    base_indict = year_sm % 15
    if base_indict == 0:
        base_indict = 15
    
    if style == 'сентябрь':
        return base_indict
    elif style == 'мартов':
        if month in ['марта', 'апреля', 'мая', 'июня', 'июля', 'августа']:
            return base_indict
        else:
            indict = base_indict + 1
            return 15 if indict == 16 else indict
    elif style == 'ультрамартов':
        if month in ['сентября', 'октября', 'ноября', 'декабря', 'января', 'февраля']:
            return base_indict
        else:
            indict = base_indict - 1
            return 15 if indict == 0 else indict
    return base_indict

for _ in range(10):
    style = random.choice(styles)
    month = random.choice(months_names)
    year = random.randint(6300, 7209)
    
    if month == 'февраля':
        max_days = 29 if is_leap_year(year) else 28
    else:
        max_days = months[month]
    
    date = random.randint(1, max_days)
    correct_answer = year
    
    if style == styles[0]:
        if month == 'января' or month == 'февраля':
            correct_answer -= 5507
        else:
            correct_answer -= 5508
    elif style == styles[2]:
        if month == 'января' or month == 'февраля':
            correct_answer -= 5508
        else:
            correct_answer -= 5509
    else:
        if month == 'сентября' or month == 'октября' or month == 'ноября' or month == 'декабря':
            correct_answer -= 5509
        else:
            correct_answer -= 5508
            
    print(f'''Переведите в современную систему летосчисления дату,
приведённую по {style}скому стилю:
{date} {month} {year} года.''')
    
    while True:
        print('Введите год (или "помощь" для подсказки):')
        answer_input = input('> ')
        
        if answer_input.lower() == 'помощь':
            print('''
=== ПОДСКАЗКА ===
Для перевода из разных стилей:
- Мартовский стиль: с января по февраль - вычитаем 5507, с марта по декабрь - вычитаем 5508
- Сентябрьский стиль: с сентября по декабрь - вычитаем 5509, с января по август - вычитаем 5508
- Ультрамартовский стиль: с января по февраль - вычитаем 5508, с марта по декабрь - вычитаем 5509
''')
            continue
        
        try:
            answer = int(answer_input)
            break
        except ValueError:
            print('Ошибка! Введите число или "помощь" для подсказки.')
    
    if answer == correct_answer:
        print('Молодец! У тебя получилось!')
    else:
        print(f'''Что-то не сходится.
Правильный ответ: {correct_answer}''')
    
    correct_indict = calculate_indict(year, style, month)
    
    while True:
        print(f'Определите индикт для {date} {month} {year} года по {style}скому стилю(или "помощь" для подсказки):')
        indict_input = input('> ')
        
        if indict_input.lower() == 'помощь':
            base = year % 15 if year % 15 != 0 else 15
            print(f'''
=== ПОДСКАЗКА ДЛЯ ИНДИКТА ===
Значение индикта - это остаток после деления года на 15

Правила:
- Для сентябрьского стиля: индикт = базовому (постоянен весь год)
- Для мартовского стиля: с марта по август = базовый, с сентября по февраль = базовый + 1
- Для ультрамартовского стиля: с сентября по февраль = базовый, с марта по август = базовый - 1

Если при делении получается 0, то индикт = 15
''')
            continue
        
        try:
            indict_answer = int(indict_input)
            break
        except ValueError:
            print('Пожалуйста, введите число или "помощь" для подсказки.')
    
    if indict_answer == correct_indict:
        print('Молодец! Индикт определён верно!\n')
    else:
        print(f'Что-то не сходится. Правильный индикт: {correct_indict}\n')
