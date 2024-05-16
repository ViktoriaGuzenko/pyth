import pytest

@pytest.mark.ui_test
def test_create_and_check_post(driver):
    print("Начало теста test_create_and_check_post")

    try:
        new_post_data = {
            "title": "Новый пост",
            "description": "Описание нового поста"
        }
        response = create_post(new_post_data)
        assert response.status_code == 201
        posts = get_all_posts()
        post_descriptions = [post['description'] for post in posts]
        assert new_post_data["description"] in post_descriptions
        driver.refresh()
        post_titles = [post["title"] for post in get_all_posts_from_page()]
        assert new_post_data["title"] in post_titles

    except Exception as e:
        print(f"Ошибка в тесте test_create_and_check_post: {str(e)}")
        raise

    finally:
        print("Тест test_create_and_check_post завершен")

@pytest.mark.ui_test
def test_contact_us_form(driver):
    print("Начало теста test_contact_us_form")

    try:
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

    except Exception as e:
        print(f"Ошибка в тесте test_contact_us_form: {str(e)}")
        raise

    finally:
        print("Тест test_contact_us_form завершен")