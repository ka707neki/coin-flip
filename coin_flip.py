import random
import time

# --- 1. Visual Interface Setup ---
print("=" * 35)
print("   🪙  THE ULTIMATE COIN FLIP  🪙   ")
print("=" * 35)

# --- 2. Randomization Logic Selection ---
print("\nChoose your luck factor:")
print(" [1] random.random()  (Scientific Precision)")
print(" [2] random.randint() (Classic 50/50)")

method = input("\n➤ Select method (1 or 2): ").strip()

# Logic for determining the random result
if method == "1":
    # Relies on decimal floating points (>= 0.5)
    result = "Heads" if random.random() >= 0.5 else "Tails"
elif method == "2":
    # Relies on integer values (0 or 1)
    result = "Heads" if random.randint(0, 1) == 0 else "Tails"
else:
    result = None

# --- 3. Start Guessing Sequence ---
if result is None:
    print("\n❌ Invalid selection! Please restart the game.")
else:
    user_guess = input("➤ Your Guess (Heads / Tails): ").strip().capitalize()

    # Validate that user entered a valid side of the coin
    if user_guess not in ["Heads", "Tails"]:
        print("⚠️ That's not a valid side of a coin! Try again.")
    else:
        # Suspense animation delay
        print("\n" + " flipping " + "● " * 3)
        time.sleep(1)  # Delay for one second to simulate realistic suspense

        # --- 4. Validate Final Result ---
        if user_guess == result:
            print(f"\n✨ BRILLIANT! You guessed it right. It's {result}!")
        else:
            print(
                f"\n💀 UNLUCKY! The coin showed {result}. Better luck next time!"
            )

print("\n" + "=" * 35)
