This app is a one that runs an underground task using huey instead of celery
To start this app, clone the repository into your local
create the virtual environment using 
'''python -m venv venv'''

Then activate virtual environemnt using bash cli
'''source venv/Script/activate'''

To be able to run the app, install the dependencies by running
'''pip install -r requirements.txt'''

Start the task by running
'''python -m runhuey'''

This will connect to the redis which have to be running on your machine.
