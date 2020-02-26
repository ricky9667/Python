def convert(ch):
    english = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/- "
    chinese = "ㄅㄆㄇㄈㄉㄊㄋㄌˇㄍㄎㄏˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙一ㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ "
    
    return chinese[english.index(ch)] if ch in english else ch

print()
print("============ Chinese Zhuyin Translator ============")
print()
print("Input your english (with zhuyin) and it will be converted to zhuyin")
print("Example: 5j4up z0 u4")
print("Will be converted to: ㄓㄨˋ一ㄣ ㄈㄢ 一ˋ")
print()
print("If you want to type english in your zhuyin you can use `` to cover it")
print("Example: ji32k72;304z;4y94 `github`")
print("Will be converted to: ㄨㄛˇㄉㄜ˙ㄉㄤˇㄢˋㄈㄤˋㄗㄞˋ github")
print()
print("===================================================")

sentence = input("Input your sentence: ")
size = len(sentence)
translate = True
for index in range(size):
    if sentence[index] == '`':
        translate = not translate
        continue

    if translate: 
        print(convert(sentence[index]), end='')
    else:
        print(sentence[index], end='')