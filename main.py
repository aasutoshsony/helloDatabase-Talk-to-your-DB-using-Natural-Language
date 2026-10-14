
import streamlit as st
from langchain_helper import get_few_shot_db_chain

#added history JSON code
import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path(__file__).parent / "query_history.json"

def load_history():
    if not HISTORY_FILE.exists():
        return []

    content = HISTORY_FILE.read_text(encoding="utf-8").strip()
    if not content:
        return []

    return json.loads(content)

def save_history(question, answer):
    history = load_history()
    history.insert(0, {
        "question": question,
        "answer": answer,
        "timestamp": datetime.now().strftime("%d-%m-%Y %I:%M %p")
    })

    HISTORY_FILE.write_text(
        json.dumps(history, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


st.title("HelloDatabase 👕")
st.subheader(" Talk to Your DB Using Natural Language Q&A 🔠")

st.markdown("""
<style>
.stTextArea textarea {
    overflow-y: auto !important;
    resize: both !important;
    overflow-wrap: break-word;
}

div[data-testid="stFormSubmitButton"] button {
    background-color: #238b47 !important;
    color: white !important;
    border: 1px solid #16a34a !important;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background-color: transparent !important;
    color: red !important;
    border: 1px solid red !important;
}
</style>
""", unsafe_allow_html=True)

with st.form("question_form"):
    question = st.text_area(
        "Question:",
        height=60,
        placeholder="Ask a question about your inventory..."
    )
    submit = st.form_submit_button("Submit")

if submit and question.strip():
    try:
        with st.spinner("Generating answer..."):
            chain = get_few_shot_db_chain()
            response = chain.invoke({"query": question})

        answer = response["result"]
        st.header("Answer")
        st.write(answer)

        save_history(question, answer) #added history JSON code


    except Exception as e:
        st.error(f"Error: {e}")

elif submit:
    st.warning("Please enter a question.")

#added history JSON code
st.divider()
st.header("Query History")

history = load_history()

if history:
    for item in history:
        with st.expander(item["question"]):
            st.caption(item["timestamp"])
            st.write(item["answer"])
else:
    st.info("No History Found!")



# 4 working wihtout HISTORY

# import streamlit as st
# from langchain_helper import get_few_shot_db_chain

# st.title("HelloDatabase 🔠")
# st.subheader("Talk to Your DB Using Natural Language Q&A 👕")

# st.markdown("""
# <style>
# .stTextArea textarea {
#     overflow-y: auto !important;
#     resize: both !important;
#     overflow-wrap: break-word;
# }

# div[data-testid="stFormSubmitButton"] button {
#     background-color: #238b47 !important;
#     color: white !important;
#     border: 1px solid #16a34a !important;
# }

# div[data-testid="stFormSubmitButton"] button:hover {
#     background-color: transparent !important;
#     color: red !important;
#     border: 1px solid red !important;
# }
# </style>
# """, unsafe_allow_html=True)

# if "history" not in st.session_state:
#     st.session_state.history = []

# with st.form("question_form"):
#     question = st.text_area(
#         "Question:",
#         height=60,
#         placeholder="Ask a question about your inventory..."
#     )
#     submit = st.form_submit_button("Submit")

# if submit and question.strip():
#     try:
#         with st.spinner("Generating answer..."):
#             chain = get_few_shot_db_chain()
#             response = chain.invoke({"query": question})
#             answer = response["result"]

#         st.session_state.history.append({
#             "question": question,
#             "answer": answer
#         })

#     except Exception as e:
#         st.error(f"Error: {e}")

# elif submit:
#     st.warning("Please enter a question.")

# if st.session_state.history:
#     st.header("Answer")
#     st.write(st.session_state.history[-1]["answer"])

#     st.divider()
#     st.header("Query History")

#     for i, item in enumerate(reversed(st.session_state.history), 1):
#         with st.expander(f"{i}. {item['question']}"):
#             st.write("**Question:**", item["question"])
#             st.write("**Answer:**", item["answer"])


# 3 Working !!

# import streamlit as st
# from langchain_helper import get_few_shot_db_chain

# st.title("HelloDatabase 🔠")
# st.subheader(" Talk to Your DB Using Natural Language Q&A 👕 ")

# st.markdown("""
# <style>
# .stTextArea textarea {
#     overflow-y: auto !important;
#     resize: both !important;
#     overflow-wrap: break-word;
# }

# div[data-testid="stFormSubmitButton"] button {
#     background-color: #238b47 !important;
#     color: white !important;
#     border: 1px solid #16a34a !important;
# }

# div[data-testid="stFormSubmitButton"] button:hover {
#     background-color: transparent !important;
#     color: red !important;
#     border: 1px solid red !important;
# }

# </style>
# """, unsafe_allow_html=True)

# with st.form("question_form"):
#     question = st.text_area(
#         "Question:",
#         height=60,
#         placeholder="Ask a question about your inventory..."
#     )
#     submit = st.form_submit_button("Submit")

# if submit and question.strip():
#     try:
#         with st.spinner("Generating answer..."):
#             chain = get_few_shot_db_chain()
#             response = chain.invoke({"query": question})

#         st.header("Answer")
#         st.write(response["result"])
#     except Exception as e:
#         st.error(f"Error: {e}")
# elif submit:
#     st.warning("Please enter a question.")




# #2 working
# import streamlit as st
# from langchain_helper import get_few_shot_db_chain

# st.title("HelloDatabase: Talk to Your DB Using Natural language 👕")

# with st.form("question_form"):
#     question = st.text_input("Question:")
#     submit = st.form_submit_button("Submit")

# if submit and question.strip():
#     with st.spinner("Generating answer..."):
#         chain = get_few_shot_db_chain()
#         response = chain.invoke({"query": question})

#     st.header("Answer")
#     st.write(response["result"])


# ================ =========================

# import streamlit as st
# from langchain_helper import get_few_shot_db_chain

# st.title("HelloDatabase: Talk to Your DB Using Python Q&A 👕")

# question = st.text_input("Question: ")

# if question:
#     chain = get_few_shot_db_chain()
#     response = chain.run(question)

#     st.header("Answer")
#     st.write(response)