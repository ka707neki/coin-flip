# 🪙 Coin Flip

A small terminal game where you guess the outcome of a coin flip. You choose which random-number method decides the result, make your guess, and see whether luck is on your side.

## Features

- Choice of two randomization methods:
  - `random.random()` — heads if the float is `>= 0.5`
  - `random.randint(0, 1)` — heads on `0`, tails on `1`
- Case-insensitive guesses (`heads`, `HEADS`, and `Heads` all work)
- Input validation for both the method choice and the guess
- Short suspense animation before the result is revealed
- No external dependencies — standard library only

## Requirements

- Python 3.6+ (uses f-strings)
- A terminal with UTF-8 support for the emoji

## Usage

```bash
git clone https://github.com/ka707neki/coin-flip.git
cd coin-flip
python3 coin_flip.py
```

## Sample Session

```
===================================
   🪙  THE ULTIMATE COIN FLIP  🪙
===================================

Choose your luck factor:
 [1] random.random()  (Scientific Precision)
 [2] random.randint() (Classic 50/50)

➤ Select method (1 or 2): 2
➤ Your Guess (Heads / Tails): heads

 flipping ● ● ●

✨ BRILLIANT! You guessed it right. It's Heads!

===================================
```

## How It Works

1. The player selects a randomization method (`1` or `2`).
2. The program generates the result **before** asking for the guess.
3. The player's guess is normalized with `.strip().capitalize()` and validated.
4. A one-second delay (`time.sleep`) builds suspense, then the guess is compared with the result.

## Possible Improvements

- Loop to play multiple rounds with a score counter
- Option to flip several coins at once
- Statistics showing the heads/tails ratio over many flips

## License

Released under the [MIT License](LICENSE).
