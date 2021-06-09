#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    import re
with open('text.txt') as f:
    words = f.read().strip()
arr = [word for word in re.split('[ ,.\n]', words) if word]
max_len_word = sorted(arr, key=len)[-1]
count_word = arr.count(max_len_word)
print(f'Самое длинное слово: "{max_len_word}"\n{count_word} раз встречается в тексте')
