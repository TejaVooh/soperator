# src/soperator/main.py

from .core import get_task_steps

def main():
    sop = """
    Using https://superset.apache.org/docs/installation/kubernetes deploy superset app
    on azure existing resource group called azstoreagepool with existing container image
    in same resource group named Apache/superset:latest1.1.1
    """

    print("Welcome to soperator.\n")
    result = get_task_steps(sop)
    print("===== Soperator Task Breakdown =====\n")
    print(result)

if __name__ == "__main__":
    main()
