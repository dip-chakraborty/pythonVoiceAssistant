import smtplib

# email constraints
sender = "diprajasn441@gmail.com"
password = "Kolkata1!2@3#"
recipient = "dipchakraborty@hotmail.com"
subject = "Sick Day"
message = "Hi Team,\n\nSorry, but I can't make it into work today."

email = "Subject: {}\n\n{}".format(subject, message)
s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()
s.login(sender, password)
s.sendmail(sender, recipient, email)
s.quit()

# success message
print("\nSuccessfully sent a sick-day email to", recipient, "since the travel time was too long")
