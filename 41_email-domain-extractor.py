 #3 email domain extractor

emails = ["vishnu@gmail.com", "admin@yahoo.com", "info@openai.com"]

for email in emails:
    domain = email.split("@")[0]
    print(f"Domain: {domain}")

"""
Domain: vishnu
Domain: admin
Domain: info
"""