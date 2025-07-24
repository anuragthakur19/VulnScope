# 🔍 Website Vulnerability Scanner

A simple web-based tool to check any website for common security issues and risks.

## 📌 What It Does

This project scans a given domain name and gives you a basic security analysis. Here's what it checks:

- ✅ **Security Headers**: Looks for missing HTTP headers that help protect websites.
- ✅ **Open Ports**: Uses Nmap to detect exposed ports on the server.
- ✅ **Geo Info**: Shows where the website's server is located.
- ✅ **Risk Score & Verdict**: Gives a simple risk level (Low, Medium, High) based on findings.
- ✅ **Summary Report**: Easy-to-understand summary for non-technical users.
- ✅ **Dark Theme UI + Animated Scanner Loader**: Clean and comfortable interface with feedback during scans.

---

## 🧠 Who It's For

Anyone curious about website security:

- Students learning about web security
- Developers checking their own sites
- Non-tech users who want a simple explanation of website risks

---

## 🛠 Tech Stack

- **Frontend**: Flask + HTML/CSS (with gradient + dark theme UI)
- **Backend**: FastAPI (for performing scans)
- **Scanner Tools**: Nmap, HTTP Header Checker, IP Geolocation API

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/website-vulnerability-scanner.git
   cd website-vulnerability-scanner
