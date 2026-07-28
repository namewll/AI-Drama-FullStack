import re
import execjs
import requests
import json
from flask import Flask
from flask import request,Response
from flask_cors import CORS
from zai import ZhipuAiClient
from dataset import Dataset

obj=Dataset('AI_chat')
obj1=Dataset('PlayLets')
client = ZhipuAiClient(api_key="f488910fe9d5446ea1f9c4de3a42fe3f.WSDQYYvvJX61HG09")
messages=[{"role":"system","content":"""身份设定：你名为剧小迷，专属电视剧领域专家，覆盖国内外所有题材电视剧（古装、现代、悬疑、言情、刑侦、家庭、奇幻、年代等）。
能力范围：
1. 根据用户喜好精准推荐适配剧集；
2. 复述剧情、解析伏笔结局、说明人物关系；
3. 查询参演演员、播出平台、上映年份；
4. 推荐风格高度相似的替代剧集。
回复要求：语气亲切自然，单次回答字数不超120，不编造不存在的剧集信息，不清楚的内容直接如实说明。
对话边界：仅回应电视剧相关问题，无关话题礼貌说明无法解答。
"""}]
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://www.mgtv.com",
    "priority": "u=1, i",
    "referer": "https://www.mgtv.com/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Google Chrome\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
app = Flask(__name__)
CORS(app)

with open("search_decrypt.js",'r',encoding='utf-8')as f:
    js_code=f.read()
execjs_code=execjs.compile(js_code)

@app.route('/api/playlets')
def api_playlets():
    page=request.args.get('page')
    limit=request.args.get('limit')
    url = "https://pianku.api.mgtv.com/rider/list/pcweb/v3"
    params = {
        "allowedRC": "1",
        "platform": "pcweb",
        "channelId": "2",
        "pn": f"{page}",
        "pc": f"{limit}",
        "hudong": "1",
        "_support": "10000000",
        "kind": "a1",
        "area": "a1",
        "year": "all",
        "feature": "all",
        "chargeInfo": "a1",
        "sort": "c2"
    }
    response = requests.get(url, headers=headers, params=params)
    hitDocs=response.json()
    for hit in hitDocs['data']['hitDocs']:
        hit['collect']=False
        hit['like']=False
        hit['progress']=0
    return hitDocs

@app.route("/api/playlet/detail")
def playlet_detail():
    id = request.args.get("id")
    url = "https://mobile-thor.api.mgtv.com/v1/vod/info"
    params = {
        "allowedRC": "1",
        "_support": "10000000",
        "uuid": "fdde58ed-1e9f-4f5e-962b-4dedcf312006",
        "ticket": "",
        "did": "fdde58ed-1e9f-4f5e-962b-4dedcf312006",
        "device": "pc",
        "osType": "window",
        "osVersion": "10.0",
        "appVersion": "9.0.4-1",
        "platform": "4",
        "seqId": "fdde58ed-1e9f-4f5e-962b-4dedcf312006",
        "src": "mgtv",
        "videoId": "9918182",
        "clipId": f"{id}"
    }
    response = requests.get(url, headers=headers, params=params)
    result = response.json()
    data=result["data"]["info"]["clip"]
    id = data["clipId"]
    title = data['clipName']
    episode_cnt = data['serialCount']
    info = data['story']
    img=data['vImgUrl']
    kind=[]
    kinds=result['data']['template']['modules'][0]['clipInfo']['detail']
    video_total=[]
    videos=result['data']['template']['modules'][2]['media']['filters'][0]['list']
    index=0
    for video in videos:
        index+=1
        if index>int(episode_cnt):
            break
        video_total.append(video['videoId'])
    for item in kinds:
        kind.append(item['font'])
    content={
        "code":200,
        "data":
            {"clipId": id,
             "title": title,
             "episode_cnt": episode_cnt,
             "info": info,
             "img": img,
             "kind": kind,
             "video_total":video_total,
             "progress":0
             }
    }
    return json.dumps(content, ensure_ascii=False)

@app.route('/api/playlet/search')
def search_playlet():
    query = request.args.get('query')
    page = request.args.get('page')
    limit = request.args.get('limit')
    res_list = execjs_code.call("get_param",query,page,limit)
    timestamp=res_list[0]
    signNonce=res_list[1]
    signature=res_list[2]
    sql=f"""select * from search where content = '{query}' """
    select_res=obj1.select(sql)
    if select_res:
        sql=f"""delete from search where content = '{query}' """
        obj1.change(sql)
    sql=f"""insert into search VALUES(0,'{query}')"""
    obj1.change(sql)
    url = "https://mobileso.bz.mgtv.com/pc/search/v2"
    params = {
        "allowedRC": "1",
        "src": "mgtv",
        "did": "70ae7094-37cb-4741-84aa-943fa13dca36",
        "timestamp": f"{timestamp}",
        "signVersion": "1",
        "signNonce": f"{signNonce}",
        "q": f"{query}",
        "pn": f"{page}",
        "pc": f"{limit}",
        "uid": "",
        "corr": "1",
        "_support": "10000000",
        "signature": f"{signature}"
    }
    response = requests.get(url, headers=headers, params=params)
    results=response.json()['data']['contents']
    content=[]
    year=0
    index=0
    short_video=[]
    kind_=[]
    result=results[0]
    name = result['data'].get('name', '')
    if name:
        title = result['data']['name']
        img = result['data']['pic']
        kind_.append(result['data']['desc'][0]['text'])
        kind_.append(result['data']['desc'][1]['text'])
        story = result['data']['story']
        id = ''
        for i in range(0, len(result['data']['tablist'])):
            short_video.extend(result['data']['tablist'][i]['data'])
        data = {
            "title": title,
            "img": img,
            "kind": kind_,
            "clipId": id,
            "year": year,
            "story": story,
            "progress": 0,
            "short_video": short_video,
            "name":True
        }
        content.append(data)
        result = {
            "code": 200,
            "data": content
        }
        return json.dumps(result, ensure_ascii=False)

    if not name:
        for result in results:
            year_list=result['data'].get("yearList",'')
            title = result['data'].get('title','')
            kind = []
            if year_list:
                year=1
                title=year_list[0]['title']
                img=year_list[0]['pic']
                kind.append(year_list[0]['desc'][0]['text'])
                story=year_list[0]['story']
                url_str = year_list[0]['sourceList'][0]['url']
                id = re.findall('\d+', url_str)[0]
                short_video = year_list[0]['sourceList'][0]['videoList']
            elif title:
                title = result['data']['title']
                img = result['data']['pic']
                kind.append(result['data']['desc'][0]['text'])
                story = result['data']['story']
                url_str = result['data']['sourceList'][0]['url']
                id = re.findall('\d+', url_str)[0]
                short_video = result['data']['sourceList'][0]['videoList']
            data={
                "title":title,
                "img":img,
                "kind":kind,
                "clipId":id,
                "year":year,
                "story":story,
                "progress": 0,
                "short_video":short_video,
                "name": False
            }
            content.append(data)
        result={
            "code":200,
            "data":content
        }
        return json.dumps(result, ensure_ascii=False)

@app.route('/api/selector')
def api_selector():
    url = "https://pianku.api.mgtv.com/rider/config/channel/v1"
    params = {
        "allowedRC": "1",
        "channelId": "2",
        "platform": "pcweb",
        "_support": "10000000"
    }
    response = requests.get(url, headers=headers, params=params)
    return json.dumps(response.json(), ensure_ascii=False)

@app.route('/api/playlet/screen')
def playlet_screen():
    background=request.args.get("background").split("=")[-1]
    topic=request.args.get("topic").split("=")[-1]
    setting=request.args.get("setting").split("=")[-1]
    gender=request.args.get("gender").split("=")[-1]
    time=request.args.get("time").split("=")[-1]
    sort_type=request.args.get("sort_type").split("=")[-1]
    page=request.args.get("page")
    limit=request.args.get("limit")
    url = "https://pianku.api.mgtv.com/rider/list/pcweb/v3"
    params = {
        "allowedRC": "1",
        "platform": "pcweb",
        "channelId": "2",
        "pn": page,
        "pc": limit,
        "hudong": "1",
        "_support": "10000000",
        "kind": background,
        "area": topic,
        "year": setting,
        "feature": gender,
        "chargeInfo": time,
        "sort": sort_type
    }
    response = requests.get(url, headers=headers, params=params)
    data=response.json()['data']['hitDocs']
    content_total=[]
    for item in data:
        id=item['clipId']
        title=item['title']
        img=item['img']
        type=item['kind']
        episode_cnt=re.search("\d+",item['updateInfo']).group()
        content={
            "clipId":id,
            "title":title,
            "img":img,
            "type":type,
            "episode_cnt":episode_cnt,
            "like":False,
            "collect":False
        }
        content_total.append(content)
    result={
        "code":200,
        "data":content_total
    }
    return json.dumps(result, ensure_ascii=False)

@app.route('/api/user/user_info')
def user_info():
    user_id=request.args.get('user_id')
    if user_id=="u_001":
        data={
            "code":200,
            "data":{
                "attention":10,
                "fans":5,
                "getlike":5,
                "name":"七沫阳光"
            }
        }
        return json.dumps(data, ensure_ascii=False)
    return

@app.route('/change_role')
def change_role():
    global messages
    ai_role = request.args.get('role')
    if(ai_role=='计算机专家老师'):
        messages=[{"role":"system","content":"""身份设定：你是一名资深计算机专家和编程导师，精通Python、Java、Vue、React、Flask、MySQL、AI等主流技术。
能力范围：
1. 解答编程问题，提供完整可运行的代码示例；
2. 讲解数据结构、算法、设计模式等计算机基础知识；
3. 指导前端、后端、数据库、Linux运维等实战开发；
4. 帮助调试代码，分析错误原因并提供解决方案。
回复要求：用通俗语言解释概念，代码带注释说明，回答详细准确，不清楚的内容直接如实说明,单次回答字数不超120。
对话边界：专注计算机技术相关问题，非技术话题礼貌说明无法解答。
"""}]
    elif(ai_role=='剧小迷'):
        messages = [{"role": "system", "content": """身份设定：你名为剧小迷，专属电视剧领域专家，覆盖国内外所有题材电视剧（古装、现代、悬疑、言情、刑侦、家庭、奇幻、年代等）。
        能力范围：
        1. 根据用户喜好精准推荐适配剧集；
        2. 复述剧情、解析伏笔结局、说明人物关系；
        3. 查询参演演员、播出平台、上映年份；
        4. 推荐风格高度相似的替代剧集。
        回复要求：语气亲切自然，单次回答字数不超120，不编造不存在的剧集信息，不清楚的内容直接如实说明。
        对话边界：仅回应电视剧相关问题，无关话题礼貌说明无法解答。
        """}]
    return "角色更换成功"

@app.route('/api/chat')
def chat():
    # print(messages)
    data=request.args.get("content")
    role = request.args.get('role')
    messages.append({"role":"user","content":data})
    def gen_stream():
        response=client.chat.completions.create(
            model="glm-5.2",
            messages=messages,
            stream=True
        )
        total_result=''
        for chunk in response:
            result=chunk.choices[0].delta.content
            if result is None:
                continue
            total_result+=result
            yield f"data:{result}\n\n"
        yield "data:[DONE]\n\n"
        messages.append({"role":"assistant","content":total_result})
        # print(data)
        # print(total_result)
        sql=""
        if role=="0":
            sql=f"""insert into chat_info values(0,'{data}','{total_result}')"""
        elif role=="1":
            sql = f"""insert into teacher_info values(0,'{data}','{total_result}')"""
        obj.change(sql)
        if len(messages)>16:
            del messages[1]
    return Response(
        gen_stream(),
        mimetype='text/event-stream',
        headers={"Cache-Control":"no-cache"}
    )

@app.route('/chat/info')
def chat_info():
    sql="""select * from chat_info"""
    res=obj.select(sql)
    item_list=[]
    for item in res:
        item_list.append({
            "user":item[1],
            "ai":item[2]
        })
    return json.dumps(item_list,ensure_ascii=False)

@app.route('/delete/info')
def delete_info():
    user_text=request.args.get('user_text')
    ai_text=request.args.get('ai_text')
    role=request.args.get('role')
    sql=""
    if role == "0":
        sql=f"""delete from chat_info where duser='{user_text}' and AI='{ai_text}'"""
    elif role=="1":
        sql = f"""delete from teacher_info where duser='{user_text}' and AI='{ai_text}'"""
    obj.change(sql)
    return "删除成功"

@app.route('/teacher/info')
def teacher_info():
    sql="""select * from teacher_info"""
    res=obj.select(sql)
    item_list=[]
    for item in res:
        item_list.append({
            "user":item[1],
            "ai":item[2]
        })
    return json.dumps(item_list,ensure_ascii=False)

@app.route('/show/search_info')
def search_info():
    sql = """select * from search"""
    res = obj1.select(sql)
    item_list = []
    for item in res:
        item_list.append(item[1])
    return json.dumps(item_list,ensure_ascii=False)

@app.route('/delete/search_info')
def delete_search_info():
    title=request.args.get('title')
    sql=f"""select * from search where content='{title}'"""
    select_res=obj1.select(sql)
    if select_res:
        sql=f"""delete from search where content='{title}'"""
        obj1.change(sql)
    return "删除成功"

@app.route('/delete/block')
def delete_block():
    sql="""delete from search"""
    obj1.change(sql)
    return "全部删除"

@app.route('/add/history')
def add_history():
    card=request.args.get('card')
    card_=json.loads(card)['clipId']
    sql=f"""select * from history where card LIKE '%{card_}%'"""
    res=obj1.select(sql)
    if res:
        sql=f"""delete from history where card LIKE '%{card_}%'"""
        obj1.change(sql)
    sql=f"""insert into history(id,card) values(0,'{card}')"""
    obj1.change(sql)
    return "添加成功"

@app.route('/select/history')
def select_history():
    id=request.args.get('id')
    sql=f"""select * from history where card LIKE '%{id}%'"""
    select_res=obj1.select(sql)
    if select_res:
        return json.loads(select_res[0][1])
    return ""

@app.route('/delete/history')
def delete_history():
    card=request.args.get('card')
    sql = f"""select * from history where card LIKE '%{card}%'"""
    select_res=obj1.select(sql)
    if select_res:
        sql=f"""delete from history where card LIKE '%{card}%'"""
        obj1.change(sql)
    return "历史删除成功"

@app.route('/select/total/history')
def select_total_history():
    sql=f"""select * from history where card LIKE '%"progress":%' AND card NOT LIKE '%"progress":0%'"""
    select_res=obj1.select(sql)
    result=[]
    if select_res:
        for hist in select_res:
            result.append(json.loads(hist[1]))
        return json.dumps(result, ensure_ascii=False)
    return ""

@app.route('/select/total/collect')
def select_total_collect():
    sql=f"""select * from history where card LIKE '%"collect":true%'"""
    select_res=obj1.select(sql)
    result=[]
    if select_res:
        for hist in select_res:
            result.append(json.loads(hist[1]))
        return json.dumps(result, ensure_ascii=False)
    return ""

@app.route('/select/total/like')
def select_total_like():
    sql=f"""select * from history where card LIKE '%"like":true%'"""
    select_res=obj1.select(sql)
    result=[]
    if select_res:
        for hist in select_res:
            result.append(json.loads(hist[1]))
        return json.dumps(result, ensure_ascii=False)
    return ""

if __name__ == "__main__":
    app.run(port=5001, debug=True)