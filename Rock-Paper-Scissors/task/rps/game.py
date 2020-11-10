import random


class RockPaperScissors:

    def __init__(self):
        self.user_choice = ""
        self.computer_choice = ""

    def play_game(self):
        player_name = self._say_hello()
        player_score = self._read_record(player_name)
        game_options = self._take_options()
        while True:
            user_choice, computer_choice = self._take_choices(game_options)
            relation_of_options = self._find_relations(game_options, computer_choice)
            if user_choice == "!exit":
                self._save_record_to_file(player_name, player_score)
                print("Bye!")
                break
            elif user_choice == "!rating":
                print(f"Your rating: {player_score}")
            else:
                winner = self._determine_the_winner(user_choice, computer_choice, relation_of_options)
                self._show_result(winner, computer_choice)
                player_score = self._update_record(winner, player_score)

    @staticmethod
    def _find_relations(game_options, c_input):
        for option in game_options:
            if c_input == option:
                option_index = game_options.index(option)
                relations = game_options[option_index:] + game_options[:option_index]
                relations.remove(option)
                num_of_relations = int(len(relations) / 2)
                relations_dict = {"win": relations[:num_of_relations],
                                  "loss": relations[num_of_relations:]}
                return relations_dict

    @staticmethod
    def _determine_the_winner(u_choice, c_choice, relations_dict):
        winner = ""
        if u_choice in relations_dict["win"]:
            winner = "user"
        elif u_choice in relations_dict["loss"]:
            winner = "computer"
        elif u_choice == c_choice:
            winner = "draw"
        return winner

    @staticmethod
    def _take_options():
        game_options = input("Choose the options to be used (separated by comma): ").split(",")
        if game_options == ['']:
            game_options = ["rock", "paper", "scissors"]
        print("Okay, let's start")
        return game_options

    @staticmethod
    def _say_hello():
        name = input("Enter your name: ")
        print(f"Hello, {name}")
        return name

    @staticmethod
    def _read_record(player_name):
        score = 0
        record_file = open("rating.txt", "r")
        record_list = record_file.readlines()
        for line in record_list:
            if player_name in line:
                line = line.split()
                score = line[1]
        record_file.close()
        return score

    @staticmethod
    def _update_record(winner, player_score):
        player_score = int(player_score)
        if winner == "user":
            player_score += 100
        if winner == "draw":
            player_score += 50
        return player_score

    @staticmethod
    def split_list(file_desc):
        record_list = file_desc.readlines()
        split_list = []
        for line in record_list:
            split_list.append(line.split())
        return split_list

    @classmethod
    def _save_record_to_file(cls, player_name, player_score):
        record_file = open("rating.txt", "r+")
        record_list = cls.split_list(record_file)
        p_score = next((line for line in record_list if player_name == line[0]), None)
        if p_score:
            p_score[1] = str(player_score)
        else:
            new_line = [str(player_name), str(player_score)]
            record_list.append(new_line)
        record_list = list(map(' '.join, record_list))
        record_data = "\n".join(record_list)
        record_file.seek(0)
        record_file.write(record_data)
        record_file.truncate()
        record_file.close()

    def _take_choices(self, game_options):
        self.user_choice = input("Write your choice or !exit/!rating: ")
        self.computer_choice = random.choice(game_options)
        return self.user_choice, self.computer_choice

    @staticmethod
    def _show_result(winner, c_choice):
        if winner == "user":
            print(f"Well done. The computer chose {c_choice} and failed")
        elif winner == "computer":
            print(f"Sorry, but the computer chose {c_choice}")
        elif winner == "draw":
            print(f"There is a draw ({c_choice})")
        else:
            print("Invalid input")


def main():
    rps = RockPaperScissors()
    rps.play_game()


if __name__ == "__main__":
    main()
