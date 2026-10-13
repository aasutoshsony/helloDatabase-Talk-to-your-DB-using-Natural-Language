# HelloDatabase — Talk to Your DB Using Python

An LLM-powered question-answering system that lets users interact with a MySQL database using natural language instead of writing SQL queries manually.

## Features

- **Natural Language to SQL:** Convert questions into SQL queries using Gemini.
- **MySQL Integration:** Retrieve inventory and discount information from a relational database.
- **Few-Shot Prompting:** Improve SQL generation using example question-query pairs.
- **LangChain Integration:** Use `SQLDatabaseChain` to generate and execute SQL queries.
- **Retail Analytics:** Answer questions about T-shirt inventory, stock quantities, and discounts.

## Tech Stack

- Python 3.11
- LangChain
- Google Gemini API
- MySQL
- SQLAlchemy and PyMySQL

## How It Works

1. The user asks a question in natural language.
2. Gemini generates an SQL query using the database schema and prompt examples.
3. LangChain executes the generated query against MySQL.
4. The application returns the result to the user.

## Example Questions

- How many Nike T-shirts are available in extra-small size and white color?
- What is the total value of the inventory for small-size T-shirts?
- How much revenue would selling all Levi's T-shirts generate after discounts?

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/aasutoshsony/helloDatabase-Talk-to-your-DB-using-Python.git
cd helloDatabase-Talk-to-your-DB-using-Python
```

### 2. Create and activate the environment

```bash
python -m venv lang-env
```

Windows PowerShell:

```powershell
.\lang-env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add your Gemini API key:

```dotenv
GOOGLE_API_KEY=your_gemini_api_key
```

Configure your MySQL connection details in the application.

### 5. Run the application

Run the Python script or notebook included in the repository.

## Future Improvements

- Add a Streamlit chat interface.
- Improve SQL accuracy with additional few-shot examples.
- Add query validation and read-only database access.

## License

Add a license file if you intend to distribute this project as open source.
