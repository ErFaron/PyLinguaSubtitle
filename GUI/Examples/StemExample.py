from Stemmer import Stemmer


def run():
    stemmer = Stemmer("english")
    print
    print(stemmer.stemWords(['younger', 'young', 'youngest', 'youngster', 'youngs', 'throwable']))


if __name__ == "__main__":
    run()