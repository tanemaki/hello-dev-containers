# hello-dev-containers

このレポジトリの目的は、Python開発環境をVS Code Remote Containersを使って構築する方法を紹介することです。
d-primeが適当に作ったものなので、あまり期待しないでくださいませ〜。

## 売りポイント

- VS Code Remote Containers（開発コンテナ）を使っているので、ローカル環境にPythonをインストールする必要がありません。VS CodeとRemote Containers拡張機能さえあれば、どこでも同じ環境で開発ができます。
- 基本的に.devcontainerディレクトリ以下の設定ファイルを変更するだけで、開発環境をカスタマイズできます。
- スクリプトはtasks.pyに書き、関数はhello_dev_containers以下にライブラリとしてまとめられます。これにより、スクリプトとライブラリが分離され、コードの再利用性が向上します。
- コード整形やインポートのソーティングなどはRuffを使って自動化しています。コードを保存する際に自動的に整形されます。
- 開発環境の違いによる問題を回避できるので、仲間とのコード共有や別環境での再現実験がしやすくなります。

## 使用ツール

- プロジェクト作成＆Pythonパッケージマネージャー [uv](https://docs.astral.sh/uv/)
- タスクランナー [Invoke](http://www.pyinvoke.org/)
- コード整形など [Ruff](https://docs.astral.sh/ruff/)

## はじめての使い方

1. このリポジトリをクローンします。
2. VS Codeを開きます。
3. Remote-Containers拡張機能をインストールします。
4. 左下の「><」をクリックして、コマンドパレットを開きます。
5. `Remote-Containers: Reopen in Container`を選択します。
6. コンテナの起動と同時に新しいウィンドウが開き、画面左下に「開発コンテナ: python @ desktop-linux」と表示されているのを確認します。
7. ターミナルを開いて、`(workspace) root@9dd39b93510f:/workspace#`のように表示されていることを確認します。
8. `python --version`を実行してPythonのバージョンが`Python 3.12.8`と表示されることを確認します。
9. `invoke say-hello-using-private-library`を実行して、`Hello from hello-dev-containers!`と表示されれば成功です。やったね！

## その他の使い方

### Pythonパッケージのインストール

```bash
uv add <package-name>
```

### Pythonパッケージのアンインストール

```bash
uv remove <package-name>
```

### Invokeタスクの列挙

```bash
invoke --list
```

### Invokeタスクの追加

`tasks.py`にタスクを追加します。

## このリポジトリをどのように作成したか

1. `hello-dev-containers`という名前でプロジェクトを作成

    ```bash
    uv init hello-dev-containers --lib # 今回はライブラリ形式（src layout）を採用
    # uv init hello-dev-containers # アプリ形式（flat layout）にしたければこちら

    # プロジェクトディレクトリの中に移動
    cd hello-dev-containers
    ```

2. `.devcontainer`の中身を他のリポジトリからコピーしてきて使いやすいように変更

3. `tasks.py`を作成してDONE!
