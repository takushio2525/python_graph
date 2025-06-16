import numpy as np
from graph_template_class import GraphWindow, Graph
import os
import pandas as pd

# プログラムのあるディレクトリ
scriptDir = os.path.dirname(os.path.abspath(__file__))

# CSVデータの読み込み
data = pd.read_csv(os.path.join(scriptDir, "data.csv"))

# 全体のサイズとレイアウトを指定
graphWindow = GraphWindow(figsize=(15, 5), layout="horizontal")  # 横並びのレイアウト

# グラフの定義
# グラフ設定データ
graph_configs = [
    {
        "x": data['学習時間(週)'],
        "y": data['国語の点数'],
        "xlabel": "学習時間(週)",
        "ylabel": "国語の点数",
        "title": "学習時間と国語の点数の散布図"
    },
    {
        "x": data['学習時間(週)'],
        "y": data['数学の点数'],
        "xlabel": "学習時間(週)",
        "ylabel": "数学の点数",
        "title": "学習時間と数学の点数の散布図"
    },
    {
        "x": data['学習時間(週)'],
        "y": data['英語の点数'],
        "xlabel": "学習時間(週)",
        "ylabel": "英語の点数",
        "title": "学習時間と英語の点数の散布図"
    }
]

# グラフを作成してウィンドウに追加
for config in graph_configs:
    graph = Graph()
    graph.add_function(config["x"], config["y"], plot_type="scatter")
    graph.set_labels(xlabel=config["xlabel"],
                     ylabel=config["ylabel"], title=config["title"])
    graph.set_range(xlim=(0, 16), ylim=(0, 100))
    graphWindow.add_graph(graph)

# グラフの表示
graphWindow.show()
