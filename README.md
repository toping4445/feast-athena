1. create venv "python3 -m venv .venv"
2. activate venv "source .venv/bin/activate"
3. install required libraries "pip3 install -r requirements.txt"
4. move the files in custom_proto to feast/protos/feast/core 
5. execute a command "python3 setup.py build_python_protos" in the feast directory
6. move the protos artifacts(feast/build/lib.macosx~~~/feast/protos/feast/core) to .venv/lib/python3.7/site-packages/feast/protos/feast/core
7. (optional on AWS) "pip3 install ipykernel"
8. (optional on AWS) "python3 -m ipykernel install --user --name .venv --display-name venv"

