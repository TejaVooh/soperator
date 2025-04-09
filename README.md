# soperator

AI-powered agent that reads SOPs from Jira, Confluence, GitHub, or Markdown files — and executes or outlines infrastructure tasks.

## What is soperator?

`soperator` is a smart DevOps assistant that understands natural language SOPs—no matter where they live. Whether written in Jira tickets, Confluence docs, GitHub issues, or Markdown files, it can:

- Parse and interpret deployment or setup instructions  
- Identify steps requiring manual input and prompt for them if needed  
- Execute tasks directly or generate detailed, actionable plans  
- Notify at each stage of execution or planning  

The idea is the brainchild of **Himanshu V Kulkarni**.  
It’s built for DevOps teams, SREs, and platform engineers who want to automate routine infrastructure tasks without reinventing the wheel.

## Use Case Example

A Jira issue says:

"Using https://superset.apache.org/docs/installation/kubernetes, deploy Apache Superset on Azure in the existing resource group `azstoragepool`, using the container image `apache/superset:latest1.1.1`."

`soperator` can:
- Parse this input
- Understand relevant setup requirements
- Identify credentials or resource gaps
- Prompt the user or read from a config file
- Deploy Superset or generate a shell script/plan

## Tech Stack

- OpenAI GPT (4o or 4-turbo) for task understanding
- Jira, Confluence, GitHub APIs for content ingestion
- Python (or Node.js) CLI interface
- YAML, JSON, Markdown support for local SOPs

## Getting Started

```bash
git clone https://github.com/yourusername/soperator
cd soperator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI and source API keys
python src/main.py

