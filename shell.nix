{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.virtualenv
    nodejs_20
    tmux
    git
  ];

  VIRTUAL_ENV_DISABLE_PROMPT = "1";
  PIP_DISABLE_PIP_VERSION_CHECK = "1";

  shellHook = ''
    set -e

    echo "Entering Django dev shell..."

    # Ensure we are in project root
    if [ ! -f manage.py ]; then
      echo "Warning: manage.py not found. Run nix-shell in Django project root."
    fi

    # Create virtualenv if missing
    if [ ! -d "venv" ]; then
      echo "Creating virtualenv..."
      python -m venv venv
    fi

    # Activate venv
    source venv/bin/activate

    # Install requirements automatically
    if [ -f requirements.txt ]; then
      echo "Installing requirements..."
      python -m pip install --upgrade pip wheel setuptools >/dev/null
      pip install -r requirements.txt
    fi

    # -------- Commands --------

    # startapp <name>
    startapp () {
      if [ -z "$1" ]; then
        echo "Usage: startapp appname"
        return 2
      fi
      mkdir -p apps
      python manage.py startapp "$1" "apps/$1"
      echo "App '$1' created in apps/$1"
    }

    # frontend install / watch
    frontend () {
      case "$1" in
        install)
          python manage.py tailwind install
          ;;
        watch)
          python manage.py tailwind start
          ;;
        *)
          echo "Usage:"
          echo "  frontend install   -> install Tailwind frontend"
          echo "  frontend watch     -> run Tailwind watcher"
          ;;
      esac
    }

    export -f startapp frontend

    # -------- TMUX AUTO SPLIT --------
    if [ -n "$PS1" ] && command -v tmux >/dev/null 2>&1 && [ -z "$TMUX" ]; then
      SESSION="django"
      if tmux has-session -t "$SESSION" 2>/dev/null; then
        tmux attach -t "$SESSION"
      else
        tmux new-session -d -s "$SESSION"
        tmux split-window -v -t "$SESSION"
        tmux select-pane -t "$SESSION:0.0"
        tmux attach -t "$SESSION"
      fi
    fi

    echo ""
    echo "Available commands:"
    echo "  startapp myapp"
    echo "  frontend install"
    echo "  frontend watch"
    echo ""
  '';
}