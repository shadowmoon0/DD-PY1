def get_count_char(str_):
    dict = {}
    str_ = str_.lower()
    for i in range(len(str_)):
        if (str_[i] in dict.keys()) and (str_[i].isalpha()):
            dict[str_[i]] += 1
        elif str_[i].isalpha():
            dict[str_[i]] = 1
    def get_percent(dict_):
        dict1 = {}
        s = 0
        for i in dict_:
            s += dict_[i]
        for i in dict_:
            dict1[i] = dict_[i]/s * 100
        dict_ = dict1
        return dict_


    return dict
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


