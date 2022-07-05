# NBA-player-tracker
A visual web application that displays NBA players' statistics and information.

## Description
This program utilizes the [NBA API](https://github.com/swar/nba_api) to receive player and team data. Handling and cleaning of the data is pre-processed each time the user runs the program or searches for a specific player. A visualization will display in a localhost page consisting of categories of player statistics (points, rebounds, etc.) along with their associated information such as name and team. The search bar is intended for users to lookup NBA players who have played at least one game in the NBA. It will also narrow down search results and display errors if player cannot be found. 

## Getting Started
### Dependencies
* Ensure intended browser of use is updated to most recent version. We recommend using either Google Chrome or Mozilla Firefox.
* Python version is the latest installed.
* pip version is the latest installed.
```
python -m pip install --upgrade pip
```

### Installation
Create a new folder and run the following commands in terminal:
``` 
git clone https://github.com/jdinh-782/NBA-player-tracker.git

cd NBA-player-tracker 
```

Now that you are inside the main directory, please install the included packages:
```
pip install -r requirements.txt
```

### Execution
Assuming all packages and dependencies are installed correctly, the program will run normally and display in [localhost](http://localhost:8000).
```
python3 main.py
```

## Help
Please submit feedback using this [form](https://docs.google.com/forms/d/e/1FAIpQLSfIuycEaVL72vk4nI769YCcoTHdk8jDoh93scR-ie0wnUaPFg/viewform?embedded=true). Otherwise, feel free to reach out to us by [email](jdinh782@gmail.com).

## Authors and Contributors
[Johnson Dinh](https://www.linkedin.com/in/johnson-dinh/) <br>
[Alvin Ly](https://www.linkedin.com/in/alvin-ly-0368491b4/)

## Acknowledgements
[Swar Patel](https://github.com/swar)
