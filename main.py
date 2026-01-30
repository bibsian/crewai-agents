import os
import logging
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Suppress litellm logging errors
os.environ["LITELLM_LOG"] = "ERROR"
logging.getLogger("LiteLLM").setLevel(logging.CRITICAL)
logging.getLogger("litellm").setLevel(logging.CRITICAL)


def main():
    """Simple CrewAI example with 2 agents orchestrated to research and write."""
    
    # Initialize Ollama LLM using CrewAI's LLM wrapper
    llm = LLM(
        model="ollama/llama3.2",
        base_url="http://localhost:11434"
    )
    
    # Agent 1: Researcher - Gathers information
    researcher = Agent(
        role='Research Analyst',
        goal='Research and gather comprehensive information on given topics',
        backstory='You are an expert researcher with a knack for finding key insights '
                  'and organizing information clearly.',
        llm=llm,
        verbose=True
    )
    
    # Agent 2: Writer - Creates content from research
    writer = Agent(
        role='Content Writer',
        goal='Create clear and engaging written content based on research',
        backstory='You are a skilled writer who transforms research into compelling, '
                  'easy-to-understand content.',
        llm=llm,
        verbose=True
    )
    
    # Task 1: Research task
    research_task = Task(
        description='Research the benefits of using AI agents in software development. '
                    'Focus on productivity improvements, automation capabilities, '
                    'and real-world use cases.',
        expected_output='A detailed research summary with key findings and insights.',
        agent=researcher
    )
    
    # Task 2: Writing task (depends on research)
    writing_task = Task(
        description='Using the research findings, write a concise 3-paragraph article '
                    'about how AI agents improve software development. '
                    'Make it accessible to non-technical readers.',
        expected_output='A well-written 3-paragraph article with clear structure.',
        agent=writer
    )
    
    # Create crew with sequential process
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the crew
    print("\n" + "="*60)
    print("STARTING AGENT ORCHESTRATION")
    print("="*60 + "\n")
    
    result = crew.kickoff()
    
    print("\n" + "="*60)
    print("FINAL OUTPUT")
    print("="*60)
    print(result)
    print("="*60 + "\n")
    
    return result


if __name__ == "__main__":
    main()
