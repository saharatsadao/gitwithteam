# รายชื่อผู้มีสิทธิ์ (ตัวอย่าง)
voters_list = ["6801", "6802", "6803"]
voted_already = []


def is_eligible(student_id):
    # AI Prompt: "เขียนฟังก์ชันเช็คว่า student_id อยู่ใน voters_list และยังไม่อยู่ใน voted_already"
    if student_id in voters_list and student_id not in voted_already:
        return True
    return False