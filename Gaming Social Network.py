# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

def create_data_structure(string_input):
    """Create dictionary of users detailing their connections and the games they
    like to play in the format {user: [[connection,...], [game,...]],...}.
    """
    network = {}
    # Divide string_input into sentences.
    sentences = string_input.split('.')
    # Extract user, connection and game details from sentences, then create
    # dictionary entries. ('len(sentences) - 1' avoids empty string at end of
    # list.)
    for i in range(0, len(sentences) - 1, 2):
        user, connections = sentences[i].split(' is connected to ')
        games = sentences[i + 1].split(' likes to play ')[1]
        network[user] = [connections.split(', '), games.split(', ')]
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
    # Proceed if user is in network.
    if user in network:
        # Output list of the people user is connected to.
        return network[user][0]
	return None

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.

def get_games_liked(network, user):
    # Proceed if user is in network.
    if user in network:
        # Output list of the games user likes to play.
        return network[user][1]
    return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.

def add_connection(network, user_A, user_B):
    # Proceed if both users are in network.
    if user_A in network and user_B in network:
        # If user_B is not in user_A's connections, add them.
        if user_B not in network[user_A][0]:
            network[user_A][0].append(user_B)
        return network
    return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)

def add_new_user(network, user, games):
    # If user is not in network, add them.
    if user not in network:
        network[user] = [[], games]
    return network

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_secondary_connections(network, user):
    # Proceed if user is in network.
    if user in network:
        # For all of the people user is connected to, compile set of their
        # connections.
        secondary_connections = []
        for primary in network[user][0]:
            for secondary in network[primary][0]:
                if secondary not in secondary_connections:
                    secondary_connections.append(secondary)
        return secondary_connections
    return None

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.

def connections_in_common(network, user_A, user_B):
    # Proceed if both users are in network.
    if user_A in network and user_B in network:
        # Compare user connections and count matches.
        in_common = 0
        for connection in network[user_A][0]:
            if connection in network[user_B][0]:
                in_common += 1
        return in_common
    return False

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

def path_to_friend(network, user_A, user_B, searched=None):
    # Proceed if both users are in network.
    if user_A in network and user_B in network:
        # Base case: if user_B is in user_A's connections, return.
        if user_B in network[user_A][0]:
            return [user_A, user_B]
        # Upon first call, initialise 'searched' list. List not initialised upon
        # definition to avoid state retention for subsequent non-recursive
        # calls.
        if searched == None:
            searched = []
        # Recurse through user connections until user_B is found or all
        # connections are exhausted.
        for connection in network[user_A][0]:
            if connection not in searched:
                searched.append(connection)
                path = path_to_friend(network, connection, user_B, searched)
                if path:
                    # If user_A is already in path, the interim users are
                    # redundant, so remove them.
                    if user_A in path:
                        return path[path.index(user_A):]
                    return [user_A] + path
    return None

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

def games_chart(network):
    """Creates a list of all the games people like to play, ordered by
    popularity.
    
    Parameter:
    network: the gamer network data structure.
    
    Return:
    chart: a list of tuples, each containing the name of a game and the number
    of people who like to play it, sorted by the latter in descending order.
    
    Sample output:
    >>> print games_chart(network)
    [('Dwarves and Swords', 9), ('Seven Schemers', 6), ('Ninja Hamsters', 4)]
    """
    # Create dictionary containing games (keys) and the number of people who
    # like to play them (values).
    games = {}
    for user in network:
        for game in network[user][1]:
            if game not in games:
                games[game] = 1
            else:
                games[game] += 1
    # Convert dictionary into list of tuples.
    chart = games.items()
    # Sort list by the number of people who like to play each game.
    chart.sort(key=lambda entry: entry[1], reverse=True)
    return chart

net = create_data_structure(example_input)
print net
print path_to_friend(net, "John", "Ollie")
print get_connections(net, "Debra")
print add_new_user(net, "Debra", []) 
print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
print get_connections(net, "Mercedes")
print get_games_liked(net, "John")
print add_connection(net, "John", "Freda")
print get_secondary_connections(net, "Mercedes")
print connections_in_common(net, "Mercedes", "John")
print games_chart(net)