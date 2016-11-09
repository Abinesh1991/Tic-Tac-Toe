"""
Its a tic tac too game.
"""
from random import randint
import collections


class TicTacToo:
    def __init__(self):

        self.input_list = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.probability_list = ["123", "456", "789", "147", "258", "369", "753", "159"]

    def display(self):
        print('   |   |')
        print(' ' + str(self.input_list[1]) + ' | ' + str(self.input_list[2]) + ' | ' + str(self.input_list[3]))
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + str(self.input_list[4]) + ' | ' + str(self.input_list[5]) + ' | ' + str(self.input_list[6]))
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + str(self.input_list[7]) + ' | ' + str(self.input_list[8]) + ' | ' + str(self.input_list[9]))
        print('   |   |')

    def select_part(self, select_flag):
        self.user_flag = select_flag
        self.system_flag = 'o' if select_flag > 0 else 'x'
        self.user_flag, self.system_flag

    def play(self):

        game_flag = True
        game_over_flag = 0
        first_entry_flag = 1

        while game_flag:
            print "Please enter number from 1-9"
            select_box = raw_input()

            user_inputs_index = self.get_user_inputs()
            system_inputs_index = self.get_system_inputs()
            if int(select_box) in user_inputs_index or int(select_box) in system_inputs_index:
                print "Please select another box,its already been selected"
                continue
            self.input_list[int(select_box)] = self.user_flag
            if first_entry_flag == 1:
                user_inputs_index = self.get_user_inputs()
                system_inputs_index = self.get_system_inputs()
                while True:
                    first_par = randint(1, 9)
                    if first_par not in user_inputs_index or first_par in system_inputs_index:
                        self.input_list[int(first_par)] = self.system_flag
                        break
            else:
                user_inputs_index = self.get_user_inputs()

                tmp_list1 = []

                for i in user_inputs_index:
                    for j in self.probability_list:
                        if str(i) in j:
                            tmp_list1.append(j)
                final_prob_list = self.get_duplicates(tmp_list1)
                for i in final_prob_list:
                    for j in i:
                        j = int(j)
                        if self.input_list[j] == " ":
                            self.input_list[j] = self.system_flag

                system_inputs_index = self.get_system_inputs()
                tmp_list2 = []
                # for i in system_inputs_index:
                #     for j in self.probability_list:
                #         if str(i) in j:
                #             tmp_list2.append(j)
                #
                # final_system_prob_list = self.get_duplicates(tmp_list2)
                # for i in final_system_prob_list:
                #     for j in self.probability_list:

                if first_entry_flag == 6:
                    print "Game is Draw!!!!!"
                    game_flag = False
            first_entry_flag += 1
            self.display()
            print system_inputs_index

    def get_duplicates(self, _list):
        final_prob_list = [item for item, count in collections.Counter(_list).items() if count > 1]
        return final_prob_list

    def get_user_inputs(self):
        index = [i for i, x in enumerate(self.input_list) if x == self.user_flag]
        return index

    def get_system_inputs(self):
        index = [i for i, x in enumerate(self.input_list) if x == self.system_flag]
        return index


if __name__ == "__main__":
    clsOcbj = TicTacToo()

    print "Please select the shape '1' or '0' "
    while True:
        select = raw_input()
        if select == "1":
            select_flag = 1
            break

        elif select == "0":
            select_flag = 0
            break
        else:
            print "Please select the correct option '1' or '0' "

    clsOcbj.select_part(select_flag)
    clsOcbj.display()
    clsOcbj.play()

