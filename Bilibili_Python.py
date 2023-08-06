from bs4 import BeautifulSoup
import requests
import re 
import os
#普通视频的爬取
def Python_bilibili(url):
#获取视频链接
    
#url="https://cn-hnzz-cm-01-04.bilivideo.com/upgcxcode/48/34/1194003448/1194003448-1-100110.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1691163198&gen=playurlv2&os=bcache&oi=3746443439&trid=00004923d0906128481fa74e1a5bad7d47f5u&mid=0&platform=pc&upsig=52d48dba17588f66fcb11f672b6a42a1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=5368&bvc=vod&nettype=0&orderid=0,3&buvid=8216863F-BDC7-82AD-E040-DA3E57CD5F8998566infoc&build=0&agrr=0&bw=21756&logo=80000000"
    headers={"User-Agent" :"Mozilla/5.0(X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    "cookie":"buvid3=18D5E06F-CE86-C214-82D8-B6206422651B06996infoc;b_nut=1686891606;_uuid=96111A10F-71DC-BDD3-68310-109F61D35F610309473infoc;buvid4=307D8A2A-E228-E57E-3361-6243C24FA32509799-123071509-SK3hbof5R8nvxnlzWNqbVvzC1SRroOby7dgsMMJNKYMhM0bA/Sjaaw%3D%3D;buvid_fp=da7c6770f590a1d40c303a37f93814ba;rpdid=|(J~RYRRJRuk0J'uYm|k)|)k~;FEED_LIVE_VERSION=V8;header_theme_version=CLOSE;home_feed_column=4;CURRENT_FNVAL=4048;browser_resolution=1100-2188;LIVE_BUVID=AUTO6216911584254065;PVID=1;share_source_origin=COPY;bsource=share_source_copy_link;b_lsid=3118FCD9_189C4622372;sid=7gbqbb20"
    }
    r=requests.get(url,headers=headers)
#print(f"响应码:{r.status_code},文本:{r.text}")
    with open("/storage/emulated/0/Python/html.txt","w",encoding="utf-8") as f:
         f.write(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
#for link in soup.find_all("script"):
    #if "window.__playinfo__" in str(link.string):
      # Target_link=str(link.string)
#print(Target_link)
    #print(r.text)
    #获取视频&音频链接
    video_link=re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"',r.text)[0]
#print(video_link)
    audio_link=re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"',r.text)[0]
#print(audio_link)
#获取视频名称
    attrs={"data-vue-meta":"true"}
    title=soup.find_all("title",attrs)[0].string
    print(title)
#获取响应
    #重新定义请求头
    headers={"User-Agent" :"Mozilla/5.0(X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    "cookie":"buvid3=18D5E06F-CE86-C214-82D8-B6206422651B06996infoc;b_nut=1686891606;_uuid=96111A10F-71DC-BDD3-68310-109F61D35F610309473infoc;buvid4=307D8A2A-E228-E57E-3361-6243C24FA32509799-123071509-SK3hbof5R8nvxnlzWNqbVvzC1SRroOby7dgsMMJNKYMhM0bA/Sjaaw%3D%3D;buvid_fp=da7c6770f590a1d40c303a37f93814ba;rpdid=|(J~RYRRJRuk0J'uYm|k)|)k~;FEED_LIVE_VERSION=V8;header_theme_version=CLOSE;home_feed_column=4;CURRENT_FNVAL=4048;browser_resolution=1100-2188;LIVE_BUVID=AUTO6216911584254065;PVID=1;share_source_origin=COPY;bsource=share_source_copy_link;b_lsid=3118FCD9_189C4622372;sid=7gbqbb20",
    "Referer":url
    }
    r_video=requests.get(video_link,headers=headers)
    r_audio=requests.get(audio_link,headers=headers)
    data_v=r_video.content
    data_a=r_audio.content
    print(r_video.status_code)
    print(r_audio.status_code)
#保存文件

    title_new=title+"new"
    with open(f"/storage/emulated/0/Python/Video/{title_new}.mp4","wb") as f:
        f.write(data_v)
    with open(f"/storage/emulated/0/Python/Video/{title_new}.mp3","wb") as f:
        f.write(data_a)
    
#合成
    os.system(f'ffmpeg -i "/storage/emulated/0/Python/Video/{title_new}.mp4" -i "/storage/emulated/0/Python/Video/{title_new}.mp3" -c copy "/storage/emulated/0/Python/Video/{title}.mp4"')

#移出视频
    os.remove(f"/storage/emulated/0/Python/Video/{title_new}.mp3")
    os.remove(f"/storage/emulated/0/Python/Video/{title_new}.mp4")
#多p视频的爬取
def Python_bilibili_p(url):
#获取响应体
    
#url="https://cn-hnzz-cm-01-04.bilivideo.com/upgcxcode/48/34/1194003448/1194003448-1-100110.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1691163198&gen=playurlv2&os=bcache&oi=3746443439&trid=00004923d0906128481fa74e1a5bad7d47f5u&mid=0&platform=pc&upsig=52d48dba17588f66fcb11f672b6a42a1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=5368&bvc=vod&nettype=0&orderid=0,3&buvid=8216863F-BDC7-82AD-E040-DA3E57CD5F8998566infoc&build=0&agrr=0&bw=21756&logo=80000000"
    headers={"User-Agent" :"Mozilla/5.0(X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    "cookie":"buvid3=18D5E06F-CE86-C214-82D8-B6206422651B06996infoc;b_nut=1686891606;_uuid=96111A10F-71DC-BDD3-68310-109F61D35F610309473infoc;buvid4=307D8A2A-E228-E57E-3361-6243C24FA32509799-123071509-SK3hbof5R8nvxnlzWNqbVvzC1SRroOby7dgsMMJNKYMhM0bA/Sjaaw%3D%3D;buvid_fp=da7c6770f590a1d40c303a37f93814ba;rpdid=|(J~RYRRJRuk0J'uYm|k)|)k~;FEED_LIVE_VERSION=V8;header_theme_version=CLOSE;home_feed_column=4;CURRENT_FNVAL=4048;browser_resolution=1100-2188;LIVE_BUVID=AUTO6216911584254065;PVID=1;share_source_origin=COPY;bsource=share_source_copy_link;b_lsid=3118FCD9_189C4622372;sid=7gbqbb20"
    }
    r=requests.get(url,headers=headers)
#print(f"响应码:{r.status_code},文本:{r.text}")
    with open("/storage/emulated/0/Python/html.txt","w",encoding="utf-8") as f:
         f.write(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    #获取视频p数
    attrs_num_p={
    "class":"cur-page"
    }
    print(soup.find_all("span",attrs=attrs_num_p)[0].string)
    P_num=int(re.findall(r'/(\d+)',soup.find_all("span",attrs=attrs_num_p)[0].string)[0])
    print(f"检测到{P_num}个视频")
    
#for link in soup.find_all("script"):
    #if "window.__playinfo__" in str(link.string):
      # Target_link=str(link.string)
#print(Target_link)
    #print(r.text)
#循环下载分p视频
    for i in range(1,P_num+1):
       #重新确定url
       url_p=url+"?p="+str(i)
       print(url_p)
       Python_bilibili(url_p)
       print(f"第{i}个视频下载完成")
Way=input("单个视频填1，分p视频填2\n")
#正则匹配url
url=input("请输入url\n")
url_temp=re.findall(r"https://b23.tv/([a-zA-Z0-9]*)",url)[0]
url="https://b23.tv/"+url_temp
headers={
  "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
#转换url
url_f=requests.get(url,headers=headers)
soup_url_f = BeautifulSoup(url_f.text, 'html.parser')
attrs_url_f={
"data-vue-meta":"true", 
"rel":"canonical" 
}
url=soup_url_f.find_all("link",attrs=attrs_url_f)[0].get("href")
#判断下载类型
if Way=="1":
    Python_bilibili(url)
else:
    Python_bilibili_p(url)
 

