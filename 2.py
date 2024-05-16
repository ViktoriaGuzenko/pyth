def test_create_and_check_post():
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