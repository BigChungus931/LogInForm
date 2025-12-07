import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector
from mysql.connector import Error

def probes_quiz(clear_main_content, create_card2, main_window, colors):
    font_family = "Bahnschrift"

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="computer mind"
        )

    except Error as e:
        messagebox.showerror("Database error", "Failed to connect to phpMyAdmin")
        return

    try:
        cursor = connection.cursor(dictionary = True)
        cursor.execute("SELECT * FROM quiz_categories WHERE id = %s", (1,))
        category_info = cursor.fetchone()
        cursor.close()
    except Error as e:
        messagebox.showerror("Database error", "Error fetching category")
        connection.close()
        return

    clear_main_content()

    if category_info:
        create_card2(
            category_info["category_name"],
            category_info["description"],
            category_info["icon"]
        )
    else:
        create_card2("Probes", "This quiz is about probes", "🚀 ")

    # Quiz data
    questions = [
        {
            "question": "which space probe orbited Jupiter starting in 2016?",
            "options": ["Voyager 2", "Galileo", "Cassini", "Juno"],
            "correct": 3
        },
        {
            "question": "which space probe landed on a comet in 2014?",
            "options": ["Pioneer", "Rosetta", "Juno", "New Horizons"],
            "correct": 1
        },
        {
            "question": "which space probe was the first to land on Mars successfully?",
            "options": ["Viking 1", "Sojourner", "Spirit", "Curiosity"],
            "correct": 0
        },
        {
            "question": "which Soviet probe was the first to reach Venus?",
            "options": ["Luna 2", "Venera 16", "Venera 7", "Mars 3"],
            "correct": 2
        },
        {
            "question": "which spacecraft took the famous 'Pale Blue Dot' photo?",
            "options": ["Voyager 2", "Voyager 1", "New Horizons", "Hubble"],
            "correct": 1
        },
        {
            "question": "which probe studied the asteroid Vesta and dwarf planet Ceres?",
            "options": ["Juno", "Rosetta", "Dawn", "Voyager 2"],
            "correct": 2
        },
        {
            "question": "which Japanese probe collected samples from asteroid Ryugu?",
            "options": ["Hayabusa2", "OSIRIS-REx", "Pioneer", "Luna 3"],
            "correct": 0
        },
        {
            "question": "which space probe studied Jupiter before Juno?",
            "options": ["New Horizons", "Cassini", "Mariner 10", "Galileo"],
            "correct": 3
        }
    ]
    random.shuffle(questions)

    # Quiz variables
    current_q = 0
    score = 0
    selected_answer = tk.IntVar()

    quiz_frame = tk.Frame(main_window.main_content)
    quiz_frame.config(bg=colors["bg"])
    quiz_frame.pack(fill="both", expand=True, padx=20, pady=10)

    title_label = tk.Label(quiz_frame, text="Multiple choice questions", font=(font_family, 32), fg=colors["text"], bg=colors["bg"])
    title_label.pack(pady=20)

    counter_label = tk.Label(quiz_frame, text="Question 1 of 8", font=(font_family, 23), bg=colors["bg"], fg="lightblue")
    counter_label.pack(pady=5)

    question_label = tk.Label(quiz_frame, text="", font=(font_family, 25, "bold"), bg=colors["bg"], fg=colors["text"],
                              wraplength=550, justify="center")
    question_label.pack(pady=20)

    option_frame = tk.Frame(quiz_frame, bg=colors["bg"])
    option_frame.pack(pady=20, fill="both", expand=True, padx=20)
    option_buttons = []
    for i in range(4):
        btn = tk.Radiobutton(option_frame, text="", variable=selected_answer, value=i, font=(font_family, 17),
                             bg=colors["bg"], fg=colors["text"], selectcolor="blue", wraplength=800, justify="left")
        btn.pack(anchor="w", pady=8, padx=20)
        option_buttons.append(btn)

    score_label = tk.Label(quiz_frame, text=f"Score: 0/{len(questions)}", font=(font_family, 20, "bold"), bg=colors["bg"],
                           fg=colors["score"])
    score_label.place(x=10, y=10)

    def load_question():
        nonlocal current_q
        if current_q < len(questions):
            q_data = questions[current_q]
            counter_label.config(text=f"Question {current_q + 1} of {len(questions)}")
            question_label.config(text=q_data["question"])
            for i, option in enumerate(q_data["options"]):
                option_buttons[i].config(text=f"{chr(65 + i)}. {option}")

            selected_answer.set(-1)
            if current_q == len(questions) - 1:
                next_btn.config(text="Finish quiz")
            else:
                next_btn.config(text="Next question")

    def next_question():
        nonlocal current_q, score
        if selected_answer.get() == -1:
            messagebox.showwarning("No selection", "Just select an answer already")
            return

        if selected_answer.get() == questions[current_q]["correct"]:
            score += 1
            score_label.config(text=f"Score: {score}/{len(questions)}")

        current_q += 1

        if current_q < len(questions):
            load_question()
        else:
            show_result()

    def show_result():
        # Clear the quiz interface
        for widget in quiz_frame.winfo_children():
            widget.destroy()

        percentage = (score / len(questions)) * 100
        if percentage >= 80:
            grade = "Excellent"
            color = "#4CAF50"
        elif percentage >= 60:
            grade = "Good job"
            color = "#FF9800"
        else:
            grade = "Why didn't you pass the test? Did you pay attention in school?"
            color = "#f44336"

        result_label = tk.Label(quiz_frame, text="Quiz complete", font=(font_family, 32), fg=colors["text"], bg=colors["bg"])
        result_label.pack(pady=30)

        score_results = tk.Label(quiz_frame, text=f"Your score: {score}/{len(questions)} ({percentage:.1f}%)",
                                 font=(font_family, 24), fg=colors["score"], bg=colors["bg"])
        score_results.pack(pady=20)

        grade_label = tk.Label(quiz_frame, text=grade, font=(font_family, 20, "bold"), fg=color, bg=colors["bg"])
        grade_label.pack(pady=20)

        # Result buttons
        result_buttons_frame = tk.Frame(quiz_frame, bg=colors["bg"])
        result_buttons_frame.pack(pady=30)

        restart_btn = tk.Button(result_buttons_frame, text="Restart quiz", command=restart_quiz,
                                font=(font_family, 12, "bold"), bg="#4CAF50", fg=colors["text"], padx=20)
        restart_btn.pack(side="left", padx=10)

        quit_btn = tk.Button(result_buttons_frame, text="Quit", command=quit_quiz, font=(font_family, 12, "bold"),
                             bg="#F44336", fg=colors["text"], padx=20)
        quit_btn.pack(side="left", padx=10)

    def restart_quiz():
        nonlocal current_q, score
        current_q = 0
        score = 0
        random.shuffle(questions)

        # Clear all widgets
        for widget in quiz_frame.winfo_children():
            widget.destroy()

        # Recreate the quiz interface
        nonlocal title_label, counter_label, question_label, option_frame
        nonlocal option_buttons, score_label, next_btn, quit_btn

        title_label = tk.Label(quiz_frame, text="Multiple choice questions", font=(font_family, 32), fg=colors["text"],
                               bg=colors["bg"])
        title_label.pack(pady=20)

        counter_label = tk.Label(quiz_frame, text="Question 1 of 8", font=(font_family, 23), bg=colors["bg"], fg="lightblue")
        counter_label.pack(pady=5)

        question_label = tk.Label(quiz_frame, text="", font=(font_family, 25, "bold"), bg=colors["bg"], fg=colors["text"],
                                  wraplength=550, justify="center")
        question_label.pack(pady=20)

        option_frame = tk.Frame(quiz_frame, bg=colors["bg"])
        option_frame.pack(pady=20, fill="both", expand=True, padx=20)
        option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(option_frame, text="", variable=selected_answer, value=i, font=(font_family, 23),
                                 bg=colors["bg"], fg=colors["text"], selectcolor="blue", wraplength=800, justify="left")
            btn.pack(anchor="w", pady=8, padx=20)
            option_buttons.append(btn)

        score_label = tk.Label(quiz_frame, text=f"Score: 0/{len(questions)}", font=(font_family, 20, "bold"),
                            bg=colors["bg"], fg=colors["score"])
        score_label.place(x=10, y=10)

        next_btn = tk.Button(quiz_frame, text="Next question", command=next_question, font=("Arial", 12, "bold"),
                             background="#4CAF50", fg=colors["text"], relief="flat")
        next_btn.place(x=840, y=10)

        quit_btn = tk.Button(quiz_frame, text="Quit", command=quit_quiz, font=("Arial", 12, "bold"), background="red",
                             fg=colors["text"], relief="flat")
        quit_btn.place(x=970, y=10)

        load_question()

    def quit_quiz():
        if messagebox.askyesno("Quit", "Are you sure you want to quit the quiz? You could go for a second run"):
            quiz_frame.destroy()

    # Create the navigation buttons
    next_btn = tk.Button(quiz_frame, text="Next question", command=next_question, font=("Arial", 12, "bold"),
                         background="#4CAF50", fg=colors["text"], relief="flat")
    next_btn.place(x=840, y=10)

    quit_btn = tk.Button(quiz_frame, text="Quit", command=quit_quiz, font=("Arial", 12, "bold"), background="red",
                         fg=colors["text"], relief="flat")
    quit_btn.place(x=970, y=10)

    # Load the first question
    load_question()