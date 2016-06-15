from pagrant.setting import sp, param, conf
from pagrant.system import cd

# Parameters need to be added first before being used.
param.update({
    'ngx_virtual_host': 'magento2-ce.local',
    'php_host': '127.0.0.1',
    'php_port': '9000',
    'app_mage_code': 'developer',
    'app_mage_root': '/srv/website'
})

conf.update({
    'build': {
        'env_vars': {
            'BUILD_SCRIPT_DIR': '/vagrant',
            'BUILD_CONF_DIR': '/vagrant/conf'
        },
        'env_vars_file': '/etc/profile.d/pagrant.sh',
        'nginx': {
            'conf': {
                'mappings': {
                    cd('conf/nginx'): '/etc/nginx'
                },
                'replacements': {
                    'ngx_virtual_host': sp('ngx_virtual_host'),
                    'php_host': sp('php_host'),
                    'php_port': sp('php_port'),
                    'app_mage_code': sp('app_mage_code'),
                    'app_mage_root': sp('app_mage_root')
                },
                'pattern': '{{*}}'
            }
        },
        'php56': {
            'app': {
                'packages': ['php5', 'php5-fpm', 'php5-mhash', 'php5-mcrypt', 'php5-curl', 'php5-cli', 'php5-mysql', 'php5-gd', 'php5-intl', 'php5-xsl']
            },
            'conf': {
                'mappings': {
                    cd('conf/php56'): '/etc/php5'
                },
                'replacements': {
                    'php_host': sp('php_host'),
                    'php_port': sp('php_port')
                },
            }
        },
        'mysql56': {
            'app': {
                # 'user': 'admin',
                'password': 'balance08'
            },
            'conf': {
                'mappings': {
                    cd('conf/mysql56/conf.d'): '/etc/mysql/conf.d'
                }
            }
        },
        'ssmtp': {
            'conf': {
                'mappings': {
                    cd('conf/ssmtp'): '/etc/ssmtp'
                }
            }
        }
    }
})