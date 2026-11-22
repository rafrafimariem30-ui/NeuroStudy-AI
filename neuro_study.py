import datetime


def run_neuro_study_v2():
    print("=========================================================")
    print("   🧠 NeuroStudy AI v2.0: Priority & Academic Tracker    ")
    print("=========================================================")

    print("\nSelect Mode:")
    print("1. 🎯 Daily Study Priority Planner")
    print("2. 📊 Grades & Weekly Progress Analyzer")

    mode = input("\nEnter mode (1 or 2): ")

    # Mode 1: Daily Study Priority Planner
    if mode == "1":
        total_minutes = int(
            input("\nHow many total minutes do you have to study today? (e.g., 120): ")
        )
        num_subjects = int(input("How many subjects do you want to plan? (e.g., 3): "))

        subjects = []
        total_weight = 0

        for i in range(num_subjects):
            print(f"\n--- Subject #{i + 1} ---")
            name = input("Subject name (e.g., Physics, Math, Python): ")
            difficulty = int(input("Difficulty level (1 = Easy, 5 = Very Hard): "))
            days_left = int(input("Days left until exam (1 = Tomorrow, 10 = Later): "))

            urgency = 10 / max(days_left, 1)
            priority_score = (difficulty * 1.5) + urgency
            subjects.append({"name": name, "score": priority_score})
            total_weight += priority_score

        subjects.sort(key=lambda x: x["score"], reverse=True)

        print("\n--- 🚀 YOUR OPTIMAL EXECUTION PLAN ---")
        for rank, sub in enumerate(subjects, start=1):
            allocated_mins = round((sub["score"] / total_weight) * total_minutes)
            print(
                f"#{rank} Priority: {sub['name']} -> {allocated_mins} mins (AI Score: {sub['score']:.1f})"
            )

    # Mode 2: Grades & Weekly Progress Analyzer
    elif mode == "2":
        num_grades = int(input("\nHow many subjects/exams do you want to evaluate? "))
        grades = []
        weakest_subject = ""
        lowest_grade = 11.0

        for i in range(num_grades):
            sub_name = input(f"\nSubject #{i + 1} name: ")
            grade = float(input(f"Enter your grade for {sub_name} (0 to 10): "))
            grades.append((sub_name, grade))

            if grade < lowest_grade:
                lowest_grade = grade
                weakest_subject = sub_name

        average_grade = sum(g for _, g in grades) / num_grades

        if average_grade >= 9.0:
            status = "Elite Performance! 🌟"
        elif average_grade >= 7.0:
            status = "Strong Performance, push for 9+! 💪"
        else:
            status = "Needs Deep Work & Extra Focus ⚡"

        print("\n=========================================================")
        print("   📈 WEEKLY ACADEMIC PERFORMANCE REPORT")
        print("=========================================================")
        print(f"Overall Average: {average_grade:.2f} / 10")
        print(f"Academic Status: {status}")
        print(
            f"🎯 Focus Target Next Week: {weakest_subject} (Grade: {lowest_grade}/10)"
        )

        # Append progress to a permanent log file
        with open("weekly_progress_log.txt", "a", encoding="utf-8") as log_file:
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            log_file.write(
                f"[{date_str}] Average: {average_grade:.2f}/10 | Focus Area: {weakest_subject} ({lowest_grade})\n"
            )

        print(
            "\n✅ Progress saved to 'weekly_progress_log.txt' to track your weekly growth!"
        )

    else:
        print("Invalid choice! Please restart and select 1 or 2.")


run_neuro_study_v2()
