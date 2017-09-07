# -*- coding: utf-8 -*-
'''
Created on 2017年2月28日

@author: Simba
'''
import os


# 脚本存放根目录
ROOT_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# 脚本日志存放根目录
LOG_HOME = ROOT_HOME + os.sep + 'logs/'


# 访问jenkins的user_id和api_token
USERID_AND_APITOKEN = ['simba',
                       '8e1df7aaff88bb16b61376a779ac5e3f'
                       ]


# jenkins地址
JENKINS_URL = 'http://10.0.250.72:8080/jenkins/'


# jenkins中的jobname与所需传入参数的对应关系
# JOBNAME_PARAM_DICT = {'testtest': ['BRANCH',
#                                   'mailto'
#                                   ],
#                      }


# 邮件标题关键字符串与jenkins的jobname的关系: key：邮件标题中的关键字字符串；value: jobname
JOBNAME_TRIGGERSTR = {'testtest': 'testtest',
                      'startimes-starecms': 'StarECMS',
                      'starmboss-app': 'starmboss-app',
                      'starmboss-server': 'starmboss-server',
                      'OTT_PROVISION': 'OTT_PROVISION',
                      'startimes-box': 'star-box',
                      'star-selfservice-web': 'star-selfservice-web',
                      'starfsa-middle-layer': 'starfsa_middle_layer',
                      'starfsa-app': 'starfsa_app',
                      'StarAPP-Android': 'StarAPP-Android_Build',
                      'StarAPP-IOS': 'StarAPP-IOS_Build_Master',
                      'starbi-starafdw': 'starbi-starafdw',
                      'starda-app': 'StarDA-App',
                      'starda-ip-dispatch': 'StarDA-ip-dispatch',
                      'starda-web': 'StarDA-Web',
                      'stardss-service': 'stardss',
                      'stardss-app': 'stardss-app',
                      'startimes-stardw': 'stardw',
                      'startimes-erp': 'starerp',
                      'startimes-mppw': 'STARMPPW',
                      'starcdn': 'starott-cdn',
                      'startimes-et': 'starott-et',
                      'startimes-ott-gradle': 'starott-gradle',
                      'startimes-os': 'starott-os',
                      'starott-platform': 'starott-platform',
                      'startimes-ott-ott': 'starott-starott',
                      'startimes-uba': 'uba',
                      'uba-etl-startimes': 'uba-etl',
                      'ottapplication': 'ottapplication'
                      }


# 异常字典
EXCEPTION_DIC = {'no_new_mail': 'There is no new email need to deal with.',
                 'no_match_keystr': ('There is no keyStr found in keyStrList or the keyStr was found more than once '
                                     'in the keyStrList.  Please check the subject of email and contact the administrator.'
                                     ),
                 'repeated parameter': 'Please make sure that the parameter is unique in the email.',
#                 'no parameter': 'There is no parameter in the email, but the job wanted to be triggered need some parameters.',
#                 'parameter count wrong': 'The number of parameter the email given, is not equal to the number of the job needs.',
                 'parameter not enough': 'Parameters in the email are not enough.\n'
                 }

