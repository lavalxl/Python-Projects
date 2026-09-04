#!/usr/bin/env bash

set -euo pipefail

DISPLAY_NUMBER="${DISPLAY:-:99}"
SCREEN_SIZE="${NOVNC_SCREEN_SIZE:-1280x720x24}"

cleanup() {
    jobs -pr | xargs -r kill 2>/dev/null || true
}
trap cleanup EXIT

Xvfb "$DISPLAY_NUMBER" -screen 0 "$SCREEN_SIZE" -nolisten tcp &

for _ in $(seq 1 50); do
    if xdpyinfo -display "$DISPLAY_NUMBER" >/dev/null 2>&1; then
        break
    fi
    sleep 0.1
done

if ! xdpyinfo -display "$DISPLAY_NUMBER" >/dev/null 2>&1; then
    echo "Не удалось запустить виртуальный X11-дисплей." >&2
    exit 1
fi

DISPLAY="$DISPLAY_NUMBER" openbox >/tmp/openbox.log 2>&1 &
x11vnc -display "$DISPLAY_NUMBER" -forever -shared -nopw \
    -rfbport 5900 -quiet >/tmp/x11vnc.log 2>&1 &
websockify --web=/usr/share/novnc 6080 localhost:5900 \
    >/tmp/websockify.log 2>&1 &

echo
echo "noVNC запущен: http://localhost:6080/vnc.html?autoconnect=1"
echo "В этом терминале выполните: python3 run.py"
echo

exec bash
