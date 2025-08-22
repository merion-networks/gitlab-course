python -m venv .venv
/.venv/bin/bandit temp.py | grep "High: 0"; echo $?