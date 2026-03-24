from bs4 import BeautifulSoup
import re


class ShowdownHTMLReplayParser:

    def __init__(self, filepath):
        self.filename = filepath
        self.lines = []
        self.players = {}
        # Parse the file into text
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                soup = BeautifulSoup(line, "html.parser")
                self.lines.append(soup.get_text())

    def find_mons_brought(self):
        poke_pattern = re.compile(r"\|poke\|([^|]+)\|([^|]+)\|")

        player_data_pattern = re.compile(r"\|player\|([^|]+)\|([^|]+)\|([^|]+)\|")

        for line in self.lines:
            match_poke = poke_pattern.search(line)
            match_player = player_data_pattern.search(line)

            #Should be detected first as all matches start with player info
            if match_player:
                player_id = match_player.group(1)
                player_name = match_player.group(2)

                if player_id not in self.players:
                    self.players[player_id] = {}
                    self.players[player_id]["name"] = player_name
                    self.players[player_id]["pokemon"] = []

            if match_poke:
                player = match_poke.group(1)
                data = match_poke.group(2)
                name,level,gender = data.split(",")

                self.players[player]["pokemon"].append(name)

        return self.players




def main():
    parser = ShowdownHTMLReplayParser("Replays/Gen9VGC2026RegF-2026-03-23-novaka1n-xstarcrossed.html")
    print(parser.find_mons_brought())


if __name__ == "__main__":
    main()