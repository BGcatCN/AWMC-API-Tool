# B50 Upload API 脚本

一个简单的Python脚本，用于请求 B50 数据上传 API。

## 功能

- 从用户输入获取 `qr_text`
- 从 `.env` 文件读取令牌（fish_token 或 lxns_code）和 bearer_token
- 发送带有认证头的 API 请求到不同服务（水鱼或落雪）
- 显示 API 响应结果

## 环境要求

- Windows 操作系统
- Python 3.13（已包含在项目中）

## 安装步骤

1. 克隆或下载项目文件夹。
2. 无需额外安装，项目已包含虚拟环境和所有依赖包。

## 配置

1. 编辑 `.env` 文件，设置以下变量：
   ```
   FISH_TOKEN=你的_fish_token
   BEARER_TOKEN=你的_bearer_token
   LXNS_CODE=你的_lxns_code
   ```

## 使用方法

1. 双击 `run_upload_b50.bat` 文件。
2. 选择要运行的脚本：输入 1（上传水鱼）或 2（上传落雪）。
3. 在命令窗口中输入 `qr_text` 并按回车。
4. 查看 API 响应结果。

## 文件说明

- `upload_b50.py`：上传水鱼脚本文件
- `upload_b50_lx.py`：上传落雪脚本文件
- `run_upload_b50.bat`：Windows 批处理文件，用于选择并运行脚本
- `requirements.txt`：Python 依赖包列表
- `.env`：环境变量配置文件
- `venv/`：虚拟环境文件夹，包含 Python 解释器和依赖包

## 注意事项

- 确保 `.env` 文件中的变量名和值正确。
- 如果遇到网络问题，请检查 API 地址和认证信息。
- 脚本会在运行结束后暂停显示结果，按任意键退出。

## API 信息

- URL：`https://api.awmc.cc/v1/upload_b50?qr_text={qr_text}&fish_token={fish_token}`
- 请求方法：GET
- 请求头：`Authorization: Bearer {bearer_token}`