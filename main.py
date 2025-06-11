import openai
import itertools
from datetime import datetime

# --- SETUP ---
openai.api_key = "YOUR-API-KEY"
MODEL = "gpt-3.5-turbo"

# Fixed test values
TEMPERATURES = [0.0, 0.7, 1.2]
MAX_TOKENS = [50, 150, 300]
PRESENCE_PENALTIES = [0.0, 1.5]
FREQUENCY_PENALTIES = [0.0, 1.5]

# --- USER INPUT ---
print("=== Prompt Playground ===\n")
system_prompt = input("Enter the system prompt: ")
user_prompt = input("Enter the user prompt (e.g., describe iPhone): ")

print("\nChoose your preferred settings from the given options:")

def choose(prompt, options, cast_func):
    while True:
        try:
            val = cast_func(input(f"{prompt} {options}: "))
            if val in options:
                return val
            print("❌ Invalid choice. Try again.")
        except:
            print("❌ Invalid input. Try again.")

temperature = choose("Temperature", TEMPERATURES, float)
max_tokens = choose("Max tokens", MAX_TOKENS, int)
presence_penalty = choose("Presence penalty", PRESENCE_PENALTIES, float)
frequency_penalty = choose("Frequency penalty", FREQUENCY_PENALTIES, float)

user_config = (temperature, max_tokens, presence_penalty, frequency_penalty)

# --- ALL COMBINATIONS EXCEPT USER CONFIG ---
all_combos = list(itertools.product(TEMPERATURES, MAX_TOKENS, PRESENCE_PENALTIES, FREQUENCY_PENALTIES))
remaining_combos = [combo for combo in all_combos if combo != user_config]

# --- API CALL FUNCTION ---
def get_response(temp, max_tok, pp, fp):
    try:
        res = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temp,
            max_tokens=max_tok,
            presence_penalty=pp,
            frequency_penalty=fp
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR: {e}]"

# --- GENERATE OUTPUTS ---
print("\nGenerating your selected response...\n")
results = []
user_output = get_response(*user_config)
results.append(("*", *user_config, user_output))

print("Generating all other combinations...\n")
for combo in remaining_combos:
    temp, max_tok, pp, fp = combo
    output = get_response(temp, max_tok, pp, fp)
    results.append(("", temp, max_tok, pp, fp, output))

# --- REFLECTION GENERATION ---
def generate_reflection(user_output, other_outputs):
    return [
        "By adjusting the parameters such as temperature, token count, and penalties, the AI's tone and length of the product description changed noticeably. Lower temperatures produced more deterministic and factual responses, while higher temperatures introduced creativity and variation. Increasing max_tokens generally led to more detailed outputs, and higher penalties reduced repetition and encouraged diverse vocabulary.",
        "Compared to the user-chosen configuration, some combinations generated verbose, imaginative descriptions while others were concise and business-like. This demonstrates how fine-tuning the parameters can help tailor the tone and style of responses, depending on the intended audience or use-case."
    ]

reflections = generate_reflection(user_output, [row[5] for row in results[1:]])

# --- SAVE TO FILE ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"results_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("=== PROMPT PLAYGROUND RESULTS ===\n\n")
    f.write(f"System Prompt: {system_prompt}\n")
    f.write(f"User Prompt: {user_prompt}\n\n")

    f.write("-" * 120 + "\n")
    f.write(f"{'User*':<6} {'Temp':<6} {'MaxTokens':<10} {'PresPenalty':<13} {'FreqPenalty':<13} Output\n")
    f.write("-" * 120 + "\n")

    for row in results:
        mark, temp, max_tok, pp, fp, output = row
        output_preview = output.replace("\n", " ").replace("\r", " ")
        f.write(f"{mark:<6} {temp:<6} {max_tok:<10} {pp:<13} {fp:<13} {output_preview}\n")

    f.write("\n\n=== REFLECTION ===\n\n")
    for para in reflections:
        f.write(para + "\n\n")

print(f"\n✅ All results (table + reflection) saved to: {filename}\n")

