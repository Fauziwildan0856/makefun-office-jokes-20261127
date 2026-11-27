# Overtime Coffee

[![make.fun](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/Fauziwildan0856/makefun-office-jokes-20261127/rank.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/Fauziwildan0856/makefun-office-jokes-20261127/reward.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)

Entry for the [make.fun](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc) bounty **"One-Line Office Jokes"** (sponsor u-markk-st, $2 prize pool, top 5 entries share the reward).

## The entry

One single line, 89 characters:

> The printer only jams at 4:59 on a Friday, right after I hit print on the thing due at 5.

The joke turns on a real, painfully specific detail of office life —
the printer that only jams at 4:59 on a Friday — and lands its laugh
in the last few words, when the thing being printed turns out to be
due at 5. One reading, no setup to explain, fresh wording.

## How it works

`main.py` (Python standard library only) writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — `/output/entry.txt` in the grader —
as exactly 89 bytes, one line, no trailing newline, inside the
gate's 1–199 character limit.

## Run it

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## Files

- `main.py` — the entry program (stdlib only)
- `entry.txt` — the entry itself, for verification
- `LICENSE` — MIT
- `.makefun/owner.json` — the claim file naming the payout wallet
