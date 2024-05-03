import json

def authenticate_user(username, password):
    with open('Lab02.json') as f:
        data = json.load(f)
        if username in data['username']:
            index = data['username'].index(username)
            if password == data['password'][index]:
                return True
    return False

def main():
    # Prompt user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Authenticate user
    if authenticate_user(username, password):
        print("User authenticated!")
    else:
        print("User not authenticated.")

if __name__ == "__main__":
    main()

