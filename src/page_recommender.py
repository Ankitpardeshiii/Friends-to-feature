def find_pages_you_might_like(user_id, data):

    user_pages = {}

    for user in data["users"]:
        user_pages[user["id"]] = set(user["liked_pages"])

    if user_id not in user_pages:
        return []

    liked_pages = user_pages[user_id]
    recommendations = {}

    for other_user, pages in user_pages.items():

        if other_user == user_id:
            continue

        shared_pages = liked_pages.intersection(pages)

        for page in pages:
            if page not in liked_pages:
                recommendations[page] = (
                    recommendations.get(page, 0)
                    + len(shared_pages)
                )

    return sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )