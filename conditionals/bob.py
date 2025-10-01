"""Bob only ever answers one of five things:

"Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
"Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
"Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
"Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
"Whatever." This is what he answers to anything else."""

def response(hey_bob):
    hey_bob = hey_bob.strip()
    if is_yelling(hey_bob) and is_question(hey_bob):
        return "Calm down, I know what I'm doing!"
    if is_yelling(hey_bob):
        return "Whoa, chill out!"
    if is_question(hey_bob):
        return "Sure."
    if len(hey_bob) < 1:
        return "Fine. Be that way!"
    return "Whatever."


def is_yelling(hey_bob):
    return hey_bob.isupper() and any(c.isalpha() for c in hey_bob)

def is_question(hey_bob):
    return hey_bob.endswith("?")