


 quiz_data =  ['GK', 'Science', 'English']
 questions={
    "GK": [
        {
            "question": "1.The most widely spoken foreign language in India:?",
            "options": ["French", "English", "Portughese", "Arabic"],
            "answer": "English"
        },
        {
            "question": "2. National Institute of Nutrition is located in:",
            "options": ["Hyderabad","karnal","Indoor","Bhopal"],
            "answer": "Hyderabad"
        },
        {
            
            "question": "3.Almora hill station is in the state of:?",
            "options": ["Himachal Pradesh","Assam","Uttrakhand","Mizoram"],
            "answer":"Uttrakhand"
        },
        {
            "question":"4.‘The Pearl Harbour of India’:",
            "options": ["Tutucorin","Chennai","Mumbai","Surat"],
            "answer": "Tutucorin"
        },
        {
          "question":"45.Which religion belongs to the Lotus Temple in New Delhi?:", 
          "options": ["Sikh","Parsi","Bahai","Jain"], 
          "answer": "Bahai"
        }
        
    ],
    "Science": [
        {
            "question": "1.Which gas is most abundant in Earth's atmosphere?",
            "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"],
            "answer": "Nitrogen"
        },
        {
            "question": "2.What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "G", "Go"],
            "answer": "Au"
        },
        {
            "question": "3.Which vitamin is abundant in citrus fruits?",
            "options": ["Vitamin A","Vitamin B","Vitamin C","Vitamin D"],
            "answer": "Vitamin C"
        },
        {
            "question":"4.Which of the following measurements is not a unit of distance?",
            "options": ["Angstrom","Ammeter","Cubit","Parsec"],
            "answer":"Ammeter"
        },
        {
           "question":"5. Zinc Oxide is",
           "options": ["Acidic","Basic","Neutral","Amphoteric"],
           "answer":"Amphoteric"    
               
                
        }
    
    ],
    "English": [
        {
            "question":"1.____ is he up to?",
            "options":["who","how","which","what"],
            "answer": "what"
        },
        {
             "question": "2.Complete the proverb : _____a day keeps the doctor away",
             "options":["An orange","An apple","A banana","A pineapple"],
             "answer":"An apple"
        },
        {
             "question": "3.The use of more words than are required to express an idea:",
             "options":[" Pleonasm","Ventriloquism ","Circumlocution","Verbatim"],
             "answer":" Pleonasm"
        },
        {
             "question":"4.The chief guest _____ the prizes to the winner.",
             "options":["gave up","gave away","gave in","gave out"],
             "answer":"gave away"
        },
        {
             "question": "5.Changing one’s mind too quickly.",
             "options":["Adaptability","Instability","Versatility","Vacillation"],
             "answer" : "Vacillation"    
        }
    ]
}
user_answers = []
quiz_results = []
with st.sidebar:
 selected_subject = st.radio("Select a subject:", quiz_data)

st.subheader(f"{selected_subject} Quiz")

# Get the selected subject's questions and options
subject_questions = quiz_data[selected_subject]

for i, question_data in enumerate(subject_questions):
     #st.caption(f" {i+1}.")
     st.write(question_data["question"])

    # Display options as radio buttons
     selected_option = st.radio("Select your answer:", question_data["options"])
     user_answers.append(selected_option)

# Calculate the score
score = sum([1 for user_ans, ques in zip(user_answers, subject_questions) if user_ans == ques["answer"]])


st.subheader("Quiz Results")
st.write(f"You scored {score}/{len(subject_questions)}")
