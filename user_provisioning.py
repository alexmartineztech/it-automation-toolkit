import json

def create_user(name, role):
    user = {
        "name": name,
        "role": role,
        "status": "active"
    }
    print(f"User created: {user}")
    return user

def deactivate_user(user):
    user["status"] = "inactive"
    print(f"User deactivated: {user}")

if __name__ == "__main__":
    user1 = create_user("John Doe", "IT Support")
    deactivate_user(user1)
