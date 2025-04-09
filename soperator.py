import os
import openai
import dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_task_steps(prompt):
    system_message = (
        "You are a helpful DevOps assistant. Read the SOP and break it down into executable steps. "
        "Highlight any manual intervention clearly."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" for free-tier
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    sop = """
    Using https://superset.apache.org/docs/installation/kubernetes deploy superset app
    on azure existing resource group called azstoreagepool with existing container image
    in same resource group named Apache/superset:latest1.1.1
    """

    result = get_task_steps(sop)
    print("\n===== Soperator Task Breakdown =====\n")
    print(result)
