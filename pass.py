def check_password(pwd):
    if len(pwd) < 6:
        return "Too short"
    if not any(c.isdigit() for c in pwd):
        return "Must contain a number"
    if not any(c.isupper() for c in pwd):
        return "Must contain an uppercase letter"
    if not any(c.islower() for c in pwd):
        return "Must contain a lowercase letter"
    return "Strong password"

while True:
    pwd = input("Enter password (or 'exit' to quit): ")
    if pwd.lower() == "exit":
        break
    print(check_password(pwd))