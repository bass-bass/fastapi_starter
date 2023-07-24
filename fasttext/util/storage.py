from google.cloud import storage

class GCSWrapper:
    def __init__(self, credential_path, bucket_name):
        """GCSのラッパークラス
        Arguments:
            credential_path {str} -- GoogleCloudPlatform Credential json path
            bucket_name {str} -- GoogleCloudStorage Bucket Name
        """
        self._credential_path = credential_path
        self._bucket_name = bucket_name
        self._client = storage.Client.from_service_account_json(self._credential_path)
        self._bucket = self._client.bucket(self._bucket_name)

    def upload_file(self, local_path, gcs_path):
        """GCSにローカルファイルをアップロード

        Arguments:
            local_path {str} -- local file path
            gcs_path {str} -- gcs file path
        """
        blob = self._bucket.blob(gcs_path)
        blob.upload_from_filename(local_path)

    def download_file(self, local_path, gcs_path):
        """GCSのファイルをファイルとしてダウンロード

        Arguments:
            local_path {str} -- local file path
            gcs_path {str} -- gcs file path
        """
        blob = self._bucket.blob(gcs_path)
        blob.download_to_filename(local_path)

    def get_content_as_string(self, gcs_path):
        """GCSのファイルをbyteとして取得

        Arguments:
            gcs_path {str} -- gcs file path
        """
        blob = self._bucket.blob(gcs_path)
        return blob.download_as_string()
