"""The Meeting That Should Have Been an Email — make.fun entry.

Writes the one-line entry to /output/entry.txt.
"""

LINE = (
    "Nine people spent forty-five minutes deciding this meeting "
    "should have been an email \u2014 then booked a follow-up to discuss sending it."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 chars"
    assert LINE.strip(), "entry must not be only whitespace"
    # The gate reads exactly this file, so never add a trailing newline.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"entry written ({len(LINE)} chars): {LINE}")


if __name__ == "__main__":
    main()
