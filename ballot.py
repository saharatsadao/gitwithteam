def save_vote(student_id, choice):
    # Role 4: เขียนระบบบันทึกคะแนนลงไฟล์หรือ List
    try:
        with open("votes.txt", "a") as f:
            f.write(f"{student_id}:{choice}\n")
        return True
    except:
        return False