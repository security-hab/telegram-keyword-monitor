
# 📡 Telegram Keyword Monitor

🚀 **Telegram Keyword Monitor** is a bot built with the [Telethon](https://docs.telethon.dev) library. It monitors messages in specified Telegram channels and automatically forwards those containing specific keywords to your group.

---

## ✨ Key Features:
- 🔍 **Real-time monitoring** of keywords in Telegram channels.
- 🔗 **Extracts links** from messages and prints them to the console.
- 🔄 **Automatically forwards** relevant messages to a designated group.
- 🛡️ **Supports two-factor authentication**.

---

## 🛠️ Requirements
Ensure you have the following installed:
- Python 3.7+ 🐍
- Telethon library 📚

---

## 🚀 Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/security-hab/telegram-keyword-monitor.git
   cd telegram-keyword-monitor
   ```

2. Install dependencies:
   ```bash
   pip install telethon
   ```

3. Configure the settings:
   - Open the `main.py` file.
   - Replace the following placeholders with your data:
     - `api_id` and `api_hash` (obtain them from [my.telegram.org](https://my.telegram.org)).
     - List of channels (`channels_to_monitor`).
     - List of keywords (`keywords`).
     - Your group's ID (`group_id_for_notifications`).

4. Run the bot:
   ```bash
   python main.py
   ```

---

## ⚙️ Setting Up Environment Variables (Optional)
To keep your sensitive data secure, use an `.env` file:

1. Install the required library:
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file in the project root and add your data:
   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   PASSWORD=your_password
   GROUP_ID=your_group_id
   ```

3. Update the code to load values from `.env`.

---

## 📝 Example Data Structure
### Channels to Monitor:
```python
channels_to_monitor = [
    'channel_username_1',
    'channel_username_2',
    'channel_username_3'
]
```

### Keywords:
```python
keywords = ['keyword1', 'keyword2', 'keyword3']
```

---

## 🤔 How to Get Your Group ID?
1. Add the bot [@userinfobot](https://t.me/userinfobot) to your group.
2. Send any message to the group.
3. The bot will return the group ID (formatted as `-1001234567890`).

---

## 💡 Ideas for Improvement
- Add logging to track errors and bot activities.
- Integrate with a database to store message history.
- Add a graphical user interface (GUI).

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

## 📬 Contact
For questions or suggestions, feel free to reach out via [Telegram](https://t.me/guardianhab).

---
