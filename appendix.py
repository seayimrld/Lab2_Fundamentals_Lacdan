# ==========================================
# TUP ECE - COMPUTER PROGRAMMING EXERCISES
# Student Surname: LACDAN
# ==========================================

SURNAME = "LACDAN"

# ------------------------------------------
# EXERCISE 1: Sensor Reading Validation
# ------------------------------------------
def run_exercise_1():
    print("=== EXERCISE 1 ===")
    seed_num = 2026
    generated_data = ["65", "35", "ERR_DATA", "118", "-20", "75"]

    valid_readings = []
    validation_results = []
    classification_results = []

    for reading in generated_data:
        try:
            val = float(reading)
            valid_readings.append(val)
            validation_results.append("Valid")

            if val < 0 or val > 100:
                classification_results.append("High")
            elif val < 40:
                classification_results.append("Low")
            else:
                classification_results.append("Moderate")
        except ValueError:
            validation_results.append("Invalid")

    avg_valid = sum(valid_readings) / len(valid_readings) if valid_readings else 0

    print("Assessment Data:")
    print("Generated Sensor Data:", ", ".join(generated_data))
    print("Valid/Invalid Results:", ", ".join(validation_results))
    print("Classification Results:", ", ".join(classification_results))
    print("Execution Log:\n [LOG] Process 'process_sensor_system' completed successfully")
    print(f"Final Output:\n {len(generated_data)} total sensor readings    {avg_valid:.2f}\n")


# ------------------------------------------
# EXERCISE 2: Signal Character-by-Character Analysis
# ------------------------------------------
def run_exercise_2():
    print("=== EXERCISE 2 ===")
    seed_num = 2026
    raw_signal = "LACDAN #50 2026!"
    processed_signal = raw_signal.upper()

    lowercase_count = sum(1 for c in raw_signal if c.islower())
    digit_count = sum(1 for c in raw_signal if c.isdigit())
    special_count = sum(1 for c in raw_signal if not c.isalnum() and not c.isspace())

    if special_count >= 3 or len(raw_signal) > 12:
        classification = "High Complexity"
    elif digit_count > 2:
        classification = "Medium Complexity"
    else:
        classification = "Low Complexity"

    print("Assessment Data:")
    print("Generated Signal:", raw_signal)
    print("Processed Signal:", processed_signal)
    print("Character Analysis:")
    print(f"   Lowercase: {lowercase_count}, Digits: {digit_count}, Special: {special_count}")
    print("Signal Classification:", classification)
    print("Execution Log:\n [LOG] Completed run_exercise_2")
    print("Final Output:\n", classification, "\n")


# ------------------------------------------
# EXERCISE 3: Authentication System
# ------------------------------------------
def run_exercise_3():
    print("=== EXERCISE 3 ===")
    seed_num = 599
    generated_password = f"{SURNAME[:3]}-{SEED_NUM}"
    attempt_limit = 5
    attempts_made = ['PASS123', 'LAC-599']

    access_result = "DENIED"
    final_system_state = "LOCKED"

    for i, attempt in enumerate(attempts_made):
        if i >= attempt_limit:
            break
        if attempt == generated_password:
            access_result = "GRANTED"
            final_system_state = "UNLOCKED"
            break

    print("Assessment Data:")
    print("Generated Password:", generated_password)
    print("Attempt Limit:", attempt_limit)
    print("Attempts Made:", attempts_made)
    print("Access Result:", access_result)
    print("Final System State:", final_system_state)
    print("Execution Log:\n [LOG] Completed run_exercise_3")
    print("Final Output:\n", access_result, "\n")


# ------------------------------------------
# MAIN EXECUTION
# ------------------------------------------
if __name__ == "__main__":
    run_exercise_1()
    run_exercise_2()
    run_exercise_3()
    