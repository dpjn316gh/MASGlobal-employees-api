# MASGlobal Employees API

## Running it locally by using PyCharm

1. Make sure you have installed at least python 3.8 and pip. You should use a Virtual
   Environment (<https://docs.python.org/3/tutorial/venv.html>) to run it.
1. Open a terminal and go to the root of this project folder.
1. Activate your Python environment if you are using a Virtual Environment.
    ```
        source bin/activate
    ```
1. Execute:
   ```
   pip install --trusted-host pypi.python.org -r requirements.txt
   ```

1. If you are using PyCharm, go to _Run_ menu, then click on _Edit Configurations..._
1. Add a new _python_ configuration.
1. On _name_ field you can choose the name what you want. E.g. webapp.
1. On _Script Path_ field, set the path of virtual environment of your project. E.g.
   `/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api/venv/bin/flask`
1. On _parameters_ write out `run`.
1. On Environment variables field, add the following ones:

    - `FLASK_APP=src/api_app`
    - `FLASK_ENV=development`
    - `APPLICATION_PATH=/<YOUR ABSOLUTE PATH>/MASGlobal-empoyees-api`
    - `ENVIRONMENT=local`

1. On _working directory_ field, write the path where **MASGlobal-employees-api** virtual environment is in.
E.g. `<YOUR ABSOLUTE PATH>/MASGlobal-employees-api/venv/bin`

1. Modify the file `/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api/deployment/conf/local/app_path.yaml` and modify value of the key `app_path_folder` 
with the value: `<the abosulute path of folder of this project>/MASGlobal-empoyees-api`

1. To check the API es running, go to [http://localhost:5000/](http://localhost:5000/)

1. Finally, open the file _/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api/src/presentation_layer/employee-information.html_ by using a browser.
That's it!.

## Running it locally by using flask

1. Modify the file `/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api/deployment/conf/local/app_path.yaml` and modify value of the key `app_path_folder` 
with the value: `/<YOUR ABSOLUTE PATH>/MASGlobal-empoyees-api`

1. Open a terminal

1. `cd /<YOUR ABSOLUTE PATH>/MASGlobal-employees-api`
1. `cd venv`
1. `source bin/activate`
1. `cd ..`
1. `pip install --trusted-host pypi.python.org -r requirements.txt`
1. `export PYTHONPATH=\$PYTHONPATH:/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api:/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api/src`
1. `export FLASK_APP=/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api/src/api_app`
1. `export APPLICATION_PATH=/<YOUR ABSOLUTE PATH>/MASGlobal-employees-api`
1. `export FLASK_ENV=development`
1. `export ENVIRONMENT=local`
1. `flask run`
1. To check the API es running, go to [http://localhost:5000/](http://localhost:5000/)
1. Finally, open the file _.../MASGlobal-employees-api/src/presentation_layer/employee-information.html_ by using a browser.
That's it!.