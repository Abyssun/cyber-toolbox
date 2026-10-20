import ipaddress


def run(args: list[str]) -> str:
    if not args:
        raise ValueError("usage: toolbox ipcalc <cidr>")
    net = ipaddress.ip_network(args[0], strict=False)
    return "\n".join([
        f"network:   {net.network_address}",
        f"netmask:   {net.netmask}",
        f"broadcast: {net.broadcast_address}",
        f"hosts:     {net.num_addresses}",
    ])
