import pandas as pd
import csv
import os



class Tweet:
    def import_data(self, PATH, type):
        # if type == "xlsx":
        #     xl = pd.ExcelFile(PATH)
        #     data = xl.parse("Sheet1")
        if type == "csv":
            data = pd.read_csv(PATH)
        # if type == "csv":
        #     with open(PATH, newline='') as f:
        #         reader = csv.reader(f)
        #         data = list(reader)
        return data

    def label_num2char(self, num):
        """
        :param num: the input 1,2,3 from keyboard
        :return: fact, opinion, anti-fact, if other than 1,2,3,4 or z, return ""
        """
        if num == "1":
            return "fact"
        elif num == "2":
            return "opinion"
        elif num == "3":
            return "anti-fact"
        else:
            return ""

    def create_label(self, df):
        """
        :param df: imported data in dataframe format
        :return: dataframe with added label in ManualLabel column
        """
        labels = df["ManualLabel"].tolist()
        for index, row in df.iterrows():
            if pd.isna(row["ManualLabel"]):
                print(row["Tweet Text"])
                print("===========")
                print("Subjective: " + str(row["SubjectivityScores"]))
                print("Sentiment: " + str(row["FlairSentimentScore"]) + " " + str(row["FlairSentiment"]))
                print('fact(1), opinion(2), anti-fact(3), end(z): ')
                getch = _Getch()
                label = getch()
                label_char = self.label_num2char(label)
                os.system('cls' if os.name == 'nt' else 'clear')
                if label == "z":
                    break
                labels[index] = label_char
            else:
                continue
        df.drop(columns=["ManualLabel"], inplace=True)
        df["ManualLabel"] = labels
        return df

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
