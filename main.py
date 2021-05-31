import tkinter as tk

class Application(tk.Frame):
    # scaleに関する情報を格納する関数
    scale = None

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、scale Widgetを作成する。
        # from_ : 入力できる数字の下限を設定する。初期値とされる。
        # orient : scale Widgetを水平方向に変更する。
        self.scale = tk.Scale(frame, from_=10, orient=tk.HORIZONTAL)

        # frame Widget(Frame)を親要素とした場合に、scale Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.scale.pack()

    # hello worldを出力する関数
    def helloWorld(self, value):
        print('hello world')

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
