import time
from math import nan

import pandas as pd

from analysis.tools import csv_conf
from analysis.tools.csv_conf import datapath, didatapath
from analysis.models import Job, DigitizedJob, Company


def batchinsert_company(compset):
    print('batch insert comp  size :', len(compset))
    list_to_insert = list()
    values = compset.values()
    for val in values:
        list_to_insert.append(val)
    Company.objects.bulk_create(list_to_insert)
    compset.clear()


def csv_duplication():

    pass


# TODO 去重方式需要考虑
def persistence_company(path: str):
    print('insert comp start')
    if path:
        start_time = time.time()
        start_index = Job.objects.count()

        oldcompanyidset = set()
        newcompanyidset = set()
        oldcomps = Company.objects.values_list('companyId')
        for comp in oldcomps:
            oldcompanyidset.add(comp[0])
        print(oldcompanyidset)
        df = pd.read_csv(path)
        print(df.tail())
        df = df[csv_conf.data_columnsname]
        df = df[start_index:]
        # 以防万一
        df = df.drop_duplicates('jobId')
    else:
        return
    rows = df.iterrows()
    compset = {}
    for index, row in rows:
        company = Company()
        company.companyId = row[14]
        if company.companyId in oldcompanyidset or company.companyId in newcompanyidset:
            continue
        company.compName = row[15]
        company.compSize = row[16]
        company.compIndustry = row[17]
        company.companyLabels = row[18]
        company.compLink = row[19]
        company.compIntroduce = row[20]
        company.contactInfo = row[21]
        tmp = lambda x: 0 if x != nan else x
        company.longitude = tmp(row[22])
        company.latitude = tmp(row[23])
        company.businessZones = row[24]
        company.compHome = row[25]
        company.companyLogo = row[26]
        company.financeStage = row[27]
        compset[company.companyId] = company
        newcompanyidset.add(company.companyId)
        if len(compset) == 1000:
            batchinsert_company(compset)


    batchinsert_company(compset)
    end_time = time.time()
    print('insert comp end costing:', end_time - start_time)


def persistence_job(path: str):
    start_time = time.time()

    print('start insert job')
    start_index = Job.objects.count()
    if path:
        df = pd.read_csv(path)
        df = df[csv_conf.data_columnsname]
        start_index+=1
        df = df[start_index:]
        # 以防万一
        df = df.drop_duplicates('jobId')
    else:
        return
    compidset = set()
    compid = df['companyId']
    for i in compid:
        compidset.add(i)

    companys = Company.objects.filter(companyId__in=compidset)
    compidtocomp = {}
    for i in companys:
        compidtocomp[i.companyId] = i

    rows = df.iterrows()
    print('-----------query over-----------')
    list_to_insert = list()
    cont = 0
    for index, row in rows:
        companyId = row[14]
        # TODO 修改外键获取方式
        job = Job()
        # try:
        job.jobId = row[0]
        job.company = compidtocomp[companyId]
        # except TypeError as e:
        #     # print('type error ', e)
        #     continue
        job.JobName = row[1]
        job.JobPlace = row[2]
        job.JobSalary = row[3]
        job.JobAdvantage = row[4]
        job.releaseTime = row[5]
        job.jobNeed = row[6]
        job.educationRequire = row[7]
        job.experienceRequire = row[8]
        job.skillRequire = row[9]
        job.jobLink = row[10]
        job.jobInfo = row[11]
        job.jobNature = row[12]
        job.jobLabels = row[13]
        job.keyword = row[28]
        list_to_insert.append(job)
        cont += 1
        if cont == 1000:
            Job.objects.bulk_create(list_to_insert)
            print('batch insert job size ', len(list_to_insert))
            list_to_insert.clear()
            cont = 0
    Job.objects.bulk_create(list_to_insert)
    print('batch insert job size:', len(list_to_insert))
    endtime = time.time()
    print('耗时：', (endtime - start_time))


def persistence_djob(path: str):
    start_time = time.time()

    print('start insert djob')
    if path:
        start_index = DigitizedJob.objects.count()
        start_index+=1
        df = pd.read_csv(path)
        print(df.tail())

        df = df[csv_conf.digital_columnsname]
        df = df[start_index:]
        # 以防万一
        df = df.drop_duplicates('jobId')
        jobids = df['jobId']
        jobidset = set()
        for id in jobids:
            jobidset.add(id)

        jobs = Job.objects.filter(jobId__in=jobidset)
        jobidtojob = {}
        for i in jobs:
            jobidtojob[i.jobId] = i
    else:
        return
    rows = df.iterrows()
    print('-----------query over-----------')

    list_to_insert = list()

    count = 0
    for index, row in rows:
        jobId = row[0]
        # TODO 修改外键获取方式
        djob = DigitizedJob()
        djob.Job = jobidtojob[jobId]
        djob.compSize = row[1]
        djob.skill = row[2]
        djob.experience = row[3]
        djob.education = row[4]
        djob.salary = row[5]
        djob.keyword = row[6]
        list_to_insert.append(djob)
        count += 1
        if count == 1000:
            DigitizedJob.objects.bulk_create(list_to_insert)
            print('batch insert djob size ', len(list_to_insert))
            list_to_insert.clear()
            count = 0
    DigitizedJob.objects.bulk_create(list_to_insert)
    print('batch insert djob size ', len(list_to_insert))
    endtime = time.time()

    print('耗时：', (endtime - start_time))


# TODO 添加各种图表需要的数据
def persistence_all():
    try:
        csv_duplication()
        persistence_company(datapath)
        persistence_job(datapath)
        persistence_djob(didatapath)
    except TimeoutError as e:
        print('database error occurred ', e)


if __name__ == '__main__':
    pass
    # write_job_to_mysql('datas/data.csv')
    # write_diJob_to_mysql()
