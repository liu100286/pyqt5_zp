# import re
import requests

data =, [{
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnLl2gp6KgeBHGmVxBawPold/?quality=720p&data_version=6805469764316563207",
             "text": "牙齿美白牙膏.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnCaOAGoiGGi6AwGHytUxlFe/?quality=720p&data_version=6805483090014635783",
             "text": "手持蒸汽挂烫机熨斗.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnMVJToa6SjlJpgOONUiHdkc/?quality=720p&data_version=6805468024091477773",
             "text": "收腹美背背心.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnSYVHSmgUyK3eEfRBAksSqg/?quality=480p&data_version=6805460468317030157",
             "text": "感温变色戒指.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnoC4PkYx9nahCPxKDDEF83X/?quality=720p&data_version=6805468124683437838",
             "text": "分格保温日式便当饭盒.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcn6m9ajpbST0RjnJdUZ2vrtc/?quality=720p&data_version=6805468386043102983",
             "text": "小型台式全自动洗碗机.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnAia3aAxGAStPmyVami3Wef/?quality=720p&data_version=6805471478612494093",
             "text": "收腹美背背心.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnoDY7i2WjXDZarOdMt8740f/?quality=720p&data_version=6805469588927547149",
             "text": "包脸包头面罩巾.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcn0t0kVcDWU2oGOe33hCDG0c/?quality=720p&data_version=6805470821407016718",
             "text": "纯棉吸汗透气船袜.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnMR81IbgIVr0INb7XXh0ZRc/?quality=720p&data_version=6805458449179084557",
             "text": "可折叠调节遮阳帽.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnmvrZDQ6vcF1K2rVRG6g1Pg/?quality=720p&data_version=6805468257793869581",
             "text": "情侣款潮流连帽卫衣.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcn6G28RCrAjywmQFYF4DAu6N/?quality=720p&data_version=6805469853189670663",
             "text": "收腹黑色裤.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnZHsOYC9XEs8ZwJIahiiiZc/?quality=720p&data_version=6805468900570957575",
             "text": "挡风玻璃胶.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnNrQhU4jQd91qipFXebRsEc/?quality=720p&data_version=6805458269855811341",
             "text": "艾草颈椎贴.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnG0kr1cNngZYqAsUBiz8Bwd/?quality=720p&data_version=6805469233779050247",
             "text": "防滑洗手间地垫.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnWOc8xMD0e1aYB4fUbsBwIh/?quality=720p&data_version=6805469365023016712",
             "text": "化妆品收纳包.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcn0gei1RT0j5yA8dWjDJVDdc/?quality=720p&data_version=6805458174494115597",
             "text": "家用皂液器.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnyNoD46cEqVLm4WxCAWuJth/?quality=720p&data_version=6805458290168825614",
             "text": "切药磨药器.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnJZHwAT1vFR7UXiAvzPkr4y/?quality=720p&data_version=6805469499257521928",
             "text": "真空压缩收纳袋.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnoqdb36YVRqF9XU99wq4tsg/?quality=720p&data_version=6805470380791170830",
             "text": "分格保温日式便当饭盒.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcns6RBfKsqaoHGhmnrqX25nd/?quality=720p&data_version=6805470480548497166",
             "text": "硅胶锅铲套装.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnHfDVryU1UkXy1pbFk6cjRL/?quality=720p&data_version=6805470044600928014",
             "text": "食品级硅胶保鲜盖.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnin24mzn1h892MASfRVOYac/?quality=720p&data_version=6805458400898451208",
             "text": "可遥控自拍杆.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnSl1pW4PE8dFWmBVTq09M0f/?quality=720p&data_version=6805470162481841928",
             "text": "牙齿美白牙膏.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnzXs9SQW7Xa5Y0ZZdSiC5hf/?quality=720p&data_version=6805470640062072590",
             "text": "口腔清新喷雾.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnrUkt69y8juRIkyhIjDCw4l/?quality=720p&data_version=6805470238109337358",
             "text": "留香沐浴露.mp4"}, {
             "href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcn09b5CMCXzEvU9maAMYwUZf/?quality=720p&data_version=6805470961828103943",
             "text": "小型台式全自动洗碗机.mp4"}, {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcnyNoD46cEqVLm4WxCAWuJth/?quality=720p&data_version=6805458290168825614", "text": "手持蒸汽挂烫机熨斗.mp4"}, {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcnJZHwAT1vFR7UXiAvzPkr4y/?quality=720p&data_version=6805469499257521928", "text": "迷你折叠洗衣机.mp4"},
         {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcnoqdb36YVRqF9XU99wq4tsg/?quality=720p&data_version=6805470380791170830", "text": "随身无线卡啦OK音响.mp4"}, {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcns6RBfKsqaoHGhmnrqX25nd/?quality=720p&data_version=6805470480548497166", "text": "剃头电推子.mp4"}, {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcnHfDVryU1UkXy1pbFk6cjRL/?quality=720p&data_version=6805470044600928014", "text": "手势悬浮小飞车.mp4"},
         {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcnin24mzn1h892MASfRVOYac/?quality=720p&data_version=6805458400898451208", "text": "感温变色戒指.mp4"}, {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcnSl1pW4PE8dFWmBVTq09M0f/?quality=720p&data_version=6805470162481841928", "text": "私人订制证件套.mp4"}, {"href": "https://internal-api-space-hl.feishu.cn/space/api/box/stream/download/video/boxcnzXs9SQW7Xa5Y0ZZdSiC5hf/?quality=720p&data_version=6805470640062072590", "text": "显示歌词风扇.mp4"},
         {"href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcnrUkt69y8juRIkyhIjDCw4l/?quality=720p&data_version=6805470238109337358", "text": "四川牛油火锅底料.mp4"}, {"href": "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcn09b5CMCXzEvU9maAMYwUZf/?quality=720p&data_version=6805470961828103943", "text": "栀子花盆栽带花苞.mp4"}]

url = "https://internal-api-space-lf.feishu.cn/space/api/box/stream/download/video/boxcns3mijaZVQhphJpbmtvXdKb/?quality=720p&data_version=6815785544388182019"
cookie = 'TS01c8a37e=015df6ccf208c91099ba8bffe1364372bfdb0e92076f24689563a2034086afb5a6eb2d96a7696bee8066c05c5c3b54134d407871ac; TS01586647=015df6ccf23aa565c683a9992e9c093258354a9b13ebc23ea5d0c6e0f957d3af8bbb41391522d3fc857a21b2756b6230da1d82c847; session=anonymous_w5bCvcOBdMOswoUhb8Kbw6BDwrfDuGgnw4IdesK8LxzDh8KUw6TDvVs%2FejPCpFo%2BIAZ2w6HDk8K%2Fw79nwqRpwphvc2pxXg%3D%3D; is_anonymous_session=1; _csrf_token=930ce08c8a865d3d7b374c5e0cf1f999aafee86c-1587119155; TS01b6f2c9=015df6ccf208c91099ba8bffe1364372bfdb0e92076f24689563a2034086afb5a6eb2d96a7696bee8066c05c5c3b54134d407871ac; lang=zh'
# header = {
# 'Cookie': cookie
# }
# r = requests.get(url, headers=header)
# with open('name.mp4', "wb") as mp4:
#     for chunk in r.iter_content(chunk_size=1024 * 1024):
#         if chunk:
#             mp4.write(chunk)
# url = 'https://bytedance.feishu.cn/docs/doccneJeuICgwq0a3IX8kjkyyqb'
header = {
    'Cookie': cookie
}
name_ = '';
for n in data:
    r = requests.get(n['href'], headers=header)
    with open(n['text'], "wb") as mp4:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp4.write(chunk)
# with open('name.mp4', "wb") as mp4:
#     for chunk in r.iter_content(chunk_size=1024 * 1024):
#         if chunk:
#             mp4.write(chunk)
