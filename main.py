import ai_policy
import candidates
import voter_check
import ballot
import counter


def main():
    print("--- ระบบเลือกตั้งประธานสาขา ComSci ---")
    print("1. ลงคะแนน")
    print("2. ดูนโยบาย")
    menu_choice = input("เลือกตัวเลือก (1 หรือ 2): ")

    if menu_choice == "2":
        candidate_id = input("กรุณาใส่เบอร์ผู้สมัครเพื่อดูนโยบาย: ")
        print("นโยบายของผู้สมัคร:", candidate_id)
        policy = ai_policy.summarize_policy(candidate_id)
        print(policy)
        return
    elif menu_choice != "1":
        print("ตัวเลือกไม่ถูกต้อง")
        return

    student_id = input("กรุณากรอกรหัสนักศึกษา: ")

    if voter_check.is_eligible(student_id):
        candidates.show_list()
        choice = input("เลือกเบอร์ที่ต้องการลงคะแนน: ")

        if ballot.save_vote(student_id, choice):
            print("ลงคะแนนสำเร็จ!")
        else:
            print("เกิดข้อผิดพลาดในการลงคะแนน")
    else:
        print("คุณไม่มีสิทธิ์ลงคะแนน หรือลงคะแนนไปแล้ว")

    # ส่วนนี้ไว้รันตอนท้ายหลัง Merge ครบ
    # counter.show_result()


if __name__ == "__main__":
    main()