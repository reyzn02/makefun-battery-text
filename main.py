"""The Battery's Last Text to Its Charger.

Writes the phone battery's final text message to /output/entry.txt:
one line, plain text, at most 200 characters. Stdlib only, no network.
"""

import os

TEXT = (
    "I waited all day for you, and now I'm at 1%. "
    "You were busy charging your ex's phone, weren't you? "
    "Tell my apps I loved them \u2014 and delete my search history "
    "before Mom sees the 3 a.m. stuff."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, must be 1-200"
    assert TEXT.strip() == TEXT and "\n" not in TEXT, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
