import base64


def encode(args: list[str]) -> str:
    if not args:
        raise ValueError("usage: toolbox encode <text>")
    text = " ".join(args)
    return base64.b64encode(text.encode()).decode()


def decode(args: list[str]) -> str:
    if not args:
        raise ValueError("usage: toolbox decode <text>")
    data = " ".join(args)
    return base64.b64decode(data, validate=True).decode()
