"""
標準出力クイズゲーム
"""

from QuizGame import Wikipedia
from QuizGame import GenerateSimilarWords
import OperationIO

io = OperationIO.OperationIO()

io.printBot("あそんであげるんだからね!!")

# io.printUser(io.inputUser(exception=["だめ", "きらい"]))
# io.printUser(io.inputUser(exception=["だめ", "きらい"], correct="こんにちは"))
# io.printUser(io.inputUser(correct="よろしく"))

#類語生成器#
generateSimilarWords = GenerateSimilarWords.GenerateSimilarWords(
            model_dir='.\data\entity_vector\entity_vector.model.bin', limit=400000, stdout_debug=True)

while True:
    #答えと問題文の生成#
    quiz_wikipedia = Wikipedia.Wikipedia()
    quiz_wikipedia.randomSearch(standardOutput=False)  # ランダムで記事を取ってくる
    print(quiz_wikipedia.word)  # 単語
    print(quiz_wikipedia.summary)  # その単語の要約

    

    similarly_list = generateSimilarWords.generate(quiz_wikipedia.word) #類似単語リスト生成

    print(similarly_list)
    #類語が見つかったときbreak
    if similarly_list:
        break

    print("INFO: 類語が見つかりませんでした．再検索をします．")

#余分な[]を削除
similarly_list = [(word.replace("[", "").replace("]", ""), value)
                     for word, value in similarly_list]

print(similarly_list)
