import os

def main(title):
    if not os.path.exists("../Results"):
        os.makedirs("../Results")
    if not os.path.exists("../Results/" + title):
        os.makedirs("../Results/" + title)
    if not os.path.exists("../Results/" + title + "/Full Scores Of Population"):
        os.makedirs("../Results/" + title + "/Full Scores Of Population")
    if not os.path.exists("../Results/" + title + "/Performance Graphs"):
        os.makedirs("../Results/" + title + "/Performance Graphs")