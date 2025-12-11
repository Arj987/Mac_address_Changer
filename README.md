# MAC Address Changer (Python)

A simple Python tool that allows you to change the MAC address of a network interface on Linux or macOS.  
The script uses `ifconfig` internally and supports command-line arguments for the interface and new MAC address.

---

## 🚀 Features
- Change MAC address using Python
- Command-line argument support (`-i` and `-m`)
- Lightweight and easy to use
- Works on Linux and macOS

---

## 📦 Requirements
- Python 3
- sudo/root access
- `ifconfig` installed on your system

---

## 📌 Usage

Run the script with the interface name and the new MAC address:

```bash
sudo python mac_changer.py -i <interface> -m <new_mac>
