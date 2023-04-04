# Задача 2.4.

print('\nПункт A.')
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    y=list(s)
    while y.count("!")!=0:
        y.remove('!')
    k="".join(y)
    print(f'\"{k}\"')
    pass
remove_exclamation_marks("Hi! Hello!")
remove_exclamation_marks("!!!!")
remove_exclamation_marks("O!h, no!!!")

print ("\nПункт B.")
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1]=="!":
        print(s[0:-1])
    else:
        print(s)
    pass
remove_last_em("Hi!")
remove_last_em("Hi!!!")
remove_last_em("!Hi")

# Дополнительно

print("\nПункт С.")
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    s=s.split(' ')
    for item in tuple(s):
        x=item.count('!')
        if x==1:
            s.remove(item)
    k=''.join(s)
    print(f'\"{k}\"')
    pass
remove_word_with_one_em("Hi!")
remove_word_with_one_em("Hi! Hi!")
remove_word_with_one_em("Hi! Hi! Hi!")
remove_word_with_one_em("Hi Hi! Hi!")
remove_word_with_one_em("Hi! !Hi Hi!")
remove_word_with_one_em("Hi! Hi!! Hi!")
remove_word_with_one_em("Hi! !Hi! Hi!")

# Отлично) Решение третьего пункта можно написать покороче

def remove_word_with_one_em(s):
    return ' '.join([w for w in s.split(' ') if w.count('!')!=1])

print(remove_word_with_one_em("Hi! Hi!! Hi!"))
