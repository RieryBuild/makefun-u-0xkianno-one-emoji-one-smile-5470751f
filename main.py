import os

# The entry: U+1F31E SUN WITH FACE — a smiling sun, warm at first glance,
# universally read as a good day, chosen rather than a default smiley,
# and right for a stranger (no intimacy, sarcasm or flirtation).
EMOJI = "\U0001f31e"


def write_entry(out_dir, text):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), EMOJI)
