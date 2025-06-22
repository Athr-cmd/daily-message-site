from flask import Flask, render_template
import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# نطاقات الوصول
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# قراءة بيانات الاعتماد من متغير البيئة
creds_json = os.getenv("GOOGLE_CREDENTIALS")
creds_dict = json.loads(creds_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# ربط gspread
client = gspread.authorize(creds)

# فتح الشيت باستخدام ID مباشرة (بدون الحاجة لتحديده داخل الكود)
sheet = client.open_by_key(os.getenv("SHEET_ID")).worksheet(os.getenv("TAB_NAME"))

@app.route("/")
def index():
    messages = sheet.col_values(1)
    message = messages[1] if len(messages) > 1 else "وحده، رسائل، تجريب."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
