source ../.venv/bin/activate
python -m cProfile -o profiling-$(date +"%Y%m%d%H%M").cprofile main.py
