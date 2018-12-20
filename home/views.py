import os
from json import dumps

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from home.models import LinkGameRanking
from home.serializers import LinkGameRankingSerializer
from timetable.serializers import PostSerializer


def index(request):
    return render(request, 'home/index.html')


@csrf_exempt
def list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return JsonResponse({"code": 400}, status=400)
        # snippets = CoursesHtml.objects.all()
        # serializer = PostSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = {}
        data['school'] = request.POST['school']
        data['type'] = request.POST['type']
        data['html'] = request.POST['html']
        data['url'] = request.POST['url']
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"code": 201}, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def linkGameRanking(request):
    max = 9
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        rankings = LinkGameRanking.objects.all()
        serializer = LinkGameRankingSerializer(rankings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        data = dict()
        data['username'] = request.POST['username']
        data['type'] = request.POST['type']
        data['record'] = request.POST['record']
        data['date'] = request.POST['date']

        rankings = LinkGameRanking.objects.filter(type=data['type'])
        if len(rankings) > max and int(data['record']) >= rankings[len(rankings) - 1].record:
            return JsonResponse({"code": 201}, status=201)

        if len(rankings) > max:
            rankings[len(rankings) - 1].delete()

        try:
            aRecord = LinkGameRanking.objects.get(username=data['username'], type=data['type'])
        except:
            aRecord = None

        serializer = LinkGameRankingSerializer(data=data)
        if serializer.is_valid():
            if aRecord is not None:
                if aRecord.record > int(data['record']):
                    aRecord.delete()
                else:
                    return JsonResponse({"code": 201}, status=201)
            serializer.save()
            return JsonResponse({"code": 201}, status=201)
        return JsonResponse(serializer.errors, status=400)


def timetable(request):
    content = {}
    content["appname"] = 'Timetable'
    content["version"] = 245
    content["title"] = '新版本(V2.4.5)'
    content["force"] = 139
    content["type"] = 0
    content["alipay"] = """563049812"""
    content["positiveButtonText"] = "下载"
    content["updateurl"] = 'https://www.coolapk.com/apk/com.strivexj.timetable'
    content[
        "upgradeinfo"] = """更新过后需要重新设置背景, 重新添加单日课程插件。
新增划词翻译(查词只需一步，直接复制单词即可弹窗翻译)。
新增通知栏显示课程信息，点击快速查词功能（支持在线查词）
支持自定义侧拉菜单背景
支持自定义单词列表自动读音的间隔和次数
支持倒计时导入导出
修复成都理工大学以及已知导课BUG。
修复倒计时插件Bug，支持添加多个倒计时插件
桌面插件添加日期

历史记录：
V2.4.0
新增 新正方系统导课，单节课桌面插件，支持自定义标题栏颜色，优化单词查找功能，修复若干Bug。
V2.3.2
新增课程导出txt，starred单词导出txt。
V2.3.1
修复导课BUG，增加更多自定义选项，优化桌面插件，新增一位开发大佬。
Tips:手动导课和用Excel、txt导入的同学，导课成功后最好将课程导出为文本或txt存放以免误删丢失。如果课程信息显示不全，可自行在设置里改变格子高度、字体大小或删减课程名字。"""

    return HttpResponse(dumps(content, ensure_ascii=False), content_type="application/json")


def list_path(path):
    file_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            list_path(file_path)
        else:
            file_list.append(file_path)
    return file_list


def tv_series_list(request):
    base = "/home/wwwroot/www.strivexj.com/myfiles/tvseries"
    mlist = []

    tv = {
        "id": 1,
        "tvName": "friends",
        "en": "Friends",
        'zh': "老友记",
        'src': "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2187822907.webp",
        'resource': os.path.join(base, "friends.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 2,
        "tvName": "agentsofshield",
        "en": "Agents of S.H.I.E.L.D.",
        'zh': "神盾局特工",
        'src': "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2505133194.webp",
        'resource': os.path.join(base, "agentsofshield.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 3,
        "tvName": "thebigbangtheory",
        "en": "The Big Bang Theory",
        'zh': "生活大爆炸",
        'src': "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2499638425.webp",
        'resource': os.path.join(base, "thebigbangtheory.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 4,
        "tvName": "sherlock",
        "en": "Sherlock",
        'zh': "神探夏洛克",
        "src": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2412027382.webp",
        'resource': os.path.join(base, "sherlock.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 5,
        "tvName": "brokegirls",
        "en": "Broke Girls",
        'zh': "破产姐妹",
        "src": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2426595773.webp",
        'resource': os.path.join(base, "brokegirls.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 6,
        "tvName": "desperatehousewives",
        "en": "Desperate Housewives",
        'zh': "绝望主妇",
        "src": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1208078100.webp",
        'resource': os.path.join(base, "desperatehousewives.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 7,
        "tvName": "gameofthrones",
        "en": "Game of Thrones",
        'zh': "权力的游戏",
        "src": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2462245619.webp",
        'resource': os.path.join(base, "gameofthrones.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 8,
        "tvName": "siliconvalley",
        "en": "Silicon Valley",
        'zh': "硅谷",
        "src": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2172371194.webp",
        'resource': os.path.join(base, "siliconvalley.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 9,
        "tvName": "modernfamily",
        "en": "Modern Family",
        'zh': "摩登家庭",
        "src": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2376089099.webp",
        'resource': os.path.join(base, "modernfamily.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 999,
        "tvName": "all",
        "en": "All",
        'zh': "全部词汇",
        "src": "https://strivexj.com/myfiles/all_glossarys.jpg",
        'resource': os.path.join(base, "modernfamily.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 10,
        "tvName": "wordfrequencylist",
        "en": "Word Frequency List",
        'zh': "Word Frequency List",
        "src": "https://strivexj.com/myfiles/p.jpg",
        'resource': os.path.join(base, "modernfamily.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 11,
        "tvName": "dict",
        "en": "Dict",
        'zh': "Dict",
        "src": "https://strivexj.com/myfiles/p.jpg",
        'resource': os.path.join(base, "modernfamily.json"),
        "description": ""
    }
    mlist.append(tv)

    tv = {
        "id": 12,
        "tvName": "ieltslistening",
        "en": "IELTS Listening",
        'zh': "雅思听力",
        "src": "https://strivexj.com/myfiles/p.jpg",
        'resource': os.path.join(base, "ieltslistening.json"),
        "description": ""
    }

    mlist.append(tv)

    return HttpResponse(dumps(mlist, ensure_ascii=False),

                        content_type="application/json")
