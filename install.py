# installer for Meteoclimatic
# José A. García-Tenorio
# Basado en el código de Matthew Wall
# 
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return MeteoclimaticInstaller()

class MeteoclimaticInstaller(ExtensionInstaller):
    def __init__(self):
        super(MeteoclimaticInstaller, self).__init__(
            version="0.7",
            name='meteoclimatic',
            description='Upload weather data to Meteoclimatic.',
            author="José A. García-Tenorio",
            restful_services='user.meteoclimatic.Meteoclimatic',
            config={
                'StdRESTful': {
                    'Meteoclimatic': {
                        'api_key': 'replace_me'}}},
            files=[('bin/user', ['bin/user/meteoclimatic.py'])]
            )
