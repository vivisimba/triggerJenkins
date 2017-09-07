# -*- coding: utf-8 -*-
'''
Created on 2017年6月21日

@author: Simba
'''
import jenkins
import config.config as CONFIG


def triggerJenkinsWithparameter(jobName, parameterDic):
    server = jenkins.Jenkins(CONFIG.JENKINS_URL, CONFIG.USERID_AND_APITOKEN[0], CONFIG.USERID_AND_APITOKEN[1])
    server.build_job(jobName, parameterDic)


def triggerJenkinsWithoutparameter(jobName):
    server = jenkins.Jenkins(CONFIG.JENKINS_URL, CONFIG.USERID_AND_APITOKEN[0], CONFIG.USERID_AND_APITOKEN[1])
    server.build_job(jobName)
    

# 获得job所需的参数列表
def getParametersOfJob(jobName):
    parameterList = []
    server = jenkins.Jenkins(CONFIG.JENKINS_URL, CONFIG.USERID_AND_APITOKEN[0], CONFIG.USERID_AND_APITOKEN[1])
    if server.get_job_info(jobName)['actions'][1]:
        parameterDefinitionsList = server.get_job_info(jobName)['actions'][1]['parameterDefinitions']
        for i in parameterDefinitionsList:
            parameterList.append(i['name'])
    return parameterList
        

    






