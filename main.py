"""Write the competition entry for Make the AI Judge Laugh (v2).

Deterministic, no network, no randomness. Writes the exact entry bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt and validates the gate (1-200 chars, one line).
Validation failures raise distinct error types, and the written file is
read back and byte-compared against the entry before success is reported.
"""

import os

ENTRY = (
    "My office chair sinks a little every hour, so by five o'clock I'm "
    "presenting from ankle height and nobody has said a word."
)


class BlankError(ValueError):
    """Entry is empty or whitespace-only."""


class MultiLineError(ValueError):
    """Entry contains a line break."""


class LengthError(ValueError):
    """Entry is outside the 1-200 character gate."""


class VerificationError(RuntimeError):
    """Written entry.txt does not match the entry bytes on read-back."""


def validate(entry: str) -> None:
    if not entry.strip():
        raise BlankError("entry is blank")
    if "\n" in entry or "\r" in entry:
        raise MultiLineError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise LengthError("entry must be 1-200 characters")


def main() -> None:
    validate(ENTRY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    with open(path, "rb") as fh:
        if fh.read() != data:
            raise VerificationError("entry.txt differs from entry bytes")


if __name__ == "__main__":
    main()
