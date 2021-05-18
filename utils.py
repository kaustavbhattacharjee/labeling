import pandas as pd
import csv
import os
from pandas import ExcelWriter



class Tweet:
    def import_data(self, PATH, type):
        if type == "xlsx":
            xl = pd.ExcelFile(PATH)
            data = xl.parse("Sheet1")
        if type == "csv":
            data = pd.read_csv(PATH)
        # if type == "csv":
        #     with open(PATH, newline='') as f:
        #         reader = csv.reader(f)
        #         data = list(reader)
        return data

    def label_key2char(self, key):
        """
        :param num: the input x,y,z from keyboard
        :return: fact, opinion, anti-fact, if other than x,y,z return ""
        """
        if key == "0":
            return "fact"
        elif key == "1":
            return "opinion"
        elif key == "2":
            return "misinformation"
        else:
            return ""

    def create_labels(self, df):
        """
        :param df: imported data in dataframe format
        :return: dataframe with added label in ManualLabel column
        """
        labels = df["ManualLabel"].tolist()
        for index, row in df.iterrows():
            if pd.isna(row["ManualLabel"]):
                print("===========")
                print("Tweet Text")
                print(row["Tweet Text"])
                print("===========")
                print("Row Number: "+ str(index))
                print("Subjective: " + str(row["SubjectivityScores"]))
                print("Sentiment: " + str(row["FlairSentimentScore"]) + " " + str(row["FlairSentiment"]))
                print("===========")
                print('Classify as fact(0), opinion(1), misinformation(2) OR Skip(s), Quit(q): ')
                print("Your Label:")
                getch = _Getch()
                label = getch()
                label_char = self.label_key2char(label)
                os.system('cls' if os.name == 'nt' else 'clear')
                if label == "q":
                    break
                labels[index] = label_char
            else:
                continue
        df.drop(columns=["ManualLabel"], inplace=True)
        df["ManualLabel"] = labels
        return df

    def save_labels(self, tweets_labeled, PATH, type, index):
        df = tweets_labeled
        if type == "xlsx":
            writer = ExcelWriter(PATH)
            df.to_excel(writer, 'Sheet1', index=index)
            writer.save()
        if type == "csv":
            df.to_csv(PATH, index=index)


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

