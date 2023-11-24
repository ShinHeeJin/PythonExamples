import requests
from tenacity import retry, stop_after_delay, wait_fixed

from ex_mailhog.notification import EmailNotification


class MailHogNotRunningException(Exception):
    pass


@retry(stop=stop_after_delay(4), wait=wait_fixed(wait=3), reraise=True)
def wait_for_mailhog_to_come_up():
    print("check mailhog server health check retry ...")
    resp = requests.get("http://0.0.0.0:8025/")
    if resp.status_code == 200:
        return True


def regist_user(email):
    print("regist_user called!")
    send_email(email, f"hello {email}")


def send_email(to, msg):
    print("send_email called!")
    notification = EmailNotification("0.0.0.0", 1025)
    notification.send(to, msg)


def get_email_from_mailhog(email):
    resp = requests.get("http://0.0.0.0:8025/api/v2/messages")
    resp.raise_for_status()
    all_emails = resp.json()
    return next(m for m in all_emails["items"] if email in m["Raw"]["To"])
