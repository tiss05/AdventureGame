# Animal Adoption Mini-Game

A simple fun Python console game where you explore a grid to adopt animals!

## How It Works

- **Grid Navigation:**  
  - Move around a 10x10 grid using N (North), S (South), E (East), and O (West).
- **Animal Adoption:**  
  - Every new cell you visit may let you adopt a new animal.
- **Input Validation:**  
  - Only accepts valid directions (N, S, E, O) and converts input to uppercase.
- **Visited Tracking:**  
  - Keeps track of where you’ve been so you can’t adopt the same animal twice from the same spot.

## How to Play

1. **Run the game:**  
   `python game.py`
2. **Enter directions:**  
   Example: `NNNEEESSOO`
3. **See your adopted animals!**

## Testing

Includes automated tests to make sure everything works perfectly:
- **Invalid input doesn’t move you or adopt animals.**
- **Only new cells count for adoption.**
- **Large input (6,000,000 steps)**

**Easy to play, easy to test, and fun to explore!**

