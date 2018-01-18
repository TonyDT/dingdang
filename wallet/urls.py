
from django.urls import path,include

from  wallet import views


urlpatterns = [
    #首页四URL企业文化  产品介绍 贷款保障 门店地址
    path('cpjs/',views.cpjs),
    path('dkbz/',views.dkbz),
    path('mddz/',views.mddz),
    path('qywh/',views.qywh),
    #首页下部文章
    path('homeEasy/',views.articleOne),
    path('homeLoan/',views.articleTwo),

    #首页json数据
    path('home/',views.jsonHome),

]
