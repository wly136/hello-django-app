# 🚀 Hello Django 应用

一个功能完整、现代化的Django示例应用，展示了Django框架的最佳实践和现代Web开发技术。

![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ 功能特性

- 🌐 **响应式设计** - 完美适配桌面和移动设备
- 🎨 **现代化UI** - 基于CSS变量和现代设计原则
- ⚡ **高性能** - 优化的静态文件处理和缓存策略
- 🔒 **安全配置** - 遵循Django安全最佳实践
- 📱 **移动友好** - 触摸友好的交互设计
- 🚀 **开发友好** - 详细的文档和开发指南

## 🛠️ 技术栈

- **后端框架**: Django 4.2+
- **前端技术**: HTML5, CSS3, JavaScript
- **数据库**: SQLite (开发), 支持PostgreSQL/MySQL (生产)
- **静态文件**: Django静态文件系统
- **部署就绪**: 包含生产环境配置指南

## 📦 安装与运行

### 前提条件
- Python 3.8+
- pip (Python包管理器)

### 快速开始

1. **克隆项目**
```bash
git clone https://github.com/wly136/hello-django-app.git
cd hello-django-app
```

2. **创建虚拟环境**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **环境配置**
```bash
# 复制环境变量示例文件
cp .env.example .env
# 编辑.env文件，设置你的安全密钥
# DJANGO_SECRET_KEY=your-super-secret-key-here
```

5. **数据库迁移**
```bash
python manage.py migrate
```

6. **创建超级用户** (可选)
```bash
python manage.py createsuperuser
```

7. **运行开发服务器**
```bash
python manage.py runserver
```

8. **访问应用**
- 主页: http://127.0.0.1:8000/
- 个性化问候: http://127.0.0.1:8000/hello/你的名字
- 管理后台: http://127.0.0.1:8000/admin/

## 📁 项目结构

```
hello-django-app/
├── hello/                    # Django应用
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── hello_project/           # Django项目配置
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/              # HTML模板
│   └── hello/
│       ├── index.html
│       └── greeting.html
├── static/                # 静态文件
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── images/
├── staticfiles/           # 收集的静态文件 (生产)
├── db.sqlite3             # 数据库文件
├── manage.py
├── requirements.txt
├── .env.example           # 环境变量示例
├── .gitignore
└── README.md
```

## 🎯 核心功能

### 首页 (/)
- 显示欢迎消息
- 提供功能导航
- 响应式设计展示

### 个性化问候 (/hello/<名字>)
- 动态URL参数处理
- 个性化的问候消息
- 美观的页面布局

### 管理后台 (/admin)
- Django自带的管理界面
- 用户和权限管理

## ⚙️ 配置说明

### 环境变量
项目使用环境变量进行配置，请复制`.env.example`为`.env`并设置以下变量：

```env
# 安全密钥 (生产环境必须修改)
DJANGO_SECRET_KEY=your-super-secret-key-here

# 调试模式 (生产环境设置为False)
DEBUG=True

# 允许的主机 (生产环境必须设置)
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 静态文件
静态文件配置已优化，支持开发和生产环境：
- 开发: 使用`STATICFILES_DIRS`
- 生产: 使用`python manage.py collectstatic`

## 🚀 部署到生产环境

### 1. 设置生产环境变量
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### 2. 收集静态文件
```bash
python manage.py collectstatic
```

### 3. 配置Web服务器
推荐使用:
- Nginx + Gunicorn
- Apache + mod_wsgi
- Docker容器化部署

### 4. 数据库配置
建议使用:
- PostgreSQL
- MySQL
- 云数据库服务

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🆘 常见问题

### Q: 静态文件无法加载？
A: 运行 `python manage.py collectstatic` 并检查Web服务器配置。

### Q: 如何添加新页面？
A: 1. 在`hello/views.py`中添加视图函数
   2. 在`hello/urls.py`中添加URL路由
   3. 在`templates/hello/`中创建HTML模板

### Q: 如何扩展功能？
A: 参考Django官方文档，可以添加:
- 用户认证系统
- 数据库模型
- REST API接口
- 实时功能(WebSocket)

## 📞 支持

如有问题，请通过以下方式联系：
- 创建 [Issue](https://github.com/wly136/hello-django-app/issues)
- 发送邮件到: your-email@example.com

---

⭐ 如果这个项目对你有帮助，请给它一个Star！