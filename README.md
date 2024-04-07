# AxaSearch

A simple Search Engine written in Python

<h2>Installation</h2>

Simply download the files and create a new virtual environment with ```python3 -m venv venv``` in the main directory of the files.

After that activate the venv with ```source venv/bin/activate``` under linux and under windows with ```./venv/Scripts/activate```.

Next you have to edit the Whitelist under Scraper/data/Whitelist.json, you got to add your domains like this:```Whitelist: ["somedomain.com"]``` to add your domains.

After that run ```python3 Scraper/Scraper.py``` to run the Scraper and create your database.

Then you only have to start the Server through ```python3 Server.py```.

Enjoy!
