#!/usr/bin/env python3
"""One Word From Grandma — score candidate words, write the winner.

The brief: send exactly one word, the single word a grandma would text
about AI. The judge weighs, most important first:
  1. reads as the single word a grandma would text about AI
  2. sounds like a real grandmother's texting voice: warm, a little baffled
  3. funny in one word, joke lands with no caption or context
  4. tied to AI, robots or machines, not a word for any subject
  5. fresh pick, not the obvious one, still instantly readable
Weights follow the brief's order: 5/4/3/2/1. Gate: UTF-8, 1-30 chars,
exactly one word, no whitespace. Output: /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

# (word, c1, c2, c3, c4, c5) — scores 1-5 per criterion, brief order.
CANDIDATES = [
    # Grandma's verdict on AI: she thinks it is witchcraft. Warm, baffled,
    # funny in one word, tied to AI as her reaction to it, and fresh —
    # nobody's first pick is a noun of suspicion.
    ("witchcraft", 5, 5, 4, 4, 4),
    # Grandma mimicking the robot's noises back at it. Tied to machines,
    # funny, but the voice is more robot than grandma.
    ("beepboop", 4, 4, 4, 5, 4),
    # Grandma's word for a robocall: she hears "robot" and blames the
    # phone calls. AI-tied, but the joke needs the robocall backstory.
    ("robocall", 4, 4, 4, 4, 3),
    # Grandma's magic word for it — same family as witchcraft, but the
    # showman's word, not the suspicious-church-lady word.
    ("hocuspocus", 4, 4, 4, 3, 4),
    # The gadget word for anything she cannot name. Perfect grandma
    # voice, but it fits a toaster as well as a chatbot.
    ("thingamajig", 4, 5, 4, 2, 3),
    # Grandma thinks the AI is Siri. Plausible text, but a brand name
    # is a weaker joke than her own verdict on the thing.
    ("siri", 4, 4, 3, 4, 3),
    # The other gadget word for anything she cannot name. Same family as
    # thingamajig, but even less tied to AI — it fits a can opener.
    ("doohickey", 3, 5, 3, 2, 3),
]

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate):
    word, *scores = candidate
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def main():
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    winner = ranked[0][0]
    # Gate: exactly one word, 1-30 chars, plain UTF-8, no whitespace.
    assert 1 <= len(winner) <= 30, "word out of gate"
    assert winner == winner.strip() and " " not in winner, "not one word"
    winner.encode("utf-8")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(winner)
    print(winner)


if __name__ == "__main__":
    main()
