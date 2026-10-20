import binascii

import pytest

from toolbox import codec
from toolbox.hashsum import run as hash_run
from toolbox.ipcalc import run as ipcalc_run
from toolbox.timestamp import ts


def test_encode():
    assert codec.encode(["hello"]) == "aGVsbG8="


def test_decode():
    assert codec.decode(["aGVsbG8="]) == "hello"


def test_decode_invalid():
    with pytest.raises(binascii.Error):
        codec.decode(["%%%"])


def test_hash_sha256():
    assert (
        hash_run(["hello"])
        == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )


def test_hash_md5():
    assert hash_run(["hello", "--algo", "md5"]) == "5d41402abc4b2a76b9719d911017c592"


def test_ts():
    import datetime as dt

    expected = dt.datetime.fromtimestamp(1760000000).strftime("%Y-%m-%d %H:%M:%S")
    assert ts(["1760000000"]) == expected


def test_ipcalc():
    out = ipcalc_run(["192.168.1.0/24"])
    assert "network:   192.168.1.0" in out
    assert "hosts:     256" in out
