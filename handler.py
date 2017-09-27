from warrant import Cognito


def auth(event, context):
    # event内から必要なパラメータ取得
    cognito_pool_id = event['cognito_pool_id']
    cognito_client_id = event['cognito_client_id']
    username = event['username']
    password = event['password']

    # Cognitoアクセス用オブジェクトの作成
    cognito = Cognito(
        cognito_pool_id,
        cognito_client_id,
        user_pool_region='ap-northeast-1',
        username=username)

    # 認証処理の実行
    cognito.authenticate(password=password)

    return cognito.id_token
