<!-- =============================================== -->
<!-- 🔐 bsb-Inquiry – Ultimate Enterprise Toolkit -->
<!-- =============================================== -->

<p align="center">
  <img src="https://github.com/Shawpon2/bsb-Inquiry/blob/main/BSB.png" alt="bsb-Inquiry Hero" width="480" style="border-radius:16px; box-shadow:0 10px 40px rgba(0,0,0,0.3);"/>
</p>

<h1 align="center">🔐 bsb-Inquiry</h1>
<h3 align="center">Next-Gen Web Security & Recon Framework</h3>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.6+-black?style=for-the-badge&logo=python&logoColor=yellow">
  </a>
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Linux%20|%20Windows%20|%20Mac-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Security-Research%20Tool-orange?style=for-the-badge">
</p>

---

## 🚀 Overview

**bsb-Inquiry** is an **enterprise-grade, high-performance web security toolkit** for professional security researchers and pentesters.  

**Why it stands out:**
- ⚡ Ultra-fast multi-threaded scanning engine  
- 🔎 Advanced reconnaissance & hidden endpoint discovery  
- 🛡 Intelligent vulnerability assessment  
- 🎨 Modern, colorized CLI output  
- 📈 Optimized workflow for serious security operations  

---

## 🧠 Core Modules

| Command | Module | Purpose |
|---------|--------|---------|
| `sp link <url>` | 🔗 Recon Engine | Recursive link crawling & hidden endpoint mapping |
| `sp admin <url>` | 🛡 Directory Scanner | Multi-threaded admin & sensitive path detection |
| `sp uploader <url>` | 📤 Upload Analyzer | Auto-detect upload forms & endpoints |
| `sp crack <url>` | 🔑 Auth Tester | Credential testing & injection validation |
| `sp upload <url>` | 📂 File Handler | Smart MIME & extension detection for uploads |

---

## ⚙️ Installation

### Requirements
- Python 3.6+
- pip package manager

### Install
```bash
pip install bsb-Inquiry
```

### Verify
```bash
sp --help
```

---

## 🧪 Usage Examples

```bash
# Crawl internal links
sp link https://example.com

# Find admin panels
sp admin https://example.com

# Detect upload forms
sp uploader https://example.com

# Credential testing
sp crack https://example.com

# Test file uploads
sp upload https://example.com
```

---

## 🏗 Architecture & Highlights

- Multi-threaded engine for high-speed requests  
- Modular & scalable command structure  
- Clean CLI output with color coding  
- Lightweight, fast & production-ready  

---

## 🔒 Security Philosophy

bsb-Inquiry is intended **ONLY** for:  
- Authorized penetration testing  
- Ethical hacking & security research  
- Educational cybersecurity labs  

> ❗ Unauthorized use is strictly prohibited.

---

## 📁 Project Structure

```
bsb-Inquiry/
├── core/
├── modules/
├── utils/
├── cli.py
├── setup.py
└── README.md
```

---

## 🤝 Contributing

Pull requests and improvements are welcome.  
Please open issues to discuss major changes.

---

## 📄 License

MIT License. Use responsibly.

---

<p align="center">
  <i>bsb-Inquiry — Redefining Professional Web Security Testing</i>
</p>
