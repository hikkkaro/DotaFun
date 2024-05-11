import customtkinter as ctk
from PIL import Image
import random
import os
from data.lists import *
import time

class GenerateNick:

    def __init__(self):
        self.ghoul_count = 0
        self.ghoul_count_need = random.randint(3, 6)
        self.symbols = list(
            "彡༒☬☠️♕彡༒☬☠️♕乡☬牡マキグ⛥⛥⛥⛥⛥ナルファマキグナルファ系路克瑞大阪市立学鎰命科ャマ能力ϒ人は妻スティ要通り玉宏¥サ丹谷Ѫ灯影伝鶐能力ϒ人は妻スティ私はディックを吸う六怒り"
        )
        self.aor = ["", "or feed", "or leave", "or afk", "or suicide",
                    "или пудж с момкой", "или фид", "или лес", "or jungle"]
        self.sfix = [
            lambda: "zxc" * random.randint(1, 4),
            lambda: "zxc" * random.randint(1, 4),
            lambda: f'{random.randint(0, 6)}-{random.randint(0, 6)} pos {random.choice(self.aor)}',
            lambda: f'{random.randint(0, 10)}к узник',
            lambda: "dead inside",
            lambda: "dead inside",
            lambda: "dead outside",
            lambda: self.warp_symbols("дед внутри", 0, 2),
            lambda: "clown",
            lambda: self.warp_symbols("rotting", 0, 2),
            lambda: self.warp_symbols("мёртв", 0, 2),
            lambda: "мёртв внутри",
            lambda: self.warp_symbols("anti social", 0, 2),
            lambda: "anti social",
            lambda: "crying",
            lambda: self.warp_symbols("eternal despair", 0, 2),
            lambda: self.warp_symbols("eternal tilted", 0, 2),
            lambda: self.warp_symbols("blood tears", 0, 2),
            lambda: "hurt",
            lambda: "hopeless",
            lambda: f'{random.randint(8, 17)} y.o.',
            lambda: self.warp_symbols("sad", 0, 3),
            lambda: "sad",
            lambda: "1000-7",
            lambda: "чудище",
            lambda: "hate",
            lambda: "all mute",
            lambda: self.warp_symbols("hate", 0, 2),
            lambda: "666" * random.randint(1, 3),
            lambda: self.warp_symbols("bury me alive", 1, 3),
            lambda: '"i tired of this place"',
            lambda: self.warp_symbols("плевать на всех", 1, 3),
            lambda: self.warp_symbols("no brain", 0, 2),
            lambda: self.warp_symbols("feeling alive", 1, 3),
            lambda: "mode:",
            lambda: "mode:",
            lambda: "mode:",
            lambda: "pudge abuzer",
            lambda: "sf abuzer",
            lambda: "loser",
            lambda: "depressed",
            lambda: self.warp_symbols("white prince", 0, 3),
            lambda: self.warp_symbols("throw down your tears", 0, 2),
            lambda: "faceless",
            lambda: self.warp_symbols("emptiness", 0, 2),
            lambda: "hollow",
            lambda: "numbness",
            lambda: "suffered",
            lambda: "senseless",
            lambda: "abandoned",
            lambda: self.warp_symbols("everlasting hate", 0, 3),
            lambda: self.warp_symbols("let me die", 0, 3),
            lambda: "fearless",
            lambda: self.warp_symbols("blessed", 0, 2),
            lambda: "hopeless",
            lambda: self.warp_symbols("obsessed", 0, 2),
            lambda: "numb the pain",
            lambda: "tragic",
            lambda: self.warp_symbols("immortal", 0, 2),
            lambda: "weak",
            lambda: "rebellious",
            lambda: self.warp_symbols("cursed", 0, 2),
            lambda: self.warp_symbols("zxc god", 0, 3),
            lambda: self.warp_symbols("zxc king", 0, 3),
            lambda: self.warp_symbols("zxc demon", 0, 3),
            lambda: self.warp_symbols("zxc beast", 0, 3),
            lambda: "damaged",
            lambda: self.warp_symbols("dying as a lifestyle", 1, 3),
            lambda: self.warp_symbols("hate me as you do", 1, 2),
            lambda: self.warp_symbols("tilted", 0, 2),
            lambda: self.warp_symbols("ugly god", 0, 3),
            lambda: self.warp_symbols("ugly god", 0, 3),
            lambda: "дед инсайд если че",
            lambda: "broken",
            lambda: self.warp_symbols("kill me", 0, 3),
            lambda: "death",
            lambda: self.warp_symbols("death", 1, 3),
            lambda: "ghoul",
            lambda: self.warp_symbols("ghoul", 1, 3),
            lambda: self.warp_symbols("pain", 1, 3),
            lambda: self.warp_symbols("pain", 1, 3),
            lambda: random.choice(self.symbols),
            lambda: f"{random.randint(0, 9)}k pts",
            lambda: f'{random.choice(["SSS", "SS+", "SS", "S+", "S", "A", "B", "C"])} ранг',
            lambda: self.warp_symbols("drain", 0, 3),
            lambda: self.warp_symbols("schizophrenic", 0, 3),
            lambda: self.warp_symbols("emotionless", 0, 3),
            lambda: self.warp_symbols("chen abuzer", 0, 3),
            lambda: self.warp_symbols("amulet abuzer", 0, 3),
            lambda: self.warp_symbols("psiblades abuzer", 0, 3),
            lambda: "warden abuzer",
            lambda: "╰‿╯",
            lambda: "zitrax mode",
            lambda: self.warp_symbols("𝖌𝖍𝖔𝖚𝖑", 0, 3),
            lambda: self.warp_symbols("solo", 0, 3),
            lambda: "igrushka otchima",
            lambda: "watch me die",
            lambda: "nocturnal",
            lambda: self.warp_symbols("genius", 0, 3),
            lambda: self.warp_symbols("hatred", 0, 3),
            lambda: self.warp_symbols("doomed", 0, 3),
            lambda: self.warp_symbols("shining", 0, 3),
            lambda: self.warp_symbols("fearful", 0, 3),
            lambda: self.warp_symbols("bleeding", 0, 3),
            lambda: "demon",
            lambda: self.warp_symbols("leprotic", 0, 3),
            lambda: self.warp_symbols("savage", 0, 3),
            lambda: self.warp_symbols("epileptic", 0, 3),
            lambda: self.warp_symbols("drain", 0, 3),
            lambda: self.warp_symbols("crying", 0, 3),
            lambda: self.warp_symbols("anxiety", 0, 3),
            lambda: self.warp_symbols("toxic", 0, 3),
            lambda: self.warp_symbols("paranoid", 0, 3),
            lambda: self.warp_symbols("suicidal", 0, 3),
            lambda: self.warp_symbols("bipolar", 0, 3),
            lambda: "humiliated",
            lambda: self.warp_symbols("talentless", 0, 3),
        ]

    def warp_symbols(self, n, r, e):
        t = random.randint(r, e)
        o = ""
        for _ in range(t):
            o += random.choice(self.symbols)
        return f"{o}{n}{o[::-1]}"

    def generate(self):

        self.ghoul_count += 1

        if self.ghoul_count == self.ghoul_count_need:
            self.ghoul_count = 0
            self.ghoul_count_need = random.randint(3, 6)

        n = random.randint(2, 4)
        r = list(range(len(self.sfix)))
        e = ""
        for _ in range(n):
            index = random.choice(r)
            e += self.sfix[index]() + " "
            r.remove(index)

        return e