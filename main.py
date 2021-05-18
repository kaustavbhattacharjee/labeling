# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from utils import Tweet

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Start Labeling')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#PATH = "Jun/test.csv"
PATH = "Kebby/MarchNonExpertsManualLabel3.csv" #first save the .xlsx file as .csv

tweet = Tweet()
tweets = tweet.import_data(PATH, "csv")
tweets_labeled = tweet.create_labels(tweets)
tweet.save_labels(tweets_labeled, PATH, "csv", index=False)
