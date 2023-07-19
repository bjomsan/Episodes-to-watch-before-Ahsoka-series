# Episodes-to-watch-before-Ahsoka-series
A program to determine what episodes of Star Wars the Clone Wars and Rebels are most crucial to watch/rewatch before the Ahsoka live-action series, based on how many episodes the user is willing to watch.

WHY? Many recommended episodes to watch are available on Google, but I didn't want to rely on a single source. This Python program takes n number of episodes the user is willing to watch, and outputs a list of episodes in chronological order + approx watch-time for the episodes.

The data in the data.json file is manually collected from the top Google searches on what to watch before the upcoming Ahsoka series. 
The JSON file is structured with one key for Clone Wars and one key for Rebels. Each key contains a list of values: "season" and "episode".

The main.py file is the program that processes the JSON data and creates a list-output of episodes. This is  done by counting the number of mentions of each episode to then determine what episodes are more and less important.

To execute the program, run the main.py file with the data.json file in the same folder.
