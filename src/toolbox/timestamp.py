import datetime as dt
import time


def now(args: list[str]) -> str:
    return f"{int(time.time())}  ({dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"


def ts(args: list[str]) -> str:
    if not args or not args[0].lstrip("-").isdigit():
        raise ValueError("usage: toolbox ts <timestamp>")
    readable = dt.datetime.fromtimestamp(int(args[0])).strftime("%Y-%m-%d %H:%M:%S")
    return readable
