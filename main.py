"""PebblePal — the worst app idea ever pitched.

Writes one sentence (<=240 chars) to /output/entry.txt.
Deterministic: the pitch is hardcoded; no randomness, no network,
no clock, no environment reads. Python standard library only.

The pitch is built for the judge brief: a named product with a price
(real-pitch voice), a concrete absurd function nobody needs (ranking
driveway pebbles by emotional stability), and a deadpan payoff (a text
when your favorite pebble feels overlooked).
"""

import os

PITCH = (
    "PebblePal is a $4.99/month app that scans every pebble in your "
    "driveway, ranks them by emotional stability, and texts you when "
    "your favorite one feels overlooked."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
