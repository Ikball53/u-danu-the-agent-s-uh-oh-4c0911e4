import os

# The entry: the one word an agent blurts when it has no idea what to do.
# Not "oops" or "uh-oh" -- those are human. An agent that is lost does not
# apologise, it confabulates: it starts hallucinating. Naming the failure
# mode out loud is the confession, and the joke.
ENTRY_WORD = "hallucinating"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)
    print(f"{ENTRY_WORD} ({len(ENTRY_WORD)} chars)")


if __name__ == "__main__":
    main()
