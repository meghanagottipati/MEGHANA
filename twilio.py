from twilio.rest import Client

def sign_in_simulation():
    # Predefined username and password
    correct_username = "MEGHANA"
    correct_password = "2011"

    print("Welcome to the Sign-In Page")

    for attempt in range(2):  # Allow 2 attempts in total
        # Get user input
        username = input("Enter your username: ").strip().upper()  # Normalize username
        password = input("Enter your password: ")

        # Basic validation for empty input
        if not username or not password:
            print("Username and password cannot be empty. Please try again.")
            continue

        # Check if the credentials are correct
        if username == correct_username and password == correct_password:
            print("Sign-in successful!")
            send_successful_sign_in_sms()  # Call function to send SMS
            return  # Exit the function on successful sign-in
        else:
            if attempt < 1:  # If not the last attempt
                print("Invalid username or password. Please try again.")
            else:
                print("Invalid username or password. No attempts remaining.")
    print("Sign-In failed please contact customer support!")


def send_successful_sign_in_sms():
    # Twilio authentication details (included directly for testing)
    account_sid = "AC9e2ec7f7825ed995456a7a82542341db"
    auth_token = "f8ec6e12ef1ab73491ba567a11cccdf6"
    client = Client(account_sid, auth_token)

    # Send an SMS when the user signs in successfully
    message = client.messages.create(
        body="Sign-in successful for MEGHANA.",
        from_="+17722131843",  # Your Twilio phone number
        to="+91xxxxxxxxxx",  # Your phone number
    )

    # Print confirmation
    print(f"Message sent: {message.body}")


# Run the sign-in simulation
if __name__ == "__main__":
    sign_in_simulation()
