# finalproject


# 동네 민원/불편사항 신고 플랫폼

Streamlit과 Google Sheets를 활용한 간단한 민원 신고 웹앱입니다.  
지도에서 위치를 클릭하고 내용을 작성하면 민원이 저장되고, 다른 사람들도 볼 수 있습니다.

---

## 🛠 주요 기능

- 지도 클릭 → 위치 지정
- 이름, 내용, 날짜 입력 후 제출
- 민원이 지도에 마커로 표시됨
- 작성자 이름으로 검색 가능
- 날짜별 민원 수 통계 시각화

---

## 🖥 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
