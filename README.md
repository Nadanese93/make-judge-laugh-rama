# Make the AI Judge Laugh

[![Bounty](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/Nadanese93/make-judge-laugh-rama/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/Nadanese93/make-judge-laugh-rama/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

A one-line joke about office life for the Make the AI Judge Laugh bounty
(2 USDC prize pool, program/v1).

## How it works

`main.py` writes the entry to `entry.txt` inside the directory named by the
MAKEFUN_OUTPUT_DIR environment variable.
UTF-8, one line, 1-200 characters, and about office life. The program is
deterministic, uses no network and no randomness, and validates the entry
before writing: it must be non-blank, a single line, and within the length
limit.

## Run

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

## License

MIT — see `LICENSE`.
