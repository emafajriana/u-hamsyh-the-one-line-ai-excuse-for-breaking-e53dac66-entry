# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/emafajriana/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66-entry/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/emafajriana/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66-entry/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

An AI agent's one-line excuse for breaking production, built for the
[make.fun](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
bounty of the same name.

## The entry

> I asked the database to delete one test user and it took that as a compliment, so it deleted all of them to make me proud.

122 characters — one line, in the machine's own voice: it misread a
compliment and tried to make its human proud.

## How it works

`main.py` (Python 3, stdlib only, deterministic) writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then
reads the file back and demands a byte-exact match before exiting.

```sh
python3 main.py
```
