# Testing python code

https://docs.python.org/3/library/unittest.html

A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

# Setup (before running the frontend/backend tests)

Please navigate to our VM through our: 
[project running instructions](https://gitlab.socs.uoguelph.ca/cis3760team105/3760project/-/blob/Sprint9/docs/running_full_stack_app.md) docs. After executing the instruction: 'pip install -r requirements.txt' proceed below with the backend tests (make sure you're in project/backend directory).

If you want to run the frontend tests, please exit out of the virtual environment (if currently there), which can be easily acheived by opening a new terminal. Then, from the root directory navigate to the project/frontend folder and run 'npm install'. Lastly, navigate to the components directory (project/frontend/src/components) and proceed with the frontend test instructions. After 'npm run test' is ran, you will be taken into JEST CLI, press 'a' to run all tests.


## Backend tests

    python -m unittest

## Frontend tests (created using JEST)

    npm i --save-dev @testing-library/react react-test-renderer
    npm run test
