# Snake Game

The classic snake game.

## How to play

The recommended way to run the game is Docker with Python 3.13. On macOS,
the default mode uses noVNC and needs only a browser:

```bash
./play.sh
```

Open <http://localhost:6080/vnc.html?autoconnect=1>, then run this command in
the terminal where the container is open:

```bash
python3 run.py
```

On Linux, `./play.sh` uses the host X11 display by default. You can select a
mode explicitly on either platform:

```bash
./play.sh novnc
./play.sh x11
```

To use X11 mode on macOS, install XQuartz, enable **Allow connections from
network clients** in **XQuartz Settings -> Security**, and restart XQuartz:

```bash
brew install --cask xquartz
./play.sh x11
```

The project directory is mounted into `/app`, so local source changes are
immediately visible in the container. Docker uses a dummy audio driver, so the
game runs without sound.

For a local installation, this game requires Python 3 and Pygame.

```
python3 run.py
```

or

```
./play.sh
```

## Rules and features:

1. Turn on sound there is music.
2. You can click the cross or press "Q" any time you want to close the game.
3. To start press "SPACE" and then to choose mode press "1" or "2":
    1) standard
    2) with walls
4. To control snake use arrows or WASD.
5. In game eat apple to grow and getting score.
6. You will die if you crash in:
    1) yourself
    2) boarders
    3) walls
7. There are two bonuses:
    1) ice cream: if you it your snake's speed will increase more than usual, but you will get 6 score points.
    2) pizza: if you eat it your snake will lose some speed, but you will also lose 5 score points.
8. You can press "P" to pause and to unpause the game.
9. If you die press "SPACE" to play again or press "M" to go to menu.
10. In menu press "S" to go to shop.
11. In shop press "S" to go to menu.
12. In shop press "1", "2" or "3" to change snake skin.
13. In shop press "4", "5", "6", "7" or "8" to change background.
14. Good Luck and Have Fun!
