def summarize_policy(candidate_id):
    # Role 6: ใช้ AI จำลองการวิเคราะห์นโยบาย
    policies = {"1": "เน้นการศึกษาและการทำงานร่วมกัน", "2": "เน้นโครงสร้างพื้นฐานและเทคโนโลยี"}
    return policies.get(candidate_id, "ไม่มีข้อมูล")