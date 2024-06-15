<h1>Random word task app</h1>
<p>This app is a one that runs an underground task using huey instead of celery</p>
<p>To start this app, clone the repository into your local
create the virtual environment using </p>

```python -m venv venv```

<p>Then activate virtual environemnt using bash cli</p>
```source venv/Script/activate```

To be able to run the app, install the dependencies by running
```pip install -r requirements.txt```

<p>Start the task by running</p>
```python -m runhuey```

This will connect to the redis which have to be running on your machine.

<h4 align="left">Credit: </h4>
Developed by Seun
