# CrewAI Agent Orchestration Example

A bare-bones example of orchestrating 2 AI agents using CrewAI and Ollama LLM.

## Architecture

- **Researcher Agent**: Gathers and analyzes information on a topic
- **Writer Agent**: Creates written content based on research findings
- **Sequential Process**: Research task completes before writing task begins

## Prerequisites

1. **Install Ollama**: https://ollama.ai/download
2. **Pull Llama model**:
   ```bash
   ollama pull llama3.2
   ```
3. **Ensure Ollama is running**:
   ```bash
   ollama serve
   # Or just run: ollama run llama3.2
   ```

## Setup

Install dependencies with uv:
```bash
uv sync
```

## Usage

Run the example:
```bash
uv run main.py
```

Or activate the virtual environment:
```bash
source .venv/bin/activate  # On Unix/macOS
# .venv\Scripts\activate   # On Windows
python main.py
```

## How It Works

1. **Researcher Agent** receives a research task and gathers information
2. **Writer Agent** receives the research output and creates an article
3. **Crew** orchestrates the sequential execution of tasks
4. Final output is displayed

## Customization

Modify `main.py` to:
- Change the topic in task descriptions
- Add more agents to the crew
- Switch to `Process.hierarchical` for different orchestration
- Use different Ollama models (llama3.1, mistral, etc.)
- Add tools to agents for real web search, file operations, etc.

## Example Output

The agents will collaborate to:
1. Research AI agents in software development
2. Write a 3-paragraph article based on findings

Each agent's thought process is visible in verbose mode.

## Environment Setting
Save a .env file like the following
```bash
# CrewAI requires OPENAI_API_KEY to be set even when using other LLMs
# Setting a dummy value since we're using Ollama
OPENAI_API_KEY=sk-dummy-key-not-used

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Suppress LiteLLM logging errorsxg
LITELLM_LOG=ERROR

CREWAI_TRACING_ENABLED=true
```
