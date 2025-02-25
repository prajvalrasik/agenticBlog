import os  # For interacting with environment variables
from crewai import Agent  # Importing the Agent class for creating specialized agents
from langchain_groq import ChatGroq  # Importing the ChatGroq model integration
from tools import google_search_tool  # Importing a tool for performing Google searches

# if you use a .env file to store your API keys and other secrets
from dotenv import load_dotenv
load_dotenv()

# Initialize the ChatGroq language model with specific parameters
model = "groq/llama3-8b-8192"
llm = ChatGroq(
    model=model,          # Use the selected model
    verbose=True,         # Enable detailed logging for debugging
    temperature=0,        # Set temperature to 0 for deterministic outputs
    groq_api_key=os.getenv('GROQ_API_KEY'),  # Fetch the API key securely
    max_tokens=512,       # **New**: reduce tokens to help avoid hitting the free-plan limit
    max_retries=5         # **New**: try re-calling if rate-limited
)

# Define the first agent: Researcher
researcher = Agent(
    role="Technology Intelligence Specialist",
    goal="""
    1. Track breakthroughs in {topic}.
    2. Identify patterns to predict trends.
    3. Validate findings and assess impact.
    """,
    backstory="""
    A tech expert skilled in identifying emerging trends using a blend of academic research, patents, and industry signals. 
    Known for spotting breakthroughs early and combining AI analytics with intuition to forecast future innovations.
    """,
    memory=False,       # Leave this on if you need memory
    verbose=True,
    llm=llm,
    tools=[google_search_tool],
    allow_delegation=True
)

# Define the second agent: Writer
writer = Agent(
    goal="""
    1. Simplify complex tech into engaging narratives.
    2. Highlight human impact and future potential.
    3. Create stories that resonate with diverse audiences.
    """,
    backstory="""
    A former physicist turned storyteller, skilled in explaining complex ideas. 
    Your work bridges gaps between experts and the public, inspiring understanding and action.
    """,
    memory=False,
    verbose=True,
    llm=llm,
    tools=[google_search_tool],
    allow_delegation=True
)

# Define the third agent: Proofreader
proof_reader = Agent(
    role="Proofreader",
    goal="""
    Ensure reports are polished, accurate, and easy to understand.
    """,
    backstory="""
    An expert in clarity and precision, ensuring every report is error-free, well-structured, and properly cited.
    """,
    memory=False,
    verbose=True,
    llm=llm,
    tools=[google_search_tool],
    allow_delegation=True
)


