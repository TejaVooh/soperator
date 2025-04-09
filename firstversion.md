# Soperator – First Version

## Overview
The first version of Soperator is a minimal prototype of a smart DevOps assistant that can:

- Read a plain-text SOP from a local Markdown file.
- Use a local LLM API (such as OpenAI) to parse the SOP and break it into actionable steps.
- Identify steps that may need manual input or intervention.
- Display the plan with clear separation of steps and prompts.

## What It Can Do (v1)
- Read `.md` files from the local `examples/` directory.
- Use OpenAI's API to interpret DevOps instructions.
- Print out step-by-step breakdowns of tasks.
- Highlight manual intervention areas in text form.
- Does not yet execute any real infrastructure changes.
- Does not yet integrate with Jira, Confluence, or GitHub issues.

## Tech Stack
- Python 3
- OpenAI API
- dotenv for secrets
- Local Markdown files as SOP inputs

## Usage
1. Place your SOP in `examples/your_sop.md`.
2. Run `s

