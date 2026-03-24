from bs4 import BeautifulSoup

class ShowdownHTMLReplayParser:

    def __init__(self, filepath):
        self.filename = filepath
        # Parse the file into text
        with open(filepath, encoding="utf-8") as f:
            self.html = f.read()
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.text = self.soup.get_text()




def main():
    parser = ShowdownHTMLReplayParser("Replays/Gen9VGC2026RegF-2026-03-23-novaka1n-xstarcrossed.html")
    print(parser.text[:1000])
if __name__ == "__main__":
    main()