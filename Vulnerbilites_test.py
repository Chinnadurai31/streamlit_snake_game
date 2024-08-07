import os
import subprocess
import json
import sys
import time

def vulnerable_code():
    # Insecure use of os.system, which can lead to command injection
    os.system("rm -rf /")  # Critical: Deleting the entire file system

def hardcoded_secrets():
    # Hardcoded secret key, which is a security vulnerability
    secret_key = "supersecretkey"
    api_token = "12345"
    password = "password123"
    print(f"Secret Key: {secret_key}, API Token: {api_token}, Password: {password}")

def buggy_code():
    # Potential bug: division by zero
    a = 10
    b = 0
    result = a / b  # Division by zero
    print(f"Result: {result}")

def insecure_subprocess():
    # Insecure use of subprocess without shell escaping
    command = "ls -la; rm -rf /"  # Command injection vulnerability
    subprocess.call(command, shell=True)

def unsafe_eval():
    # Unsafe use of eval, which can lead to arbitrary code execution
    user_input = input("Enter Python code to execute: ")
    eval(user_input)  # Critical: Arbitrary code execution

def dangerous_pickle():
    # Insecure use of pickle for deserialization, which can lead to arbitrary code execution
    import pickle
    data = pickle.loads(b"cos\nsystem\n(S'rm -rf /'\ntR.")  # Arbitrary code execution

def infinite_loop():
    # Infinite loop bug
    while True:
        print("Infinite loop")

def memory_leak():
    # Memory leak by accumulating large objects
    large_list = []
    while True:
        large_list.append(" " * 10**6)  # 1MB per iteration

def unhandled_exception():
    # Unhandled exception
    result = 10 / 0  # Unhandled division by zero

def bad_practice_mutable_default():
    # Bad practice: mutable default argument
    def append_to_list(item, my_list=[]):
        my_list.append(item)
        return my_list

    print(append_to_list(1))
    print(append_to_list(2))  # List will keep growing

def resource_leak():
    # Resource leak: file not closed
    file = open("test.txt", "w")
    file.write("Hello, World!")  # File not closed

def deprecated_module_usage():
    # Deprecated module usage
    import imp  # Deprecated in favor of importlib

def insecure_hash():
    # Insecure hashing algorithm
    import hashlib
    password = "password123"
    hashed_password = hashlib.md5(password.encode()).hexdigest()  # MD5 is insecure
    print(f"Hashed Password: {hashed_password}")

def no_ssl_verification():
    # No SSL certificate verification
    import requests
    requests.get("https://example.com", verify=False)  # Insecure: no SSL verification

def hardcoded_paths():
    # Hardcoded file paths
    config_path = "/etc/config.json"  # Bad practice: hardcoded path
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

def no_logging():
    # No logging for critical operations
    user_action = input("Enter your action: ")
    if user_action == "delete_all":
        os.system("rm -rf /")  # Critical operation with no logging

def sensitive_data_in_logs():
    # Sensitive data logged
    password = "password123"
    print(f"Logging sensitive data: {password}")  # Sensitive data logged

def bad_error_handling():
    # Bad error handling
    try:
        result = 10 / 0
    except:
        pass  # Swallowing exception without handling

def unoptimized_code():
    # Unoptimized code: redundant calculations
    sum_ = 0
    for i in range(10**6):
        sum_ += i * i  # Can be optimized

def race_condition():
    # Potential race condition
    import threading
    count = 0

    def increment():
        nonlocal count
        for _ in range(1000000):
            count += 1

    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=increment)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(f"Final count: {count}")

def main():
    vulnerable_code()
    hardcoded_secrets()
    buggy_code()
    insecure_subprocess()
    unsafe_eval()
    dangerous_pickle()
    infinite_loop()
    memory_leak()
    unhandled_exception()
    bad_practice_mutable_default()
    resource_leak()
    deprecated_module_usage()
    insecure_hash()
    no_ssl_verification()
    hardcoded_paths()
    no_logging()
    sensitive_data_in_logs()
    bad_error_handling()
    unoptimized_code()
    race_condition()

if __name__ == "__main__":
    main()
