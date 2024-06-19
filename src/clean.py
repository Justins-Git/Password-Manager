import os

# Python script to clean files during testing
def main():
    if os.path.exists("key.key"):
        os.remove("key.key")
    if os.path.exists("master.json"):
        os.remove("master.json")
    if os.path.exists("passwords.json"):
        os.remove("passwords.json")

if __name__ == "__main__":
    main()