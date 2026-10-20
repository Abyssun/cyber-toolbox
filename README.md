# cyber-toolbox

CTF / 日常安全常用小工具集合。纯标准库实现，无第三方依赖。

## 安装

```bash
pip install -e .
```

## 使用

```bash
# Base64
toolbox encode "hello"
toolbox decode "aGVsbG8="

# 哈希
toolbox hash "hello"            # 默认 sha256
toolbox hash "hello" --algo md5

# 时间戳
toolbox now                     # 当前时间戳与可读时间互转
toolbox ts 1760000000

# IP / 子网计算
toolbox ipcalc 192.168.1.0/24
```

## 开发

```bash
pip install -e . pytest ruff
pytest          # 运行测试
ruff check .    # 代码检查
```

## 路线图

- [ ] URL 编解码
- [ ] Hex / ROT13
- [ ] 字典处理（去重、合并、切割）
- [ ] JWT 解析（不校验签名，仅解码）
