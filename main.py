from fetch_data import fetch_data
from send_mail import send_mail
from update_sent_email import update_sent_email

data = fetch_data()

with open("log.txt", "a") as log:
    for row in data:
        try:
            send_mail(
                row["events"]["roles"][0]["users"]["email"],
                row["users"]["email"],
                row["users"]["name"],
                row["events"]["event_name"],
                row["events"]["registration_fees"],
                row["created_at"],
                row["transaction_id"],
            )
            update_sent_email(row["team_id"])
            log.write("Success -> " + row["users"]["email"] + "\n")

        except Exception as e:
            print("failed -> " + row["users"]["email"] + str(e))
            log.write("failed -> " + row["users"]["email"] + str(e) + "\n")
