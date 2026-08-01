# 👥 Friends to Features

**Friends to Features** is a Python project that analyzes social network data to generate intelligent recommendations. Using a JSON dataset of users, friendships, and liked pages, the system suggests **people users may know** and **pages they might like** based on mutual connections and shared interests.

## ✨ Features

* 🤝 Recommend people users may know using mutual friends
* 👍 Recommend pages based on shared interests
* 📂 JSON-based data processing
* 🐍 Modular Python project structure
* ⚡ Lightweight and easy to extend

## 📁 Project Structure

```text
Friends-to-Features/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── data.json
│   └── cleaned_data.json
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── friend_recommender.py
│   └── page_recommender.py
│
└── notebooks/
    └── Data_analysis.ipynb
```

## 🛠️ Tech Stack

* Python 3
* JSON
* Git & GitHub

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Ankitpardeshiii/Friends-to-Features.git
```

Navigate to the project directory:

```bash
cd Friends-to-Features
```

Install dependencies (if required):

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python app.py
```

## 🧠 How It Works

### Friend Recommendation

The recommendation engine:

* Identifies the user's direct friends.
* Explores friends-of-friends.
* Excludes existing friends and the current user.
* Ranks suggestions by the number of mutual friends.

### Page Recommendation

The recommendation engine:

* Compares liked pages between users.
* Measures similarity through shared interests.
* Recommends pages the user has not already liked.
* Scores recommendations based on common interests.

## 📄 Sample Dataset

```json
{
  "users": [
    {
      "id": 1,
      "friends": [2, 3],
      "liked_pages": [101, 102]
    }
  ]
}
```

## 🔮 Future Enhancements

* Build a Streamlit web interface
* Visualize the social network with graphs
* Improve recommendations using collaborative filtering
* Support larger datasets
* Add automated testing

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Ankit Pardeshi**

* 🌐 Portfolio: https://ankitpardeshi.xyz
* 🐙 GitHub: https://github.com/Ankitpardeshiii
* 💼 LinkedIn: https://linkedin.com/in/ankitpardeshi

If you found this project helpful, consider giving it a ⭐ on GitHub!
