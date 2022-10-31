import config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logzioFormat': {
            'format': '{"additional_field": "value"}',
            'validate': False
        }
    },
    'handlers': {
        'logzio': {
            'class': 'logzio.handler.LogzioHandler',
            'level': 'INFO',
            'formatter': 'logzioFormat',
            'token': f'{config.LOGZIO_TOKEN}',
            'logzio_type': 'python-handler',
            'logs_drain_timeout': 5,
            'url': f'https://{config.LOGZIO_URL}:8071',
            'retries_no': 4,
            'retry_timeout': 2,
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['logzio'],
            'propagate': True
        }
    }
}