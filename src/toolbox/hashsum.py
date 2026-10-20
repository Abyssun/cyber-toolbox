import hashlib

ALGOS = ("md5", "sha1", "sha256", "sha512")


def run(args: list[str]) -> str:
    algo = "sha256"
    if "--algo" in args:
        i = args.index("--algo")
        algo = args[i + 1]
        args = args[:i] + args[i + 2 :]
    if not args:
        raise ValueError("usage: toolbox hash <text> [--algo ALGO]")
    if algo not in ALGOS:
        raise ValueError(f"unsupported algo: {algo}, choose from {ALGOS}")
    text = " ".join(args)
    return hashlib.new(algo, text.encode()).hexdigest()
