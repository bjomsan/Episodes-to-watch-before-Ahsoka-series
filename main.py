# The data gathering and processing is done in 5 steps:
    # Step 1: Read and parse the JSON data from the file
    # Step 2: Use a dictionary to count the mentions of each episode  
    # Step 3: Iterate through the data and update the count of mentions for each episode
    # Step 4: Create a list of tuples in the format (tvshow, season, episode, mentions)
    # Step 5: Sort the episodes based on their total mentions from high-low

# Further on is a number of functions to adjust the output based on user input


# Step 1
import json
with open("data.json", "r") as json_file:
    data = json.load(json_file)


# Step 2
episode_mentions = dict.fromkeys([f"{tv_show}-S{episode['season']:02d}E{episode['episode']:02d}" for tv_show, episodes in data.items() for episode in episodes], 0)


# Step 3
for tv_show, episodes in data.items():
    for episode in episodes:
        season = episode["season"]
        episode_number = episode["episode"]
        episode_key = f"{tv_show}-S{season:02d}E{episode_number:02d}"
        # Increment mention count
        episode_mentions[episode_key] += 1


# Step 4
# we make a complete list of episodes aswell as one with only clonewars and one with only rebels
all_sorted_episodes = []
clonewars_sorted_episodes = []
rebels_sorted_episodes = []

for episode_key, mentions in episode_mentions.items():
    tv_show, season, episode_number = episode_key.split("-")[0], int(episode_key.split("S")[1][:2]), int(episode_key.split("E")[1][:2])
    all_sorted_episodes.append((tv_show, season, episode_number, mentions))

    # check if current episode is clonewars or rebels and append to list
    if tv_show == "clonewars":
        clonewars_sorted_episodes.append((tv_show, season, episode_number, mentions))
    elif tv_show == "rebels":
        rebels_sorted_episodes.append((tv_show, season, episode_number, mentions))


# Step 5
all_sorted_episodes.sort(key=lambda x: x[3], reverse=True)
clonewars_sorted_episodes.sort(key=lambda x: x[3], reverse=True)
rebels_sorted_episodes.sort(key=lambda x: x[3], reverse=True)



# ///////////////////////////////////////////
#                FUNCTIONS 
# ///////////////////////////////////////////



# convert minutes into hours and minutes
def minutes_to_hours_and_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes



# part of sorting episodes in chronological order
def custom_sort_key(episode):
    tv_show, season, episode_number, mentions = episode
    return (tv_show, season, episode_number, mentions)



# print list of recommende episodes and the watch-time
def print_episode_list(episode_list, n):
    # first take the average episode lenght multiplied and convert to hours and minutes
    total_minutes = len(episode_list) * 23
    hours, minutes = minutes_to_hours_and_minutes(total_minutes)

    # we make if sentance to make sure that the program always recommends every episode
    # with the same amount of mentions since they are equally relevant. 
    if n != len(episode_list):
        print(f"""\nEpisodes chosen:{n}
It's recommende to watch an extra {len(episode_list) - n} episodes since they have the same number of mentions.
This makes for a total of {len(episode_list)} episodes.
""")
        
    # print the approx watch-time
    print(f"""Approx. time to watch:
{total_minutes} minutes // {hours} hours and {minutes} minutes.
""")
    
    # sort the recommended episodes by show, season and episode to make it chronological 
    sorted_episodes = sorted(episode_list, key=custom_sort_key)
    print("- Recommended  order of episodes -")
    for i in sorted_episodes:
        print(f"{i[0]} - S{i[1]} E{i[2]} - mentions {i[3]}")



# check if there are more episodes with same number of mentions 
def check_other_episodes(mentions, episode_list, x):  # x stores value from 1-3 to differ what list to use
    if x == 1:
        for i in all_sorted_episodes:
            if i[-1] == mentions and i not in episode_list:
                episode_list.append(i)
    elif x == 2:
        for i in clonewars_sorted_episodes:
            if i[-1] == mentions and i not in episode_list:
                episode_list.append(i)
    elif x == 3:
        for i in rebels_sorted_episodes:
            if i[-1] == mentions and i not in episode_list:
                episode_list.append(i)



# function to print every episode mentioned in chronological order + watch-time
def print_all():
    all_episodes_sorted = sorted(all_sorted_episodes, key=custom_sort_key)
    total_minutes = len(all_episodes_sorted) * 23
    hours, minutes = minutes_to_hours_and_minutes(total_minutes)
    print(f"""Total number of episodes: {len(all_episodes_sorted)}
          
Approx. time to watch:
{total_minutes} minutes // {hours} hours and {minutes} minutes.
""")
    print("- Recommended order of episodes -")
    for i in all_episodes_sorted:
        print(f"{i[0]} - S{i[1]} E{i[2]} - mentions {i[3]}")



# make list of all episodes based on n number of episodes the user wants to see
def both_clonewars_rebels(n):
    if n > len(all_sorted_episodes):
        n = len(all_sorted_episodes)
        print(type(n))
        print("ETTER", n)
        print(f"There is only a total of {n} episodes so here is the complete list:")

    episode_list = []
    for i in range(n):
        episode_list.append(all_sorted_episodes[i])
    # the -1 element is the number of mentions
    temp = episode_list[-1]

    # call function to see if there are other episodes with same num of mentions
    check_other_episodes(temp[-1], episode_list, 1)
    # call function to print the recommende episodes 
    print_episode_list(episode_list, n)



# make list of only CloneWars based on n number of episodes the user wants to see
def only_clonewars(n):
    if n > len(clonewars_sorted_episodes):
        n = len(clonewars_sorted_episodes)
        print(f"There is only a total of {n} episodes so here is the complete list:")

    episode_list = []
    for i in range(n):
        episode_list.append(clonewars_sorted_episodes[i])
    # the -1 element is the number of mentions
    temp = episode_list[-1]

    # call function to see if there are other episodes with same num of mentions
    check_other_episodes(temp[-1], episode_list, 2)
    # call function to print the recommende episodes 
    print_episode_list(episode_list, n)



# make list of only Rebels based on n number of episodes the user wants to see
def only_rebels(n):
    if n > len(rebels_sorted_episodes):
        n = len(rebels_sorted_episodes)
        print(f"There is only a total of {n} episodes so here is the complete list:")

    episode_list = []
    for i in range(n):
        episode_list.append(rebels_sorted_episodes[i])
    # the -1 element is the number of mentions
    temp = episode_list[-1]

    # call function to see if there are other episodes with same num of mentions
    check_other_episodes(temp[-1], episode_list, 3)
    # call function to print the recommende episodes 
    print_episode_list(episode_list, n)



# main function gives user a choice and takes input,
# then call on the other functions to process and print output
def main():
    user_choice1 = input("""Choose action:
Press 1 - Choose how many episodes to watch
Any other action will display total list of recommended episodes
> """)
    try:
        if int(user_choice1) == 1:
            n = int(input("""Insert number of episodes to watch:
> """))
    
        user_choice2 = input("""For Clone Wars only - Press 1
    For Rebels only - Press 2
    For both, press any other key
    > """)
        
        try:
            if int(user_choice2) == 1:
                only_clonewars(n)
            elif int(user_choice2) == 2:
                only_rebels(n)
        except:
            both_clonewars_rebels(n)

    except:
        print_all() 



# call main() function to start the interactive program in terminal
main()
