from crewai import Crew, Process
from agents import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task

# Define the topic
topic = "The Sudden Boom of Agentic AI"

# Initialize the Crew with agents and tasks
crew = Crew(
    agents=[researcher, writer, proof_reader],
    tasks=[research_task, write_task, proof_read_task],
    process=Process.sequential,  # Ensures tasks run in sequence
    verbose=True  # Enables detailed logging
)

# Execute the crew with the provided input
result = crew.kickoff(inputs={"topic": topic})

# Print the final result
print(result)