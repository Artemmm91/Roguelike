DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd ${DIR}
mkdir backend
cd backend
pip3 install virtualenv
python3 -m venv ./venv
source venv_project/bin/activate
pip3 install -r ../requirements.txt
cd ..
python3 main.py
