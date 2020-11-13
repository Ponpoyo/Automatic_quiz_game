"""
word2vec temp
"""


from gensim.models import KeyedVectors


class GenerateSimilarWords(object):

    def __init__(self, model_dir, limit=None, stdout_debug=False):
        self.stdout_debug = stdout_debug  # 標準出力デバッグをするかどうか

        self._print("OK")

        # モデルの生成
        self._model = KeyedVectors.load_word2vec_format(
            model_dir, binary=True, limit=limit)
        self._print(self._model)

    def generate(self, word):
        """
        類語の生成
        """
        try:
            results = self._model.most_similar(word)
        except KeyError: #単語が存在しないとき
            return None

        if self.stdout_debug:
            for result in results:
                self._print(result)

        return results

    def _print(self, text):
        """
        標準出力デバッグ
        """
        if self.stdout_debug:
            print("GenerateSimilarWords,INFO: ", text)


def printList(list_,sep="",end="\n"):
    """
    リストのインデクスを1行ずつ表示する関数
    """
    [print(idx,sep=sep,end=end) for idx in list_]


if __name__ == "__main__":
    gsw = GenerateSimilarWords(
        model_dir='..\data\entity_vector\entity_vector.model.bin', limit=400000, stdout_debug=True)

    similarly_list = gsw.generate("カレー") #類似単語リスト生成

    #余分な[]を削除
    similarly_list = [(word.replace("[", "").replace("]", ""), value)
                     for word, value in similarly_list]

    printList(similarly_list)
