import streamlit as st

def quiz_app():
    st.header("Quizzerama🎲")

    subject = st.selectbox("Select Subject:", ["Physics", "Chemistry", "Mathematics", "Biology"])

    if subject == "Physics":
        physics_quiz()
    elif subject == "Chemistry":
        chemistry_quiz()
    elif subject == "Mathematics":
        math_quiz()
    elif subject == "Biology":
        biology_quiz()

def physics_quiz():
    st.header("Physics Quiz")
    st.subheader("(Electric Charges and Fields MCQs)")

    # Define the quiz questions and answers
    questions = [
        {
             "question": "If the sizes of charged bodies are very small compared to the distances between them, we treat them as ____________.",
            "options": ["Zero charges", "Point charges", "Single charge", "No charges"],
            "correct_option": "Point charges",
        },
        {
            "question": "The force per unit charge is known as ____________.",
            "options": ["Electric current", "Electric potential", "Electric field", "Electric space"],
            "correct_option": "Electric field",
        },
        {
            "question": "What is the dielectric constant of a metal?",
            "options": ["-1", "0", "1", "Infinite"],
            "correct_option": "Infinite",
        },
        {
            "question": "The property which differentiates two kinds of charges is called",
            "options": ["Equality of charge", "Polarity of charge", "Fraction of charge", "None of the option"],
            "correct_option": "Polarity of charge",
        },
        {
            "question": "————— gives the information on field strength, direction, and nature of the charge.",
            "options": ["Electric current", "Electric flux", "Electric field", "Electric potential"],
            "correct_option": "Electric field",
        },
    ]

    quiz(questions)

def chemistry_quiz():
    st.header("Chemistry Quiz")
    st.subheader("(Aldehydes, Ketones, and Carboxylic Acids MCQs)")

    # Define the quiz questions and answers
    questions = [
        {
            "question": "Which of the following cannot reduce Fehling’s solution?",
            "options": ["Formic acid", "Acetic acid", "Formaldehyde", "Acetaldehyde"],
            "correct_option": "Acetic acid",
        },
        {
            "question": "Which of the following acids does not form anhydride?",
            "options": ["Formic add", "Acetic acid", "Propionic add", "n-butyric acid"],
            "correct_option": "Acetic acid",
        },
        {
            "question": "The acid which does not contain-COOH group is",
            "options": ["Ethanoic acid", "Lactic acid", "Picric add", "Palmitic acid"],
            "correct_option": "Picric add",
        },
        {
            "question": "Methyl ketones are usually characterised through",
            "options": ["Tollen’s reagent", "Iodoform test", "Schiff’stest", "Benedict solution test."],
            "correct_option": "Iodoform test",
        },
        {
            "question": "HVZ reaction is used to prepare",
            "options": ["ß-haloacid", "α-haloacid", "α, ß-unsaturated add", "  None of these"],
            "correct_option": "α-haloacid",
        },
    ]

    quiz(questions)

def math_quiz():
    st.header("Mathematics Quiz")
    st.subheader("(Differential Equations MCQs)")

    # Define the quiz questions and answers
    questions = [
        {
            "question": "What is the order of differential equation y’’ + 5y’ + 6 = 0?",
            "options": ["0", "1", "2", "3"],
            "correct_option": "2",
        },
        {
            "question": "What is the degree of differential equation (y’’’)2 + (y’’)3 + (y’)4 + y5 = 0?",
            "options": ["2", "3", "4", "5"],
            "correct_option": "2",
        },
        {
            "question": "The number of arbitrary constants in the particular solution of a differential equation of third order is:",
            "options": ["3", "2", "1", "0"],
            "correct_option": "0",
        },
        {
            "question": "Solution of differential equation x.dy – y.dx = Q represents:",
            "options": ["A rectangular hyperbola", "Parabola whose vertex is at the origin", "Straight line passing through the origin", "A circle whose centre is at the origin"],
            "correct_option": "Straight line passing through the origin",
        },
        {
            "question": "If y = ax2+b, then dy/dx at x = 2 is equal to:",
            "options": ["2a", "3a", "4a", " None of these"],
            "correct_option": "4a",
        },
    ]

    quiz(questions)

def biology_quiz():
    st.header("(Biology Quiz)")
    st.subheader("Molecular Basis of Inheritance MCQs")

    # Define the quiz questions and answers
    questions = [
        {
            "question": "The nucleic acid synthesis takes place in?",
            "options": ["3’-5’ direction", "5’-3’ direction", "Both ways", "Any direction"],
            "correct_option": "5’-3’ direction",
        },
        {
            "question": " Hershey and Chase’s experiment was based on the principle",
            "options": ["Transformation", "Translation", "Transduction", "Transcription"],
            "correct_option": "Transduction",
        },
        {
            "question": "Histones are:",
            "options": ["Positively charged and basic amino acids", "Positively charged and acidic proteins", "Negatively charged and basic proteins", "Absent in bacteria"],
            "correct_option": "Absent in bacteria",
        },
        {
            "question": " In eukaryotes, RNA II facilitates transcription of:",
            "options": ["rRNA", "mRNA", "hnRNA", "tRNA"],
            "correct_option": "hnRNA",
        },
        {
            "question": "Which non-radioactive isotope was used by Messelson and Stahl in their experiment?",
            "options": ["P32", "S35", "N15", " None"],
            "correct_option": "N15",
        },
    ]

    quiz(questions)

def quiz(questions):
    # Initialize a score variable
    score = 0

    # Display each question and get user input
    for i, q in enumerate(questions, 1):
        st.subheader(f"Question {i}: {q['question']}")

        # Use st.radio to display radio buttons with options
        unique_key = f"radio_{i}"  # Generate a unique key for each radio button
        selected_option = st.radio(f"Select an option for Question {i}:", q["options"], key=unique_key)

        # Use a checkbox to display the correct answer
        show_answer = st.checkbox(f"Show correct answer for Question {i}")
        if show_answer:
            st.write(f"Correct answer: {q['correct_option']}")

        # Check if the selected option is correct
        if selected_option == q["correct_option"]:
            score += 1
            st.success("Correct! 👍")  # Display a success emoji for correct answers
        else:
            st.warning("Incorrect! ❌")  # Display a warning emoji for incorrect answers

    # Display the final score
    st.success(f"Your final score is: {score}/{len(questions)}")

    # Award badges based on the score
    if score == len(questions):
        st.balloons()
        st.success("Congratulations! You've earned the Master Quizzer badge!")
    elif score >= len(questions) // 2:
        st.success("Well done! You've earned the Quiz Enthusiast badge!")

if __name__ == "__main__":
    quiz_app()
