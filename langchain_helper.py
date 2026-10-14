
import os 
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI  #changed
from langchain_experimental.sql import SQLDatabaseChain
from langchain_classic.prompts import SemanticSimilarityExampleSelector
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_classic.chains.sql_database.prompt import PROMPT_SUFFIX
from few_shots import few_shots
import re #added
from langchain_core.output_parsers import StrOutputParser #added

load_dotenv()


def get_few_shot_db_chain():
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3
    )

    llm = ChatGoogleGenerativeAI(  #changed
        model="gemini-3.5-flash-lite",  #changed: replace with your intended Gemini model ID
        google_api_key=os.environ["GOOGLE_API_KEY"],
        temperature=0.1
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    to_vectorize = [
        " ".join(str(value) for value in example.values())  #changed
        for example in few_shots
    ]

    vectorstore = Chroma.from_texts(
        to_vectorize, embeddings, metadatas=few_shots
    )

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
        input_keys=["input"]  #changed
    )

    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    Do not include markdown code fences such as ```sql or ``` in the SQLQuery output.
    
    IMPORTANT SQL RULES:
    - Aggregate data at the requested group level before ranking or filtering.
    - Use RANK() or ROW_NUMBER() with PARTITION BY for highest/lowest values per group; filter by the required rank.
    - Never replace per-group ranking with a global LIMIT.
    - Add LIMIT only when the user explicitly requests a specific number of results or top/bottom N.
    - For GROUP BY and HAVING queries, return all matching groups unless a limit is requested.
    - Preserve requested sorting direction (ASC/DESC) and return executable SQL only, without Markdown code fences.
    
    Output formatting rules:
    1. First, display the SQL query result as a Markdown table using the exact column names and values returned by SQL.
    2. Immediately below the table, write `**Explanation:**` followed by a concise natural-language summary of the results.
    3. For grouped or ranked results, explain the results group-wise, mentioning the relevant brand, size, color, stock, inventory value, percentage contribution, and rank.
    4. Preserve all rows, values, column names, and ordering returned by SQL. Do not invent, omit, or recalculate results.
    5. If SQL returns no rows, state that no matching records were found.
    6. Do not display the generated SQL query in the final answer unless explicitly requested.

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"]
    )

    chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=True,
        prompt=few_shot_prompt
    )

    return chain



# =================================== ================

# # from langchain.llms import GooglePalm
# # from langchain.utilities import SQLDatabase
# # from langchain_experimental.sql import SQLDatabaseChain
# # from langchain.prompts import SemanticSimilarityExampleSelector
# # from langchain.embeddings import HuggingFaceEmbeddings
# # from langchain.vectorstores import Chroma
# # from langchain.prompts import FewShotPromptTemplate
# # from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
# # from langchain.prompts.prompt import PromptTemplate

# # from few_shots import few_shots

# # import os
# # from dotenv import load_dotenv
# # load_dotenv()  # take environment variables from .env (especially openai api key)


# import os
# import streamlit as st
# from dotenv import load_dotenv
# from langchain_community.utilities import SQLDatabase
# from langchain_community.llms import GooglePalm
# from langchain_experimental.sql import SQLDatabaseChain
# from langchain_classic.prompts import SemanticSimilarityExampleSelector
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
# from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
# from langchain_classic.chains.sql_database.prompt import PROMPT_SUFFIX
# from few_shots import few_shots

# load_dotenv()



# def get_few_shot_db_chain():
#     db_user = "root"
#     db_password = "root"
#     db_host = "localhost"
#     db_name = "atliq_tshirts"

#     db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
#                               sample_rows_in_table_info=3)
#     llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)

#     embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
#     to_vectorize = [" ".join(example.values()) for example in few_shots]
#     vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)
#     example_selector = SemanticSimilarityExampleSelector(
#         vectorstore=vectorstore,
#         k=2,
#     )
#     mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
#     Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
#     Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
#     Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
#     Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    
#     Use the following format:
    
#     Question: Question here
#     SQLQuery: Query to run with no pre-amble
#     SQLResult: Result of the SQLQuery
#     Answer: Final answer here
    
#     No pre-amble.
#     """

#     example_prompt = PromptTemplate(
#         input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
#         template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
#     )

#     few_shot_prompt = FewShotPromptTemplate(
#         example_selector=example_selector,
#         example_prompt=example_prompt,
#         prefix=mysql_prompt,
#         suffix=PROMPT_SUFFIX,
#         input_variables=["input", "table_info", "top_k"], #These variables are used in the prefix and suffix
#     )
#     chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
#     return chain

 