# AWMC B50 Upload API Request Tool

这是一个简单的 Python 脚本，用于请求 AWMC B50 上传 API。

## 功能特性

- 默认请求 `https://api.awmc.cc/v1/upload_b50` 端点
- 支持 Bearer 令牌认证
- 交互式输入 `qr_text` 参数
- 从 `.env` 文件读取 `FISH_TOKEN` 和 `BEARER_TOKEN`

## 开箱即用

1. **双击运行**：直接双击 `run.bat` 文件启动脚本。
2. **手动运行**：在命令行中运行 `python api_request.py`。

## 配置

编辑 `.env` 文件，设置你的令牌：

```env
FISH_TOKEN=你的鱼令牌
BEARER_TOKEN=你的Bearer令牌
```

## 使用方法

### 默认模式（推荐）

运行脚本后，会提示输入 `qr_text`：

```bash
python api_request.py
# 或双击 run.bat
```

### 自定义 qr_text

```bash
python api_request.py --qr-text "你的二维码文本"
```

### 自定义环境文件

```bash
python api_request.py --env-file "path/to/your/.env"
```

### 其他 API 请求

如果你想请求其他 API，可以指定 URL：

```bash
python api_request.py https://api.example.com/endpoint -X POST -j '{"key": "value"}'
```

## 依赖

- Python 3.6+
- 无需额外包（使用标准库）

## 注意事项

- 确保 `.env` 文件存在且包含必要的令牌
- Bearer 令牌会自动添加到请求头中
- 如果 Python 未安装，`run.bat` 会提示安装