# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1 Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны
# иметь заглавные первые буквы. email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем
# регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или
# com. Например: Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол,
# заглавная буква, .net), te_4_st@test.com - верно указан.
import re


pattern_name = '^[A-Z]{1}[a-z]+[^A-Z]$'
pattern_email = '[a-z_0-9]+@[a-zA-Z0-9]+\.(ru|org|com)'

name = input('Введите имя: ')
sername = input('Введите фамилию: ')
email = input('Введите электронную почту: ')

if not re.match(pattern_name, name):
    print('Неверно указано имя')
if not re.match(pattern_name, sername):
    print('Неверно указана фамилия')
if not re.match(pattern_email, email):
    print('Неверно указан email')


# Задача - 2:
# Вам дан текст:

pattern = '\.{2}'
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

if re.search(pattern, some_str):
    print('В тексте встречаются точки более одного раза подряд')
else:
    print('В тексте не встречаются точки более одного раза подряд')

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!
