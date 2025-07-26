def brute_force_with_file(target_password, password_file):
    try:
        with open(password_file, 'r') as file:
            attempts = 0
            for line in file:
                guess = line.strip()
                attempts += 1
                print(f"Trying: {guess}")
                if guess == target_password:
                    print(f"\nPassword '{target_password}' cracked in {attempts} attempts!")
                    return
            print("\nPassword not found in the list.")
    except FileNotFoundError:
        print(f"Error: The file '{password_file}' was not found.")

# Example usage
if __name__ == "__main__":
    password = "Password"  # The password to crack
    brute_force_with_file(password, "passwords.txt")