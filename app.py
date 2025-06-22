from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1lWcY4kMNvP6R4i3R7sk-11GufkW6TXVOB3fP3I-mMno").sheet1

@app.route("/")
def index():
    messages = sheet.col_values(1)
    message = messages[1] if len(messages) > 1 else "لا توجد رسائل حالياً."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)