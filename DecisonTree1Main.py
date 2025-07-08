from typing import Tuple


class DecisionTree:

    def __init__(self):
        print("Decision Tree part 1 demo.")

    def ask_user(self) -> Tuple[int, int, int, int, int]:
        """
        ask the user the five questions and get a 1-5 answer back for each one.
        :return:
        """
        # Note: You don't need to do dummy-proofing at this stage.
        # for example:
        coldness = int(input("How cold is it outside? (1-5) "))
        # TODO: You write the rest of this, including changing out the example question above.

        return coldness, answer_2, answer_3, answer_4, answer_5

    def decide(self, q1:int, q2:int, q3:int, q4:int, q5:int) -> str:
        """
        take the five values given and use a decision tree to make a recommendation based on them.
        :param q1: The answer to the first question (1-5)
        :param q2: The answer to the second question (1-5)
        :param q3: The answer to the third question (1-5)
        :param q4: The answer to the fourth question (1-5)
        :param q5: The answer to the fifth question (1-5)
        :return: your recommendation
        """
        # TODO: implement this method. (Hint: Don't forget to do a commit to the previous method first.)
        # Note: Please feel free to change the variable names above; fix the corresponding comment if you do so.

    def ask_and_answer(self) -> str:
        a1, a2, a3, a4, a5 = self.ask_user()
        return self.decide(a1, a2, a3, a4, a5)


if __name__ == "__main__":
    dt = DecisionTree()
    print(dt.ask_and_answer())