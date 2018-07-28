from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def timetable(request):
    content = {
        "appname": "Timetable",
        "version": "200",
        "title": "新版本(V2.0.0)",
        "force": "100",
        "updateurl": "https://www.strivexj.com/timetable/tt.apk",
        "upgradeinfo": "新增课程自定义（字体大小、透明度、格子高度、是否显示周末、上课时间、颜色等）\n相机支持预览图片\n修复侧滑菜单、相机、课程滑动卡顿\n修复课程自动切换周数\n修复浏览器闪退等BUG"
    }
    return JsonResponse(data=content, status="200")
