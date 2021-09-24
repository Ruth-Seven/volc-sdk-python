# coding:utf-8


import os
import configparser


HOME = os.environ['HOME']


CONFIG_FILE = os.path.join(HOME, '.volc/config')
CREDENTIAL_FILE = os.path.join(HOME, '.volc/credentials')

DEFAULT_CONFIG_SETION='ml_platform'
DEFAULT_SETTION='default'


class Credentials(object):
    def __init__(self, ak="", sk="", service="", region=""):
        self.ak = ak
        self.sk = sk
        self.service = service
        self.region = region

        self.config_file = ""
        self.credential_file = ""
        
        self.set_config()

    def set_ak(self, ak):
        self.ak = ak

    def set_sk(self, sk):
        self.sk = sk

    def set_config(self, credential_section=DEFAULT_SETTION):
        env_config_file = self._load_env_var("VOLC_CONFIG_FILE")
        env_credential_file = self._load_env_var("VOLC_CREDENTIALS_FILE")

        # Firstly, must set file paths
        self.config_file= self._fifo_valid_value(
            env_config_file,
            CONFIG_FILE,
        )
        self.credential_file= self._fifo_valid_value(
            env_credential_file,
            CREDENTIAL_FILE,
        )
        

        if os.environ.get('HOME', None) is None:
            raise ValueError("Please set $HOME in your env")

        credential_ak, credential_sk = self._load_file_config(self.credential_file, credential_section , 'access_key_id', 'secret_access_key')
        (config_region_custom,) = self._load_file_config(self.config_file, DEFAULT_CONFIG_SETION, 'region')
        (config_region_default,) = self._load_file_config(self.config_file, DEFAULT_SETTION, 'region')

        env_ak = self._load_env_var("VOLC_ACCESS_KEY_ID")
        env_sk = self._load_env_var("VOLC_SECRET_ACCESS_KEY")
        env_region = self._load_env_var("VOLC_REGION")
        
        self.ak = self._fifo_valid_value(
            self.ak,
            env_ak,
            credential_ak,
        )
        self.sk = self._fifo_valid_value(
            self.sk,
            env_sk,
            credential_sk,
        )
        self.region = self._fifo_valid_value(
            self.region,
            env_region,
            config_region_custom,
            config_region_default,
        )


    def _load_env_var(self, env_name):
        return os.environ.get(env_name, None)

    def _load_file_config(self, file, section, *keys):
        config = configparser.ConfigParser()
        
        config.read(file)
        if section not in config.sections():
            print(f"{file} hasn't the {section} section.")
            return (None for _ in keys)

        values = []
        for key in keys:
            values.append(config[section].get(key, None))
        return tuple(values)

    def _fifo_valid_value(self, *values):
        for value in values:
            if value:
                return value
        raise ValueError("Each value is null or empty. Please check the valid parameters")