import os
import pytz #시간대(timezone) 처리를 위한 라이브러리
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from collections import Counter
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1DkyKTgoc3vQuzp189kFeAxbaGgRPb9Z0EpSQp32YNfY'  
SHEET_RANGE = 'Sheet1!A:G'

def main(): #basic usage of the Sheets API
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    service = build('sheets', 'v4', credentials=creds)
    return service

def setup_sheet_headers():
    service = main()
    headers = [["작성자", "내용", "위도", "경도", "작성일", "제출 시간", "민원 종류"]]
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range="Sheet1!A1:G1",
        valueInputOption="RAW",
        body={"values": headers}
    ).execute()

def save_complaints_to_sheet(civil_complaint):
    service = main()
    seoul_tz = pytz.timezone('Asia/Seoul')
    submit_time = datetime.now(seoul_tz).strftime('%Y-%m-%d %H:%M:%S') # 현재 시간을 한국 표준시로 가져오기
    values = [[
        civil_complaint.user, 
        civil_complaint.content, 
        civil_complaint.latitude, 
        civil_complaint.longitude, 
        str(civil_complaint.created_date),
        submit_time,
        civil_complaint.complaint_type
        ]]
    body = {'values': values}
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_RANGE,
        valueInputOption="RAW",
        body=body
    ).execute()

def load_all_complaints():
    service = main()
    result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=SHEET_RANGE
    ).execute()
    return result.get("values", [])[1:]

def filter_by_author(author_name):
    all_data = load_all_complaints()
    return [row for row in all_data if row[0] == author_name]

def count_by_date():
    all_data = load_all_complaints()
    dates = [row[4] for row in all_data]
    return dict(Counter(dates))