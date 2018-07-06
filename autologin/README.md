

1.NOXをダウンロードする
    https://jp.bignox.com/

2.applist.jsonを作って起動したいアプリ名を書く。
	Nox\binディレクトリまで移動して以下のコマンドを実行
	adb shell pm list packages >C:\app.txt
    C直下に落ちるapp.txtを見てアプリ名を記述

{   
    "AppList":
    [
        "APP01",
        "APP02",
        "APP03"
        ##"jp.co.会社名..."みたいな感じのはず
    ]
}



※躓いたところ
    アプリの起動だけは
    subprocess.Run()ではなく
    subprocess.Popen(app_name, shell=True)
    を使わないとずっと待機中になってスクリプトが進まなかった。
    popenはrunとは違い実行待ちをせずコマンドを実行するスクリプト
    