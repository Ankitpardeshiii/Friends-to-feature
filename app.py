from src.data_loader import load_data
from src.friend_recommender import find_people_you_may_know
from src.page_recommender import find_pages_you_might_like

DATA_PATH = "data/data.json"

def main():

    data = load_data(DATA_PATH)

    user_id = 1

    print("Friend Recommendations")
    print(find_people_you_may_know(user_id, data))

    print()

    print("Page Recommendations")
    print(find_pages_you_might_like(user_id, data))


if __name__ == "__main__":
    main()