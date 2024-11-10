from mailersend import emails

mailer = emails.NewEmail("mlsn.27939e69d85339d9e0859fe5d0f105dc1b42ea07a6d895e18e6533af6cda568d")

# define an empty dict to populate with mail values
mail_body = {}

mail_from = {
    "name": "Arthur",
    "email": "amc5347@gmail.com",
}

recipients = [
    {
        "name": "Your Client",
        "email": "cma5347@gmail.com",
    }
]

reply_to = {
    "name": "Name",
    "email": "arthur.coimbra@zukkin.com",
}

mailer.set_mail_from(mail_from, mail_body)
mailer.set_mail_to(recipients, mail_body)
mailer.set_subject("Hello!", mail_body)
mailer.set_html_content("This is the HTML content", mail_body)
mailer.set_plaintext_content("This is the text content", mail_body)
mailer.set_reply_to(reply_to, mail_body)

# using print() will also return status code and data
mailer.send(mail_body)