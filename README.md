# Docker + FastAPI + PythonによるBATCH,API構築テンプレート

## FastText
### FLOW
0. batch.evaluate_model     -> modelの評価
1. batch.make_data          -> trainデータ作成
2. batch.make_model         -> model作成 & local(docker container)へ保存
3. batch.upload_model       -> GCSへmodelアップロード
4. batch.download_model     -> GCSからmodelダウンロード
5. api.load_model & predict -> 推論api起動

*作成済みモデル使用する際は4から実行

*0,1,3,4実行時は引数に日付を指定（e.g. 2022-10-26）

*0~3は日付を統一（データセットの作成日）

## Docker container
```
/tmp/data/data.txt      -> local data (batch.make_modelで使用)
         /train.txt     -> local train data (batch.evaluate_modelで使用)
         /valid.txt     -> local valid data (batch.evaluate_modelで使用)
    /model/ft_model.bin -> local model (apiで使用)
    /log

/app/ft_api.py          -> api実行用
    /ft_batch.py        -> batch実行用
    /util/*             -> util系
    /model/ftmodel.py   -> fasttext用
    /resources
        /.env               -> 環境変数ファイル
        /credential.json    -> GCPへの認証ファイル
```

*/tmp/data, /tmp/model配下は使用後に都度削除する -> ft_xx_clear_tmp.sh

## resources
resources配下をdockerの/app/resources配下にマウント

以下gitignoreのため必要に応じて手動で配置
* .env
* credential.json

## 実行までの手順
resources配下に必要なファイルが配備されている前提
1. `git clone git@github.com:bass-bass/fastapi_starter.git`
2. `cd fastapi_starter`
3. (`systemctl start docker`)
4. `docker-compose up -d --build`
5. (`sh sh/batch/ft_04_download_model.sh 2022-10-26`)
6. `sh sh/api/ft_api_start.sh`
