# How To Setup Environment
## Non scripted setup:
**Note this Only Needs to Be Done ONCE**
## Windows
- Clone the Repo 
- In terminal Go To the Project/Backend folder
- `python -m venv env`
- `env\Scripts\activate.bat`
- `pip install -r requirements.txt`
- In terminal Go To the Project/Frontend folder
- `npm install`

## MacOS/Linux VM
- Clone the Repo 
- In terminal Go To the Project/Backend folder
- `python -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- In terminal Go To the Project/Frontend folder
- `npm install`

# How to Run the Full Stack App
## Windows
- In terminal Go To the Project/Backend folder
- `env\Scripts\activate.bat`
- **If exisits: Delete the __init__.py file in the project directory**
- `flask run`
- In terminal Go To the Project/Frontend folder
- `npm start`

## MacOS/Linux VM
- In terminal Go To the Project/Backend folder
- `source env/bin/activate`
- **If exisits: Delete the __init__.py file in the project directory**
- `flask run`
- In terminal Go To the Project/Frontend folder
- `npm start`


# back-end lint:
- Make sure the project environment has been correctly setup
- Start the env, see above for instructions on how to
- Download all the updated packages: 
- `pip install -r requirements.txt`
- nagivate to the project/backend folder, and run: 
- `pylint app.py`

# front-end lint:
- Change directory to "project/frontend/src"
- run `npx eslint --fix .`
- If there is no output, there are no errors found by the linter.

# Common Issues
## Some Python package missing?:
- In terminal Go To the Project/Backend folder
- Make sure there is a folder called env
- If not, please follow the instructions for setup environment: backend
- If there is: run the below commands:
- `env\Scripts\activate.bat`
- `pip install -r requirements.txt`
