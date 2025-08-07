# 🐾 Pet Name Generator & LangChain Agent

A fun and educational project showcasing **LangChain** capabilities through two main features:
1. **Pet Name Generator** - A Streamlit web app that generates creative pet names based on animal type and color
2. **LangChain Agent** - An intelligent agent that can search Wikipedia and perform calculations using multiple tools

## 🚀 Features

### Pet Name Generator
- Interactive web interface built with Streamlit
- Generates 5 creative pet names based on:
  - Pet type (Cat, Dog, Cow, Hamster)
  - Pet color (user input)
- Powered by OpenAI's GPT models via LangChain

### LangChain Agent
- Multi-tool agent that can:
  - Search Wikipedia for factual information
  - Perform mathematical calculations
  - Chain multiple operations together
- Demonstrates the ReAct (Reasoning + Acting) framework
- Verbose output showing the agent's thought process

## 🛠️ Technologies Used

- **LangChain** - Framework for building LLM applications
- **OpenAI API** - GPT models for text generation
- **Streamlit** - Web app framework
- **Python** - Core programming language
- **dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.9 or higher
- OpenAI API key
- Git (for cloning the repository)

## 🔧 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/langchain-llm-app.git
cd langchain-llm-app
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install streamlit langchain langchain-openai langchain-community python-dotenv altair
```

### Step 4: Set Up Environment Variables
1. Create a `.env` file in the project root:
```bash
touch .env
```

2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

**Note**: Get your API key from [OpenAI's platform](https://platform.openai.com/api-keys)

### Step 5: Run the Applications

#### Option A: Pet Name Generator (Streamlit App)
```bash
streamlit run main.py
```
- Open your browser to the URL shown in the terminal (usually `http://localhost:8501`)
- Select your pet type from the sidebar
- Enter your pet's color
- Get 5 creative name suggestions!

#### Option B: LangChain Agent (Terminal)
```bash
python langchain_helper.py
```
- Watch the agent search Wikipedia and perform calculations
- See the step-by-step reasoning process in the terminal

## 📁 Project Structure

```
langchain-llm-app/
├── main.py                 # Streamlit web app
├── langchain_helper.py     # LangChain agent and helper functions
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
└── .venv/                 # Virtual environment (created after setup)
```

## 🎯 Usage Examples

### Pet Name Generator
1. Launch the Streamlit app
2. Choose "Dog" from the dropdown
3. Enter "Golden" as the color
4. Get creative names like "Sunny", "Goldie", "Buttercup", etc.

### LangChain Agent
The agent will:
1. Search Wikipedia for dog lifespan information
2. Extract the average lifespan (typically 10-13 years)
3. Multiply that number by 3 using the calculator tool
4. Show you the complete reasoning process

## 🔍 Key Learning Points

- **LangChain Chains**: See how to chain prompts with LLMs
- **LangChain Agents**: Understand the ReAct framework
- **Tool Integration**: Learn how agents use multiple tools
- **Streamlit Integration**: Build interactive web apps with LLMs
- **Environment Management**: Secure API key handling
- **Modern LangChain**: Uses latest patterns (avoiding deprecated methods)

## 🛡️ Security Notes

- Never commit your `.env` file or API keys to version control
- The `.gitignore` file is configured to exclude sensitive files
- Keep your OpenAI API key secure and monitor usage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Useful Links

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

## ❓ Troubleshooting

### Common Issues

1. **Import Error for `altair.vegalite.v4`**
   ```bash
   pip install 'altair>=4,<5'
   ```

2. **OpenAI API Key Not Found**
   - Ensure `.env` file exists in project root
   - Check that `OPENAI_API_KEY` is correctly set
   - Restart your terminal after creating `.env`

3. **Agent Calculator Errors**
   - The agent needs clear, step-by-step instructions
   - Make sure Wikipedia and calculator tools are properly loaded

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed
2. Verify your OpenAI API key is valid
3. Ensure you're using Python 3.9+
4. Check the [LangChain troubleshooting guide](https://python.langchain.com/docs/troubleshooting)

---

**Happy coding! 🎉** Feel free to experiment with different prompts, add new tools, or extend the functionality!
