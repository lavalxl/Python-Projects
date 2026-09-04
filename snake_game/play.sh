#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
IMAGE_NAME="${SNAKE_GAME_IMAGE:-snake-game:python3.13}"
CONTAINER_DISPLAY="${SNAKE_DISPLAY:-host.docker.internal:0}"
MODE="${1:-auto}"

usage() {
    cat <<'EOF'
Использование: ./play.sh [auto|novnc|x11]

  auto   noVNC на macOS, X11 на Linux (по умолчанию)
  novnc  окно игры в браузере на http://localhost:6080
  x11    прямое X11-окно; на macOS требуется XQuartz
EOF
}

case "$MODE" in
    auto)
        if [[ "$(uname -s)" == "Darwin" ]]; then
            MODE=novnc
        else
            MODE=x11
        fi
        ;;
    novnc | x11) ;;
    -h | --help)
        usage
        exit 0
        ;;
    *)
        usage >&2
        exit 2
        ;;
esac

if ! command -v docker >/dev/null 2>&1; then
    echo "Docker не найден. Установите и запустите Docker Desktop или Colima." >&2
    exit 1
fi

if ! docker info >/dev/null 2>&1; then
    echo "Docker daemon недоступен. Запустите Docker Desktop или 'colima start'." >&2
    exit 1
fi

if [[ "$MODE" == "x11" && "$(uname -s)" == "Darwin" ]]; then
    XHOST_BIN="$(command -v xhost || true)"
    if [[ -z "$XHOST_BIN" && -x /opt/X11/bin/xhost ]]; then
        XHOST_BIN=/opt/X11/bin/xhost
    fi

    if [[ -z "$XHOST_BIN" ]]; then
        cat >&2 <<'EOF'
Для режима x11 на macOS нужен XQuartz.
Установите его командой:

  brew install --cask xquartz

Затем откройте XQuartz Settings -> Security, включите
"Allow connections from network clients" и перезапустите XQuartz.
Либо используйте режим без XQuartz: ./play.sh novnc
EOF
        exit 1
    fi

    open -ga XQuartz
    if ! "$XHOST_BIN" +localhost >/dev/null 2>&1; then
        cat >&2 <<'EOF'
Не удалось разрешить локальное X11-подключение.
Включите "Allow connections from network clients" в настройках XQuartz
или используйте режим без XQuartz: ./play.sh novnc
EOF
        exit 1
    fi
    trap '"$XHOST_BIN" -localhost >/dev/null 2>&1 || true' EXIT
fi

if [[ "$MODE" == "x11" && "$(uname -s)" != "Darwin" ]]; then
    if [[ -z "${DISPLAY:-}" || ! -d /tmp/.X11-unix ]]; then
        echo "Локальный X11-дисплей не найден. Используйте './play.sh novnc'." >&2
        exit 1
    fi

    if command -v xhost >/dev/null 2>&1; then
        xhost +local:docker >/dev/null
        trap 'xhost -local:docker >/dev/null 2>&1 || true' EXIT
    fi
    CONTAINER_DISPLAY="$DISPLAY"
fi

docker build --tag "$IMAGE_NAME" "$SCRIPT_DIR"

echo
echo "Контейнер готов в режиме $MODE."
if [[ "$MODE" == "novnc" ]]; then
    echo "Откройте http://localhost:6080/vnc.html?autoconnect=1"
fi
echo "Для запуска игры выполните: python3 run.py"
echo

DOCKER_ARGS=(
    --rm
    --interactive
    --tty
    --init
    --env SDL_AUDIODRIVER=dummy
    --volume "$SCRIPT_DIR:/app"
    --workdir /app
)

if [[ "$MODE" == "novnc" ]]; then
    DOCKER_ARGS+=(
        --publish 127.0.0.1:6080:6080
        --env DISPLAY=:99
    )
    CONTAINER_COMMAND=(start-novnc)
else
    DOCKER_ARGS+=(--env "DISPLAY=$CONTAINER_DISPLAY")
    if [[ "$(uname -s)" != "Darwin" ]]; then
        DOCKER_ARGS+=(--volume /tmp/.X11-unix:/tmp/.X11-unix:rw)
    fi
    CONTAINER_COMMAND=(bash)
fi

docker run "${DOCKER_ARGS[@]}" "$IMAGE_NAME" "${CONTAINER_COMMAND[@]}"
