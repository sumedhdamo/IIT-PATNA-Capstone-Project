import os
from datetime import datetime
import yagmail

# --- Config ---
BASE_DIR = r'\\W10-CLIENT\ADReports'
LOG_FILE = r'E:\ADReportScript\ad_health_log.txt'
SENDER = 'damodare.sumedh@gmail.com'
APP_PASSWORD = 'vXxxxx xxxxX'
RECIPIENTS = ['damodare.sumedh@gmail.com', 'damodaresumedh5@gmail.com']

def get_latest_txt(folder_path):
    txts = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    return sorted(txts, reverse=True)[0] if txts else None

def extract_failures(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if "failed test" in line.lower()]

def process_folder(folder):
    folder_path = os.path.join(BASE_DIR, folder)
    if not os.path.isdir(folder_path):
        return None
    latest_txt = get_latest_txt(folder_path)
    if not latest_txt:
        return f"\n✔️ {folder}\n   ⚠️ No DCDIAG (.txt) file found."
    dcdiag_path = os.path.join(folder_path, latest_txt)
    failures = extract_failures(dcdiag_path)
    if failures:
        fail_str = "\n".join(f"      - {f}" for f in failures)
        return f"\n✔️ {folder}\n   📄 Latest DCDIAG report: {latest_txt}\n   ❌ DCDIAG Failures:\n{fail_str}"
    else:
        return f"\n✔️ {folder}\n   📄 Latest DCDIAG report: {latest_txt}\n   ✅ DCDIAG: All tests are passed."

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    header = f"\n📋 Active Directory Health Report – {today}\n📁 Reading report folders from: {BASE_DIR}\n"
    try:
        dc_folders = os.listdir(BASE_DIR)
        reports = [process_folder(f) for f in dc_folders]
        reports = [r for r in reports if r]
    except Exception as e:
        reports = [f"❌ Could not read base folder: {e}"]

    # Write to log
    with open(LOG_FILE, 'w', encoding='utf-8') as log:
        log.write(header + "\n".join(reports) + "\n")

    # Send email
    yag = yagmail.SMTP(SENDER, APP_PASSWORD)
    yag.send(to=RECIPIENTS, subject=f"AD Health Report – {today}", contents=header + "\n".join(reports))
    print("✅ Report emailed.")

if __name__ == "__main__":
    main()
