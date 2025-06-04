from datetime import date
from sheets_oauth import setup_sheet_headers, save_complaints_to_sheet

setup_sheet_headers()

class civil_complaint:
    def __init__(self, user, content, latitude, longitude, complaint_type, created_date=None, lang='Korean'):
        self.user = user
        self.content = content
        self.latitude = latitude
        self.longitude = longitude
        self.complaint_type = complaint_type
        self.lang = lang 
        if created_date:
            self.created_date = created_date
        else:
            self.created_date = date.today()

    def __str__(self):
        return self.to_string(lang=self.lang)

    def to_string(self, lang='Korean'):
        if lang == 'Korean':
            return (
                f"[{self.created_date}]\n"
                f"작성자: {self.user}\n"
                f"민원 유형: {self.complaint_type}\n"
                f"민원 내용: {self.content}\n"
                f"위치: 위도({self.latitude:.6f}), 경도({self.longitude:.6f})"
            )
        else:
            return (
                f"[{self.created_date}]\n"
                f"User: {self.user}\n"
                f"Complaint type: {self.complaint_type}\n"
                f"Complaint content: {self.content}\n"
                f"Location: Lat({self.latitude:.6f}), Lon({self.longitude:.6f})"
            )

def submit_complaint(user, content, latitude, longitude, complaint_type, created_date=None):
    complaint = civil_complaint(user, content, latitude, longitude, complaint_type, created_date)
    save_complaints_to_sheet(complaint)
