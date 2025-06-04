from datetime import date
from sheets_oauth import setup_sheet_headers, save_complaints_to_sheet

setup_sheet_headers()

class civil_complaint:
    def __init__(self, user, content, latitude, longitude, complaint_type, created_date=None):
        self.user = user
        self.content = content
        self.latitude = latitude
        self.longitude = longitude
        self.complaint_type = complaint_type
        if created_date:
            self.created_date = created_date
        else:
            self.created_date = date.today()

    # def __str__(self):
    #     return f"[{self.created_date}] {self.user}님이 신고: ({self.complaint_type}):{self.content} ({self.latitude}, {self.longitude})"
    def __str__(self):
        return self.to_string(lang='Korean')  # 기본은 한국어

    def to_string(self, lang='Korean'):
        if lang == 'Korean':
            return (
                f"[{self.created_date}] ({self.complaint_type})\n"
                f"{self.user}님이 신고:{self.content} \n " 
                f" 위치: ({self.latitude:.6f}, {self.longitude:.6f})"
            )
        else:
            return (
                f"[{self.created_date}] {self.user} reported: "
                f"({self.complaint_type}): {self.content} "
                f"(Latitude {self.latitude:.6f}, Longitude {self.longitude:.6f})"
            )

def submit_complaint(user, content, latitude, longitude, complaint_type, created_date=None):
    complaint = civil_complaint(user, content, latitude, longitude, complaint_type, created_date)
    save_complaints_to_sheet(complaint)
