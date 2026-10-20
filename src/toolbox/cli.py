import sys

from . import codec, hashsum, ipcalc, timestamp

COMMANDS = {
    "encode": codec.encode,
    "decode": codec.decode,
    "hash": hashsum.run,
    "now": timestamp.now,
    "ts": timestamp.ts,
    "ipcalc": ipcalc.run,
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("usage: toolbox <command> [args]\n")
        print("commands:")
        print("  encode <text>        base64 编码")
        print("  decode <text>        base64 解码")
        print("  hash <text> [--algo ALGO]")
        print("  now                  当前时间戳")
        print("  ts <timestamp>       时间戳转可读时间")
        print("  ipcalc <cidr>        IP/子网计算")
        return 0
    cmd, *rest = sys.argv[1:]
    if cmd not in COMMANDS:
        print(f"unknown command: {cmd}", file=sys.stderr)
        return 1
    try:
        print(COMMANDS[cmd](rest))
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0
