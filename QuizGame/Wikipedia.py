"""
Wikipedia操作クラス
"""

import wikipedia
import random


class Wikipedia(object):
    def __init__(self, language="ja"):
        """
        set language
        @param language; Default argument is Japanese.
        If you get English articles, "language" argument sets "en".
        """
        wikipedia.set_lang("ja")

    def searchFrom2(self, word, standardOutput=False):
        """wikipedia サーチ 2
        単語リストのシャッフルを行う
        @param word,str 検索したいワード
        @param standerdOutput;default=False 結果の標準出力表示(デバッグ)
        """
        self.words = wikipedia.search(
            word)  # wikipediaから検索ワードを取得
        self._shuffleWords()  # シャッフル
        self.word = self.words[0]  # 1番最初を取得
        self.url = wikipedia.page(self.word).url  # URL取得
        self.summary = wikipedia.summary(
            self.word)  # 要約を取得

        if standardOutput:
            # 表示
            print("候補:", self.words)
            print("要約:", self.summary)
            print("Word:", self.word)
            print("URL:", self.url)

    def searchFrom(self, word, standardOutput=False):
        """wikipedia サーチ
        @param word,str 検索したいワード
        @param standerdOutput;default=False 結果の標準出力表示(デバッグ)
        """
        self.words = wikipedia.search(
            word)  # wikipediaから検索ワードを取得
        self.word = self.words[0]  # 1番最初を取得
        self.url = wikipedia.page(self.word).url  # URL取得
        self.summary = wikipedia.summary(
            self.word)  # 要約を取得

        if standardOutput:
            # 表示
            print("候補:", self.words)
            print("要約:", self.summary)
            print("Word:", self.word)
            print("URL:", self.url)

    def randomSearch(self, standardOutput=False):
        """wikipedia ランダムサーチ
        @param 
            standerdOutput;default=False 結果の標準出力表示(デバッグ)
        """
        self.words = wikipedia.search(
            wikipedia.random(1))  # wikipediaから検索ワードを取得
        self.word = self.words[0]  # 1番最初を取得
        self.url = wikipedia.page(self.word).url  # URL取得
        self.summary = wikipedia.summary(
            self.word)  # 要約を取得

        if standardOutput:
            # 表示
            print("候補:", self.words)
            print("要約:", self.summary)
            print("Word:", self.word)
            print("URL:", self.url)

    def _shuffleWords(self):
        """
        wordsリストをシャッフルする
        """
        self.words = random.sample(self.words, len(self.words))


if __name__ == "__main__":
    Wikipedia().searchFrom("日本", standardOutput=True)
