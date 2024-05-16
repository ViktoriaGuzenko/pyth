def test_contact_us_form():
    open_contact_us_form()
    contact_data = {
        "name": "Иванов Иван",
        "email": "ivanov@example.com",
        "message": "Тестовое сообщение для Contact Us формы"
    }
    fill_contact_form(contact_data)
    submit_contact_form()
    alert_text = get_alert_text()
    assert "Спасибо за ваше сообщение!" in alert_text