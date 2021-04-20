import os
import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(csv_file_path, word):
    # 検索対象取得
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, mode="w") as f:
            new_df = pd.DataFrame(index=[], columns=["name"])
            new_df.to_csv(csv_file_path, encoding="utf_8-sig")

    df=pd.read_csv(csv_file_path)
    source=list(df["name"])
    
    message_list = []

    # 検索
    if word in source:
        message_list.append(f"『{word}』はいます")
    else:
        message_list.append(f"『{word}』はいません")
        message_list.append(f"『{word}』を追加します")
        source.append(word)
    
    # デバッグ用メッセージ出力
    # for message in message_list:
    #     print(message)

    # CSV書き込み
    df=pd.DataFrame(source, columns=["name"])
    df.to_csv(csv_file_path, encoding="utf_8-sig")

    return message_list
