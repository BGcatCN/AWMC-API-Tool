import logging
import os
import time
import requests
from dotenv import load_dotenv

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('upload_b50_lx.log', encoding='utf-8')
    ]
)

# 加载环境变量
load_dotenv()

# 获取环境变量
lxns_code = os.getenv('LXNS_CODE')
bearer_token = os.getenv('BEARER_TOKEN')

if not lxns_code or not bearer_token:
    logging.error("错误：.env文件中缺少LXNS_CODE或BEARER_TOKEN")
    exit(1)

# 向用户索取qr_text
qr_text = input("请输入qr_text: ")

# 构建API URL
url = f"https://api.awmc.cc/v1/upload_lx_b50?qr_text={qr_text}&lxns_code={lxns_code}"

# 设置请求头
headers = {
    'Authorization': f'Bearer {bearer_token}'
}

logging.info("开始上传落雪任务")
logging.info(f"请求URL: {url}")
logging.debug(f"请求头: {headers}")


def poll_task_status(task_id, headers, timeout=60, interval=5, max_attempts=20):
    status_url = f"https://api.awmc.cc/v1/get_lx_b50_task_byid?task_id={task_id}"
    for attempt in range(1, max_attempts + 1):
        logging.info("轮询第 %s 次，查询任务状态：%s", attempt, status_url)
        try:
            status_response = requests.get(status_url, headers=headers, timeout=timeout)
            logging.info("状态查询响应状态码: %s", status_response.status_code)
            status_response.raise_for_status()

            try:
                status_data = status_response.json()
            except ValueError:
                logging.error("状态查询响应不是有效JSON: %s", status_response.text)
                return

            logging.info("状态查询JSON: %s", status_data)
            logging.info("msg: %s", status_data.get('msg'))
            logging.info("userid: %s", status_data.get('userid'))
            logging.info("uploadstatus: %s", status_data.get('uploadstatus'))
            logging.info("done: %s", status_data.get('done'))

            if status_data.get('done') is True:
                logging.info("B50上传任务完成，停止轮询。")
                return

            if attempt < max_attempts:
                time.sleep(interval)
        except requests.RequestException as e:
            logging.error("状态查询失败: %s", str(e))
            return

    logging.warning("轮询达到最大次数，停止查询。")

# 发送POST请求
try:
    response = requests.post(url, headers=headers)
    logging.info("响应状态码: %s", response.status_code)

    try:
        data = response.json()
    except ValueError:
        data = None

    if data:
        logging.info("响应JSON: %s", data)
        logging.info("msg: %s", data.get('msg'))
        logging.info("userid: %s", data.get('userid'))
        logging.info("uploadstatus: %s", data.get('uploadstatus'))

        task_id = data.get('task_id')
        if task_id:
            logging.info("开始轮询任务状态，task_id: %s", task_id)
            poll_task_status(task_id, headers)
        else:
            logging.warning("响应中未包含 task_id，无法轮询任务状态。")
    else:
        logging.warning("响应内容: %s", response.text)
except Exception as e:
    logging.error("请求失败: %s", str(e))