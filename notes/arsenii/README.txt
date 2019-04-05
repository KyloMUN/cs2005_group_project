
1.Create an environment
Create a project folder and a venv folder within:
Commands:
	mkdir myproject
	cd myproject
	python3 -m venv venv
2. Activate environment
Command:
	venv/bin/activate

3.Install Flask
Within the activated environment, use the following command to install Flask:
Commands:
	python -m Flask --version
	pip install Flask
	venv/bin/activate
4.Run flask
Commands:
	export FLASK_APP= file_name
	flask run
To stop the development server type CTRL-C in your terminal
5.Deactivating the Virtual Environment
Commands:
	deactivate

