# **Remote WiFi Credentials Extractor**

The **Remote WiFi Credentials Extractor** is a penetration testing tool designed to extract saved WiFi credentials from target systems. By leveraging built-in system commands, it retrieves stored WiFi profiles and their passwords, generates reports, and sends the results back via Google SMTP for remote analysis.

---

## **Key Features**
- Extract saved WiFi profiles and passwords.
- Automates the credential retrieval process for efficiency.
- Sends results securely to a specified email via Google SMTP.
- Lightweight and easy to use.

---

## **Setup Instructions**
1. **Install Dependencies**:  
   Ensure Python is installed along with the required libraries (`smtplib`, `subprocess`, `re`).

2. **Update Gmail Details**:  
   - Open the script in a code editor.
   - Replace the placeholder email address and app password with your own Gmail address and app password to receive the results.  

   Example:
   ```python
   mail("your_email@gmail.com", "your_app_password", results)
### **Disclaimer**

The author of this tool are **not responsible** for any misuse or illegal activities performed with it. This tool is provided **"as is"** without any warranties, and the user assumes full responsibility for ensuring ethical and legal compliance when using the tool.

By using this tool, you acknowledge that:
1. This tool is intended solely for **ethical penetration testing** and **educational purposes**.
2. You must have **explicit written consent** from the owner of the target system before using this tool.
3. Unauthorized use of this tool for malicious purposes is strictly prohibited and may violate local, national, or international laws.

**Use this tool responsibly and only in environments where you have proper authorization.**
