# Cisco Automation Scripts

A small collection of Python scripts for connecting to and backing up the configuration of a Cisco device, built against the public **Cisco DevNet IOS XR Always-On Sandbox**. This repository holds academic work exploring network automation with [Netmiko](https://github.com/ktbyers/netmiko).

---

## Contents

| File | Description |
|------|-------------|
| `test_conn.py` | Opens an SSH session to the IOS XR sandbox and runs `show install active summary` to verify connectivity. |
| `backup.py` | Connects to the device, pulls the full running configuration (`show running-config`), and saves it to a timestamped file like `xr_config_YYYY-MM-DD_HH-MM.txt`. |
| `config_2026-04-10_13-27.txt` | A sample running-config backup produced by `backup.py`. |

---

## Requirements

- Python 3.8+
- [Netmiko](https://pypi.org/project/netmiko/)

Install dependencies:

```bash
pip install netmiko
```

---

## Target Device

These scripts target Cisco's public sandbox:

- **Host:** `sandbox-iosxr-1.cisco.com`
- **Port:** `22` (SSH)
- **Platform:** Cisco IOS XR

You'll need a free Cisco DevNet account to obtain valid sandbox credentials. See the [Cisco DevNet Sandbox page](https://devnetsandbox.cisco.com/) for current login details.

---

## Usage

### Test the connection

```bash
python test_conn.py
```

Expected output: a successful SSH handshake followed by the device's installed-software summary.

### Back up the running configuration

```bash
python backup.py
```

On success, a new file named `xr_config_<timestamp>.txt` will be written to the current working directory.

---

## Purpose

This repository is a personal academic workspace — nothing here is production-grade. It exists to document my learning around SSH-based network automation with Python and Netmiko.

---

## License

No license specified. All content is for personal academic use.
