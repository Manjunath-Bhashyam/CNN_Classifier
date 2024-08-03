echo [$(date)]: "START"
echo [$(date)]: "Creating env with Python3.10"
python -m venv env
echo [$(date)]: "Activating env"
source env/scripts/activate
echo [$(date)]: "Installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"