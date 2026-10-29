import random
random.seed(7)

# Balanced multilingual snippets (no language dominates), as a moderation feed would see.
snippets = {
    'en': 'the quick brown fox jumps over the lazy dog and posts a comment here ',
    'es': 'el veloz zorro marron salta sobre el perro perezoso y el nino escribe ',
    'ru': 'быстрая коричневая лиса прыгает через ленивую собаку и пишет коммент ',
    'zh': '敏捷的棕色狐狸跳过了懒狗然后在这里留下了一条评论内容 ',
    'ja': 'すばしこい茶色のきつねが怠け者の犬を飛び越えてコメントを書く ',
    'ko': '빠른 갈색 여우가 게으른 개를 뛰어넘고 여기에 댓글을 남긴다 ',
    'emoji': '😀 great post 👍🏽 love it 🔥 so true 💯 lol 😂 ',
}
keys = list(snippets)
out = []
total = 0
while total < 48000:
    s = snippets[random.choice(keys)]
    out.append(s)
    total += len(s.encode())
data = ''.join(out)
open('corpus/multilang.txt', 'wb').write(data.encode())
print('multilang.txt bytes', len(data.encode()))
