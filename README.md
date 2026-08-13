# 🎬 AI-Drama-FullStack — 全栈AI追剧应用

<div align="center">

![GitHub](https://img.shields.io/badge/Platform-UniApp-green)
![GitHub](https://img.shields.io/badge/Backend-Flask-blue)
![GitHub](https://img.shields.io/badge/Database-MySQL-orange)
![GitHub](https://img.shields.io/badge/Frontend-Vue3-brightgreen)
![GitHub](https://img.shields.io/badge/License-MIT-yellow)

**基于 UniApp(Vue3) + Flask + MySQL + AI 的全栈跨端追剧应用**  
**一套代码，运行于 H5 与微信小程序**

</div>

---

## 📖 项目简介

**AI-Drama-FullStack** 是一款集追剧管理与智能推荐于一体的全栈应用。用户可通过关键词搜索剧集、查看详情、收藏点赞、记录观看进度，并享受 AI 智能助手的个性化推荐与互动问答。

> 这是我在保研准备阶段独立开发的全栈 + AI 综合实践项目，旨在探索 AI 能力在传统追剧场景中的落地应用。

---

## ✨ 功能特点

| 功能模块 | 说明 |
|---------|------|
| 🔍 **剧集搜索** | 关键词搜索，智能匹配推荐 |
| 📺 **剧集详情** | 展示剧集信息、选集列表、演员阵容 |
| ⭐ **收藏系统** | 一键收藏，数据持久化存储 |
| ❤️ **点赞系统** | 互动点赞，实时更新状态 |
| 📜 **历史记录** | 自动记录观看进度，断点续看 |
| 🤖 **AI 智能助手** | 多角色对话，智能推荐剧集 |
| 📱 **跨端适配** | 一套代码，运行于 H5 和微信小程序 |
| 🎨 **精美 UI** | 统一设计系统，流畅交互体验 |

---

## 🛠️ 技术栈

### 前端
- **UniApp** - 跨端开发框架
- **Vue 3** - 响应式 UI 框架
- **SCSS** - CSS 预处理器
- **uni-ui** - 官方组件库
- **HBuilderX** - 开发工具

### 后端
- **Flask** - Python Web 框架
- **Flask-CORS** - 跨域资源共享
- **PyMySQL** - MySQL 数据库驱动
- **Requests** - HTTP 请求库

### 数据库
- **MySQL** - 关系型数据库
- **JSON 字段** - 灵活存储剧集数据

### 数据来源
- **芒果TV API** - 剧集数据来源（含 MD5 签名破解）

---

## 📱 项目截图

| 首页 | 详情页 | 搜索页 |
|------|--------|--------|
| ![首页](screenshots/1.png) | ![详情](screenshots/2.png) | ![搜索](screenshots/3.png) |

| 我的页面 | AI 助手 | 历史记录 |
|------|--------|--------|
| ![我的](screenshots/4.png) | ![AI](screenshots/5.png) | ![历史](screenshots/6.png) |

---

## 🚀 快速开始

### 前端启动（HBuilderX）

1. 用 **HBuilderX** 打开项目
2. 点击菜单栏 **运行** → **运行到浏览器**
3. 或点击工具栏的 ▶️ 运行按钮

### 后端启动

```bash
# 进入后端目录
cd backend

# 安装 Python 依赖
pip install -r requirements.txt

# 启动 Flask 服务
python app.py
数据库配置
sql
CREATE DATABASE playlets;
USE playlets;

CREATE TABLE history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    card JSON COMMENT '剧集数据',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE search (
    id INT PRIMARY KEY AUTO_INCREMENT,
    content VARCHAR(255) COMMENT '搜索关键词',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
📁 项目结构
text
AI-Drama-FullStack/
├── pages/                      # 页面目录
│   ├── index/                  # 首页
│   ├── detail/                 # 详情页
│   ├── search/                 # 搜索页
│   ├── my/                     # 我的页面
│   └── webview/                # WebView 播放页
├── components/                 # 公共组件
├── stores/                     # 状态管理
├── utils/                      # 工具函数
├── static/                     # 静态资源
├── uni_modules/                # uni-ui 组件
├── backend/                    # 后端服务
│   ├── app.py                  # Flask 主程序
│   ├── dataset.py              # 数据集处理
│   └── search_decrypt.js       # 搜索解密脚本（JS逆向分析）
├── screenshots/                # 项目截图
├── App.vue                     # 应用入口
├── main.js                     # 主文件
├── manifest.json               # 项目配置
├── pages.json                  # 页面路由
├── .gitignore                  # Git 忽略文件
├── LICENSE                     # MIT 开源协议
└── README.md                   # 项目说明
🏆 技术亮点
1. 🔐 API 签名破解
成功破解芒果 TV 搜索接口的 MD5 动态签名机制，通过 JS 逆向分析还原签名算法，实现数据的高效采集。

python
import hashlib

def generate_sign(params):
    """还原芒果TV MD5签名算法"""
    sorted_keys = sorted(params.keys())
    sign_str = '&'.join([f'{k}={params[k]}' for k in sorted_keys])
    return hashlib.md5(sign_str.encode('utf-8')).hexdigest()
2. 🤖 AI 智能助手
集成多角色 AI 对话系统，支持「剧小迷」和「计算机专家」两种角色切换，实现智能问答与剧集推荐。

3. 📱 跨端适配
基于 UniApp 实现一套代码，多端运行，流畅适配 H5 与微信小程序平台。

4. 💾 数据持久化
使用 MySQL 的 JSON 字段灵活存储剧集数据，配合本地缓存实现数据一致性。

📄 License
MIT License © 2026 namew11

🙏 致谢
数据来源：芒果TV

开发框架：UniApp

后端框架：Flask
