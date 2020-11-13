"""
Input/Output をするクラス
"""


class OperationIO:
    def printBot(self, text, sep="", end="\n"):
        """
        ボット出力関数
        """
        print("BOT:「 {} 」".format(text), sep=sep, end=end)

    def printUser(self, text, sep="", end="\n"):
        """
        ユーザ出力関数
        """
        print("You:「 {} 」".format(text), sep=sep, end=end)

    def inputUser(self, exception=None, correct=None, repeat=True):
        """
        ユーザの入力判定
        @param:        
            exception,str or list default=None : 禁止事項
            correct,str or list default=None   : 正しい
            repeat,bool default=True         : 質問を繰り返すか(繰り返す:True，一度のみ:False) 

        <<exception，correctの関係性>>
            Exist，None → 禁止事項のとき以外を返す
            None，None  → すべて返す
            None，Exist → 正しいときのみを返す
            Exist，Exist→ 禁止事項のとき以外かつ正しいときのみを返す
        """
        while repeat:
            userText = input(">>").strip()  # ユーザ入力

            if exception and not correct:  # 禁止事項のとき以外を返す
                if userText in exception:
                    self.printBot("『 {} 』は理解できません!!".format(userText))
                    continue
                else:
                    return userText
            if not exception and not correct:  # すべて返す
                return userText
            if not exception and correct:  # 正しいときのみを返す
                if userText in correct:
                    return userText
                else:
                    self.printBot("『 {} 』は理解できません!!".format(userText))
                    continue
            if exception and correct:  # 禁止事項のとき以外かつ正しいときのみを返す
                if not userText in exception and userText in correct:
                    return userText
                else:
                    self.printBot("『 {} 』は理解できません!!".format(userText))
                    continue
            else:
                return userText

        return userText
