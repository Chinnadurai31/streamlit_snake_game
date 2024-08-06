import os
import subprocess

def vulnerable_code():
    # Insecure use of os.system, which can lead to command injection
    os.system("ls")

def hardcoded_secrets():
    # Hardcoded secret key, which is a security vulnerability
    secret_key = "supersecretkey"
    print(f"Secret Key: {secret_key}")

def buggy_code():
    # Potential bug: division by zero
    a = 10
    b = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("Caught division by zero!")

def insecure_subprocess():
    # Insecure use of subprocess without shell escaping
    command = "ls -la"
    subprocess.call(command, shell=True)

def main():
    vulnerable_code()
    hardcoded_secrets()
    buggy_code()
    insecure_subprocess()

if __name__ == "__main__":
    main()
