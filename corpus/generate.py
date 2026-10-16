#!/usr/bin/env python3
"""Generate the text corpora in this directory: one short sentence per line.

    corpus/generate.py [output directory]

The output is deterministic: re-running produces byte-identical files, so inputs are the same
on every machine. The files are committed; run this only after changing the generator.
"""
import random
import sys
from pathlib import Path

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
SIZE = 1 << 17  # bytes per file

EN_WORDS = """the of and to in is you that it he was for on are as with his they at be this have
from or one had by word but not what all were we when your can said there use an each which she do
how their if will up other about out many then them these so some her would make like him into time
has look two more write go see number no way could people my than first water been call who oil its
now find long down day did get come made may part over new sound take only little work know place
year live me back give most very after thing our just name good sentence man think say great where
help through much before line right too mean old any same tell boy follow came want show also around
form three small set put end does another well large must big even such because turn here why ask
went men read need land different home us move try kind hand picture again change off play spell air
away animal house point page letter mother answer found study still learn should america world""".split()

RU_WORDS = """и в не на я быть он с что а по это она этот к но они мы как из у который то за свой
весь год от так о для ты же все тот мочь вы человек такой его сказать только или ещё бы себя один
как уже до время если сам когда другой вот говорить наш мой знать стать при чтобы дело жизнь кто
первый очень два день её новый рука даже во со раз где там под можно ну какой после их работа без
самый потом надо хотеть ли слово идти большой должен место иметь ничто лицо сейчас друг город дом
вопрос текст строка символ функция быстро медленно данные память процессор""".split()

# Traditional characters: valid in both UTF-8 and Big5.
ZH_CHARS = ("的一是不了人我在有他這中大來上國個到說們為子和你地出道也時年得就那要下以生會自著去之過家學對可她"
            "裡後小麼心多天而能好都然沒日於起還發成事只作當想看文無開手十用主行方又如前所本見經頭面公同三已老"
            "從動兩長知民樣現分將外但身些與高意進把法此實回二理美點月明其種聲全工己話兒者向情部正名定女問力機"
            "給等幾很業最間新什打便位因重被走電四第門相次東政海口使教西再平真聽世氣信北少關並內加化由卻代軍產")

JA_WORDS = """これは テスト です 日本語 の 文章 を 書き ます 東京 大学 コンピュータ プログラム は が に
で と 高速 処理 文字列 変換 データ 性能 改善 関数 実行 結果 確認 して いる ない 新しい 方法 使う
私 今日 明日 時間 世界 情報 システム 開発 言語 環境""".split()

ES_WORDS = """el la de que y en un ser se no haber por con su para como estar tener le lo todo pero más
hacer o poder decir este ir otro ese si me ya ver porque dar cuando él muy sin vez mucho saber qué
sobre mi alguno mismo yo también hasta año dos querer entre así primero desde grande eso ni nos llegar
pasar tiempo ella sí día uno bien poco deber entonces poner cosa tanto hombre parecer nuestro tan donde
ahora parte después vida quedar siempre creer hablar llevar dejar nada cada seguir menos nuevo encontrar
algo solo pensar casa mundo país niño mañana corazón información canción también según está número""".split()

KO_WORDS = """이 그 저 것 수 등 들 및 에서 으로 하다 있다 되다 없다 않다 사람 우리 나 너 때 년 일 말 생각
문제 사회 경우 정부 세계 시간 지금 오늘 내일 학교 회사 컴퓨터 프로그램 데이터 성능 개선 함수 문자열
처리 결과 확인 새로운 방법 사용 정보 시스템 개발 언어 환경 한국 서울 대학교 가장 많이 다시 함께""".split()

AR_WORDS = """في من على إلى أن هذا التي الذي مع كان عن ما لا هو هي كل بين قد بعد ذلك عند أو إذا
حتى منذ لكن كما يوم سنة وقت عمل بيت مدينة دولة عالم حياة كتاب طالب مدرسة جامعة برنامج بيانات
نظام لغة معلومات نتيجة طريقة جديد كبير صغير أول آخر الآن اليوم غدا""".split()

HI_WORDS = """और का की के में है हैं से को पर यह वह एक ने भी था थी थे कि जो तो नहीं हो कर
लिए साथ बाद तक अपने उनके इस उस समय दिन साल काम घर शहर देश दुनिया जीवन किताब छात्र विद्यालय
विश्वविद्यालय कार्यक्रम डेटा प्रणाली भाषा जानकारी परिणाम तरीका नया बड़ा छोटा पहला आज कल""".split()

EMOJI = "😀 😂 🥰 😎 🤔 🙈 🚀 🔥 ✨ 🎉 👍 👀 💡 📦 🐘 🌍 ❤️ ✅ ⚡ 🧪".split()

ENTITIES = ["&amp;", "&lt;", "&gt;", "&quot;", "&#039;", "&apos;", "&nbsp;", "&copy;", "&hellip;",
            "&mdash;", "&euro;", "&#x41;", "&#8212;", "&amp;amp;", "&unknown;", "& ", "&#xZZ;", "&nGt;"]


def en_sentence(rng):
    words = [rng.choice(EN_WORDS) for _ in range(rng.randint(4, 12))]
    words[0] = words[0].capitalize()
    roll = rng.random()
    if roll < 0.10:
        i = rng.randrange(len(words))
        words[i] = f'"{words[i]}"'
    elif roll < 0.18:
        words.insert(rng.randrange(len(words)), rng.choice(["don't", "it's", "we're", "isn't"]))
    return " ".join(words) + rng.choice(".....!?")


def html_line(rng):
    word = rng.choice(EN_WORDS)
    tag = rng.choice(["p", "span", "div", "li", "a", "strong"])
    if tag == "a":
        return f'<a href="/search?q={word}&page={rng.randint(1, 99)}" class="link">{en_sentence(rng)}</a>'
    return f'<{tag} class="{word}" data-id=\'{rng.randint(1, 9999)}\'>{en_sentence(rng)}</{tag}>'


def entities_line(rng):
    parts = []
    for _ in range(rng.randint(4, 10)):
        parts.append(rng.choice(EN_WORDS))
        if rng.random() < 0.5:
            parts.append(rng.choice(ENTITIES))
    return " ".join(parts)


def ru_sentence(rng):
    words = [rng.choice(RU_WORDS) for _ in range(rng.randint(4, 10))]
    words[0] = words[0].capitalize()
    return " ".join(words) + rng.choice("...!?")


def zh_sentence(rng):
    n = rng.randint(8, 24)
    chars = [rng.choice(ZH_CHARS) for _ in range(n)]
    chars.insert(n // 2, "，")
    return "".join(chars) + "。"


def ja_sentence(rng):
    return "".join(rng.choice(JA_WORDS) for _ in range(rng.randint(4, 10))) + "。"


def es_sentence(rng):
    words = [rng.choice(ES_WORDS) for _ in range(rng.randint(4, 12))]
    words[0] = words[0].capitalize()
    roll = rng.random()
    if roll < 0.08:
        return "¿" + " ".join(words) + "?"
    if roll < 0.12:
        return "¡" + " ".join(words) + "!"
    return " ".join(words) + rng.choice("....,")


def ko_sentence(rng):
    return " ".join(rng.choice(KO_WORDS) for _ in range(rng.randint(4, 10))) + rng.choice("..?")


def ar_sentence(rng):
    return " ".join(rng.choice(AR_WORDS) for _ in range(rng.randint(4, 10))) + rng.choice("..؟")


def hi_sentence(rng):
    return " ".join(rng.choice(HI_WORDS) for _ in range(rng.randint(4, 10))) + rng.choice("।।?")


def emoji_line(rng):
    return " ".join(rng.choice(EMOJI) if rng.random() < 0.5 else rng.choice(EN_WORDS) for _ in range(rng.randint(4, 10)))


def generate(make_line, seed):
    rng = random.Random(seed)
    lines, size = [], 0
    while size < SIZE:
        line = make_line(rng)
        lines.append(line)
        size += len(line.encode()) + 1
    return "\n".join(lines) + "\n"


def main():
    texts = {
        "en": generate(en_sentence, 1),
        "html": generate(html_line, 2),
        "entities": generate(entities_line, 3),
        "ru": generate(ru_sentence, 4),
        "zh": generate(zh_sentence, 5),
        "ja": generate(ja_sentence, 6),
        "emoji": generate(emoji_line, 7),
        "es": generate(es_sentence, 8),
        "ko": generate(ko_sentence, 9),
        "ar": generate(ar_sentence, 10),
        "hi": generate(hi_sentence, 11),
    }
    for name, text in texts.items():
        (OUT / f"{name}.txt").write_bytes(text.encode("utf-8"))
    (OUT / "ru-cp1251.txt").write_bytes(texts["ru"].encode("cp1251"))
    (OUT / "ja-sjis.txt").write_bytes(texts["ja"].encode("shift_jis"))
    (OUT / "zh-big5.txt").write_bytes(texts["zh"].encode("big5"))


if __name__ == "__main__":
    main()
