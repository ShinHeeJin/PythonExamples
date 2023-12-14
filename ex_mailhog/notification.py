import smtplib
from abc import ABC, abstractmethod


class AbstractNotifications(ABC):
    @abstractmethod
    def send(self, destination, message):
        raise NotImplementedError


class EmailNotification(AbstractNotifications):
    def __init__(self, smtp_host, smtp_port):
        self.server = smtplib.SMTP(smtp_host, smtp_port)
        self.server.noop()

    def send(self, destination, message):
        msg = f"Subject: test email\n{message}"
        self.server.sendmail(from_addr="test@test.com", to_addrs=[destination], msg=msg)
