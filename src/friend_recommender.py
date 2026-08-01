def find_people_you_may_know(user_id, data):
    user_friends = {}

    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])

    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    suggestions = {}

    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    sorted_suggestions = sorted(
        suggestions.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [user for user, _ in sorted_suggestions]