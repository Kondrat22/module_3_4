def single_root_words(root_word, *other_words):
    same_words = list()
    list_words = list(other_words)
    lowercase_list = [s.lower() for s in list_words]
    root_word_lower = root_word.lower()
    for i in range(len(lowercase_list)):
        if (root_word_lower in lowercase_list[i]) or (lowercase_list[i] in root_word_lower):
            same_words.append(list_words[i])
    return same_words


result_1 = single_root_words(
    'кот', 'котёнок', 'косметолог', 'теракотовый', 'пинкод', 'котлован')
print(result_1)
result_2 = single_root_words(
    'низкотемпературный', 'кот', 'собака', 'темп', 'Австралия', 'тур', )
print(result_2)
