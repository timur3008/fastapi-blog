# файл для настройки api
from environs import Env
from dataclasses import dataclass, field


@dataclass
class RunConfig:
    api_host: str
    api_port: str

    @staticmethod
    def from_env(env: Env) -> 'RunConfig':
        return RunConfig(api_host=env.str('API_HOST'), api_port=env.int('API_PORT'))
    

@dataclass
class ApiV1Prefix:
    prefix: str = '/v1'
    categories: str = '/categories'
    products: str = '/products'


@dataclass
class ApiPrefix:
    prefix: str = '/api'
    v1: ApiV1Prefix = field(default_factory=ApiV1Prefix)