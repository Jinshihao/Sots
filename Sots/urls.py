"""Sots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import administrators.adminuser.adminuser as ad
import administrators.models as admo
import administrators.user.user as us
import administrators.job.job as job
import administrators.company.company as com
from analysis.personalCenter import login, postuserName, \
    registered, personalEdit, postPersonalInformation, personalCity
from analysis.views import access, index, job_list, persistence, get_searchKeyword, \
    get_recommendInformation, get_hotJob, get_personRecommend, \
    get_allrequirementsDiagrams, test_url, get_carouselData, get_user_data, get_user_feature, \
    get_job_need, get_job_detail, get_salary_analysis, get_comp_scale, get_comp_statu, jianli, get_useragenum, \
    get_userfavjob, get_userfavcity, test, get_usersex, get_postportrait, get_factorjobnum, get_topsalaryjobnum, \
    get_avgsalaryjobnum, get_welfaresalaryfactor, get_factorsalary, get_industrycitycompnum, get_corporateportrait, \
    get_compkind, get_citycompscale, get_difcompscalejobnum, get_difcompscaleedu, get_difcompscaleexper, \
    get_cityindustrycompnum
import administrators.website.website as web
import administrators.test.test as te
import administrators.carousel.carousel as carousel
from administrators.crawler import crawler_admin

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 后台
    url(r'admin/$', ad.main),
    url(r'admin/login$', ad.land, name='login'),  # 管理员登陆界面，
    url(r'admin/checks$', ad.checks, name='checks'),  # 后台校验用户名和密码
    url(r'admin/main$', ad.show_main, name='main'),  # 主界面
    url(r'admin/welcome$', ad.welcome, name='welcome'),  # 欢迎分界面
    url(r'admin/repassword$', ad.repassword, name='repassword'),  # 修改管理员密码
    url(r'admin/adminUpdate$', ad.update, name='adminUpdate'),  # 完成修改
    url(r'admin/login$', ad.exit, name='exit'),

    # 用户
    url(r'^admin/userShow$', us.show, name='userShow'),  # 用户展示
    url(r'admin/userShowNext', us.showNext, name='userShowNext'),
    url(r'admin/userDel*', us.delete, name='userDel'),  # 用户删除
    url(r'admin/userAdd', us.add, name='userAdd'),  # 跳转到添加用户界面
    url(r'admin/userSave', us.save, name='userSave'),  # 用户存储
    url(r'admin/userEdit', us.edit, name='userEdit'),  # 跳转到编辑用户界面
    url(r'admin/userUpdate', us.update, name='userUpdate'),  # 用户更新

    # 岗位
    url(r'admin/jobShow$', job.show, name='jobShow'),  # 岗位展示
    url(r'admin/jobShowNext', job.showNext, name='jobShowNext'),
    url(r'admin/jobDel', job.delete, name='jobDel'),  # 岗位删除
    url(r'admin/jobAdd', job.add, name='jobAdd'),  # 跳转到添加岗位界面
    url(r'admin/jobSave', job.save, name='jobSave'),  # 岗位存储
    url(r'admin/jobEdit', job.edit, name='jobEdit'),  # 跳转到编辑岗位界面
    url(r'admin/jobUpdate', job.update, name='jobUpdate'),  # 岗位更新

    # 网站
    url(r'admin/websiteShow', web.show, name='websiteShow'),  # 网站展示
    url(r'admin/websiteNext', web.showNext, name='webShowNext'),
    url(r'admin/websiteDel', web.delete, name='websiteDel'),  # 网站删除
    url(r'admin/websiteAdd', web.add, name='websiteAdd'),  # 跳转到添加网站界面
    url(r'admin/websiteSave', web.save, name='websiteSave'),  # 网站存储
    url(r'admin/websiteEdit', web.edit, name='websiteEdit'),  # 跳转到编辑岗位界面
    url(r'admin/websiteUpdate', web.update, name='websiteUpdate'),  # 岗位更新

    # 公司
    url(r'admin/companyShow$', com.show, name='companyShow'),  # 公司展示
    url(r'admin/companyShowNext', com.showNext, name='companyShowNext'),
    url(r'admin/companyDel', com.delete, name='companyDel'),  # 公司删除
    url(r'admin/companyEdit', com.edit, name='companyEdit'),

    # 轮播图片
    url(r'admin/carouselShow$', carousel.show, name='carouselShow'),  # 轮播展示
    url(r'admin/carouselShowNext', carousel.showNext, name='carouselShowNext'),
    url(r'admin/carouselDel', carousel.delete, name='carouselDel'),
    url(r'admin/carouselAdd', carousel.add, name='carouselAdd'),
    url(r'admin/carouselSave', carousel.save, name='carouselSave'),
    url(r'admin/carouselEdit', carousel.edit, name='carouselEdit'),
    url(r'admin/carouselUpdate', carousel.update, name='carouselUpdate'), # path('admin/', admin.site.urls),

    # 后台
    url(r'admin/$', ad.main),
    url(r'admin/login$', ad.land, name='login'),  # 管理员登陆界面，
    url(r'admin/checks$', ad.checks, name='checks'),# 后台校验用户名和密码
    url(r'admin/main$', ad.show_main, name='main'),# 主界面
    url(r'admin/welcome$', ad.welcome, name='welcome'),#  欢迎分界面
    url(r'admin/repassword$', ad.repassword, name='repassword'),# 修改管理员密码
    url(r'admin/adminUpdate$', ad.update, name='adminUpdate'),# 完成修改
    url(r'admin/login$', ad.exit, name='exit'),



    # 用户
    url(r'^admin/userShow$', us.show, name='userShow'),# 用户展示
    url(r'admin/userDel*', us.delete, name='userDel'),# 用户删除
    url(r'admin/userAdd', us.add, name='userAdd'),# 跳转到添加用户界面
    url(r'admin/userSave', us.save, name='userSave'),# 用户存储
    url(r'admin/userEdit', us.edit, name='userEdit'),# 跳转到编辑用户界面
    url(r'admin/userUpdate', us.update, name='userUpdate'),# 用户更新

    # 岗位
    url(r'admin/jobShow$', job.show, name='jobShow'),# 岗位展示
    url(r'admin/jobShowNext', job.showNext, name='jobShowNext'),
    url(r'admin/jobDel', job.delete, name='jobDel'),# 岗位删除
    url(r'admin/jobAdd', job.add, name='jobAdd'),# 跳转到添加岗位界面
    url(r'admin/jobSave', job.save, name='jobSave'),# 岗位存储
    url(r'admin/jobEdit', job.edit, name='jobEdit'),# 跳转到编辑岗位界面
    url(r'admin/jobUpdate', job.update, name='jobUpdate'),# 岗位更新

    # 网站
    url(r'admin/websiteShow', web.show, name='websiteShow'),  # 网站展示
    url(r'admin/websiteDel', web.delete, name='websiteDel'),  # 网站删除
    url(r'admin/websiteAdd', web.add, name='websiteAdd'), # 跳转到添加网站界面
    url(r'admin/websiteSave', web.save, name='websiteSave'),  # 网站存储
    url(r'admin/websiteEdit', web.edit, name='websiteEdit'),# 跳转到编辑岗位界面
    url(r'admin/websiteUpdate', web.update, name='websiteUpdate'),# 岗位更新

    # 公司
    url(r'admin/companyShow$', com.show, name='companyShow'),  # 公司展示
    url(r'admin/companyShowNext', com.showNext,name='companyShowNext'),
    url(r'admin/companyDel', com.delete, name='companyDel'),  # 公司删除
    url(r'admin/companyEdit', com.edit, name='companyEdit'),




    url(r'^$', index, name='index'),        #前台首页
    url(r'sots/searchResult', job_list),    #搜索匹配结果
    url(r'sots/searchKeyword', get_searchKeyword),  #搜索关键字获取
    url(r'sots/recommendInformation', get_recommendInformation),    #推荐职位
    url(r'sots/hotJob', get_hotJob),            #热门职位
    url(r'sots/personRecommend', get_personRecommend),  #猜你喜欢
    url(r'sots/glyphicon', get_allrequirementsDiagrams),
    url(r'sots/carouselData', get_carouselData),# 前台轮播
    url(r'sots/user/usereduexper', get_user_data),
    url(r'sots/user/userfavjob', get_userfavjob),
    url(r'sots/user/usersex', get_usersex),
    url(r'sots/user/userfavcity', get_userfavcity),
    url(r'sots/user/userage', get_useragenum),
    url(r'sots/visualanalysis/userfeature', get_user_feature),
    url(r'sots/visualanalysis/jobneed', get_job_need),
    url(r'sots/visualanalysis/jobdetail', get_job_detail),
    url(r'sots/visualanalysis/salaryanalysis', get_salary_analysis),
    url(r'sots/visualanalysis/compscale', get_comp_scale),
    url(r'sots/visualanalysis/compstatu', get_comp_statu),
    url(r'sots/logIn', login),# 登录校验
    url(r'sots/postuserName', postuserName),# 注册用户名的异步校验
    url(r'sots/registered', registered),# 注册校验
    url(r'sots/personalEdit', personalEdit),# 前台获取性别、城市、学历、工作年限的列表信息
    url(r'sots/personalCity', personalCity),# 根据省份查询对应的市集合
    url(r'sots/postPersonalInformation', postPersonalInformation),# 前台用户个人信息提交
    url(r'sots/post/postportrait', get_postportrait),
    url(r'sots/post/factorjobnum', get_factorjobnum),
    url(r'sots/post/topsalaryjobnum', get_topsalaryjobnum),
    url(r'sots/post/avgsalaryjobnum', get_avgsalaryjobnum),
    url(r'sots/post/welfaresalaryfactor', get_welfaresalaryfactor),
    url(r'sots/post/factorsalary', get_factorsalary),
    url(r'sots/post/industrycitycompnum', get_industrycitycompnum),
    url(r'sots/corporate/corporateportrait', get_corporateportrait),
    url(r'sots/corporate/compkind', get_compkind),
    url(r'sots/corporate/citycompscale', get_citycompscale),
    url(r'sots/corporate/difcompscalejobnum', get_difcompscalejobnum),
    url(r'sots/corporate/difcompscaleedu', get_difcompscaleedu),
    url(r'sots/corporate/difcompscaleexper', get_difcompscaleexper),
    url(r'sots/corporate/cityindustrycompnum', get_cityindustrycompnum),


    # 测试0
    url(r'access', access, name='access'),
    url(r'persistence', persistence, name='persistence'),
    url(r'operation', test_url),
    url(r'postCity', te.postCity),
    url(r'city', te.personalCity, name='city'),
    url(r'test', test),
    # 随机生成求职者的测试数据，存入数据库


    # url(r'admin/img', te.imgs, name='img'),# 图片测试
    # url(r'admin/testShow', te.img, name='testShow'),# 图片测试
    url(r'admin/testShow', te.show, name='testShow'),  # 展示页面
    url(r'admin/testRandom', te.rando, name='testRandom'),  # 进入后端去生成
    url(r'admin/infoSave', te.save, name='infoSave'),  # 存储生成

    # 爬虫管理页面
    url(r'admin/crawler/start', crawler_admin.start_spider, name='start_spider'),
    url(r'admin/crawler/end', crawler_admin.end_job, name='end_job'),
    url(r'admin/crawler/list', crawler_admin.list_job, name='list_crawler_job'),
    url(r'^admin/crawler$', crawler_admin.crawler_index, name='crawler_admin'),
]
