import functools

SURNAME = "LACDAN"
SEED_NUM = 5

# Logging Decorator
def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed '{func.__name__}'.\n")
        return result
    return wrapper

# ==========================================
# EXERCISE 2: Signal Processing & Analysis
# ==========================================

def generate_signal(surname, seed_num):
    return f"{surname}#{seed_num}*2026!"

def normalize_signal(signal):
    return signal.strip()

def analyze_signal(signal):
    counts = {"uppercase": 0, "lowercase": 0, "digits": 0, "special": 0}
    for char in signal:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        else:
            counts["special"] += 1
    return counts

def classify_signal(counts):
    if counts["special"] > 2 and counts["digits"] > 2:
        return "HIGH COMPLEXITY (MIXED SIGNAL)"
    elif counts["uppercase"] > counts["lowercase"]:
        return "STRONG ALPHA-DOMINANT SIGNAL"
    else:
        return "STANDARD SIGNAL"

@log_execution
def run_exercise_2(surname, seed_num):
    raw_signal = generate_signal(surname, seed_num)
    processed_signal = normalize_signal(raw_signal)
    char_analysis = analyze_signal(processed_signal)
    classification = classify_signal(char_analysis)

    print("=== EXERCISE 2 RESULTS ===")
    print(f"Generated Signal: {raw_signal}")
    print(f"Processed Signal: {processed_signal}")
    print(f"Character Analysis: {char_analysis}")
    print(f"Signal Classification: {classification}")
    print(f"Final Output: Signal processed successfully with classification '{classification}'.")

# ==========================================
# EXERCISE 3: Authentication & Lock System
# ==========================================

def generate_credentials(surname, seed_num):
    password = f"{surname[:3]}_{seed_num}99"
    attempt_limit = seed_num if seed_num >= 3 else 3
    return password, attempt_limit

@log_execution
def run_exercise_3(surname, seed_num, sample_attempts):
    password, limit = generate_credentials(surname, seed_num)
    
    attempts_made = []
    access_result = "DENIED"
    final_state = "LOCKED"

    for idx, attempt in enumerate(sample_attempts, start=1):
        if idx > limit:
            print(f"[SECURITY] Max attempts reached ({limit}). Process terminated.")
            break
            
        attempts_made.append(attempt)
        if attempt == password:
            access_result = "GRANTED"
            final_state = "UNLOCKED"
            break

    print("=== EXERCISE 3 RESULTS ===")
    print(f"Generated Password: {password}")
    print(f"Attempt Limit: {limit}")
    print(f"Attempts Made: {attempts_made}")
    print(f"Access Result: {access_result}")
    print(f"Final System State: {final_state}")
    print(f"Final Output: Authentication ended with status '{access_result}'. System remains {final_state}.")

if __name__ == "__main__":
    run_exercise_2(SURNAME, SEED_NUM)
    print("-" * 50)
    run_exercise_3(SURNAME, SEED_NUM, ["PASS123", "LAC_599", "WRONG"])
