# Recreate the python virtual environment and reinstall libs on Windows.
# Chris Joakim

$dirs = ".\venv\", ".\pyvenv.cfg"
foreach ($d in $dirs) {
    if (Test-Path $d) {
        echo "deleting $d"
        del $d -Force -Recurse
    } 
}

echo 'creating new venv ...'
python -m venv .\venv\

echo 'activating new venv ...'
.\venv\Scripts\Activate.ps1

echo 'upgrading pip ...'
python -m pip install --upgrade pip 

echo 'install pip-tools ...'
pip install --upgrade pip-tools

echo 'pip-compile requirements.in ...'
pip-compile --output-file .\requirements.txt .\requirements.in

echo 'pip install requirements.txt ...'
pip install -q -r .\requirements.txt

echo 'pip list ...'
pip list > pip_list.txt
pip list

echo 'done; next -> .\venv\Scripts\activate'
