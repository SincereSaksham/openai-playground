# 🧪 Prompt Playground (Console-Based)

This is a console-based Prompt Playground that lets users explore how different OpenAI completion parameters affect the output of a product description prompt.

---

## 📦 Features

- 🔧 Accepts user input for:
  - System Prompt
  - User Prompt
  - Model (currently hardcoded to `gpt-3.5-turbo`)
- 🎛️ Allows testing across different values of:
  - `temperature`: 0.0, 0.7, 1.2
  - `max_tokens`: 50, 150, 300
  - `presence_penalty`: 0.0, 1.5
  - `frequency_penalty`: 0.0, 1.5
- 🧠 Automatically runs the prompt across all combinations (Cartesian product)
- 📊 Generates a results table (with one row marked as `*` for the user-chosen parameters)
- 📄 Saves:
  - Results table
  - All full responses
  - 2-paragraph reflection
  ... into a single `.txt` file

---

## 🛠️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/SincereSaksham/openai-playground.git
   cd openai-playground
   ```

2. Install dependencies:
   ```
   pip install openai
   ```
3. Run the script:
   ```
   python playground.py
   ```

## 📋 Output Table Example (Partial

| Mark | Temp | Max Tokens | Presence Penalty | Frequency Penalty | Output                                      |
| ---- | ---- | ---------- | ---------------- | ----------------- | ------------------------------------------- |
| \*   | 0.7  | 150        | 0.0              | 0.0               | The iPhone is a revolutionary smartphone... |
|      | 1.2  | 150        | 1.5              | 0.0               | Apple’s iPhone takes smart to the next...   |

The stark mark in the first row shows the output for user chosen input ! 


## ✨ Reflection
Varying the parameters had a noticeable impact on the style and content of the responses:

Increasing temperature made the descriptions more creative and expressive but sometimes inconsistent. For example, at temperature = 1.2, the iPhone was described in a more metaphorical tone, while at 0.0, the description remained factual and dry.

Higher presence_penalty and frequency_penalty led to more varied phrasing and reduced repetition, which made responses feel more natural and less robotic. However, it occasionally caused important details to be omitted.

This experimentation shows how fine-tuning parameters can dramatically affect the tone, creativity, and informativeness of AI-generated content.

## 📁 Output File
All data is saved in a file named something like:
prompt_results_2025-06-11_21-48-00.txt

This includes:

1. Full table of configurations and responses

2. Full-length outputs

3. Final 2-paragraph reflection
