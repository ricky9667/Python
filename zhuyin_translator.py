def converter(ch):
    global t
    t = not t if ch == '`' else t
    english = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/- "
    chinese = "ㄅㄆㄇㄈㄉㄊㄋㄌˇㄍㄎㄏˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙一ㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ "
    return chinese[english.index(ch)] if ch in english and t else (ch if ch in english else "")


def init_messages():
    print("\n============ Chinese Zhuyin Translator ============\n")
    print("Input your english (with zhuyin) and it will be converted to zhuyin")
    print("Example: 5j4up z0 u4")
    print("Will be converted to: ㄓㄨˋ一ㄣ ㄈㄢ 一ˋ")
    print("\nIf you want to type english in your zhuyin you can use `` to cover it")
    print("Example: ji32k72;304z;4y94 `github`")
    print("Will be converted to: ㄨㄛˇㄉㄜ˙ㄉㄤˇㄢˋㄈㄤˋㄗㄞˋ github\n")
    print("===================================================")


def main():
    print(''.join(list(map(converter, input("Input your sentence: ")))))


if __name__ == "__main__":
    t = True
    init_messages()
    main()
