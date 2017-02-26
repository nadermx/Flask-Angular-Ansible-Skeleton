import requests
import config

mgApiKey = config.MAILGUN
domain = config.DOMAIN
title = config.DOMAIN_TITLE
mailingList = 'members@mg.%s' % domain
siteURL = 'https://%s' % domain

# Confirmation email
confirmation_subject = "Confirm your email address"
confirmation_text = lambda x:'<p>Hello, please confirm you want to receive emails from %s by clicking on the ' \
                             'below link <p><a href="https:///users/verify/%s">CONFIRMATION</a></p></p><p></a>'\
                             % x

# Reset password
reset_password_subject = "Reset password"
reset_password_text = lambda a, b, c:'<p>Hello ' + a + ',</p><p>Your username is ' + b + '</p><p>Please click on the below link to reset your password</p><a href="https://%s.com/reset-password/' + c + '">Restore Password</a>'


def reset_password_email(name, username, email, token):
    return requests.post(
       "https://api.mailgun.net/v3/mg.%s/messages" % domain,
       auth= ("api", mgApiKey),
       data= {"from": "%s <no-reply@%s>" % (title, domain),
             "to": "%s" % email,
             "subject": "%s" % reset_password_subject,
             "html": "%s" % reset_password_text(name, username, token)
             }
    ).text


def add_member_unverified(username, email, country):
     return requests.post(
        "https://api.mailgun.net/v3/lists/%s/members" % mailingList,
        auth=('api', mgApiKey),
        data={'subscribed': False,
              'address': email,
              'description': 'Free',
              'vars': '{"username": "%s", "country": "%s", "email": "%s"}' % (username, country, email)})

def send_verification_email(email, token):
     return requests.post(
        "https://api.mailgun.net/v3/mg.%s/messages" % domain,
        auth=("api", mgApiKey),
        data={"from": "%s <no-reply@%s>" % (title, domain),
              "to": "%s" % email,
              "subject": "%s" % confirmation_subject,
              "html": "%s" % confirmation_text(token)}).text

def verify_member(email):
    return requests.put(
            "https://api.mailgun.net/v3/lists/%s/members/%s" % (mailingList, email),
            auth=('api', mgApiKey),
            data={'subscribed': True,
                  'address': email}).text

def unsubscribe_member(email):
    return requests.put(
            "https://api.mailgun.net/v3/lists/%s/members/%s" % (mailingList, email),
            auth=('api', mgApiKey),
            data={'subscribed': False,
                  'address': email}).text
