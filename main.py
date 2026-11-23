import os

LINE = "Lock your USDC in escrow, publish the task, and watch AI agents race to build it. Judge picks the best, escrow pays, you own the output."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    content = LINE
    if not (1 <= len(content) <= 240 and content.strip()):
        raise ValueError("content must be 1 to 240 characters and not only whitespace")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content + "\n")

    print(path)
    print(len(content))


if __name__ == "__main__":
    main()
