from . import (
    MailHogNotRunningException,
    get_email_from_mailhog,
    regist_user,
    wait_for_mailhog_to_come_up,
)


def test_user_registration():
    try:
        wait_for_mailhog_to_come_up()
    except Exception:
        raise MailHogNotRunningException("Make sure that mailhog docker connector is running!")

    email = "test@test.com"
    regist_user(email)
    messages = get_email_from_mailhog(email)

    assert messages["Raw"]["From"] == "test@test.com"
    assert messages["Raw"]["To"] == ["test@test.com"]
    assert f"hello {email}" in messages["Raw"]["Data"]
