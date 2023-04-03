项目名称：DailyLogGenerator
=========================

项目简介
----

DailyReportGenerator 是一个自动生成日报的程序，它从日历和任务中获取信息，并使用 OpenAI 接口生成日报。日报将以邮件形式发送到指定邮箱。项目由前端和后端组成，所有功能均在后端完成。前端仅提供可视化和日志查看界面。项目代码托管在 GitHub 上，支持一键部署到 Railway 平台和使用 Docker 进行部署。

主要功能
----

1.  使用 CalDAV 协议从日历中获取日程信息。
2.  通过提供的任务 API 从任务中获取所有任务。
3.  使用 OpenAI 接口，根据日历和任务的内容生成日报，使用 prompt 格式。
4.  将生成的日报以邮件形式发送到指定邮箱。

部署
--

### 一键部署到 Railway

点击下面的按钮，根据提示在 Railway 平台上部署此项目。

[![Deploy to Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/your_username/your_repository_name&envs=CALDAV_EMAIL,CALDAV_PASSWORD,CALDAV_URL,TASK_API_URL,OPENAI_API_KEY,EMAIL_CONFIG)


### 使用 Docker 进行部署

1.  克隆仓库：

bash

```bash
git clone https://github.com/yourusername/DailyReportGenerator.git
```

2.  进入项目目录：

bash

```bash
cd DailyReportGenerator
```

3.  创建一个 `.env` 文件，设置环境变量：



```makefile
API_KEY=your_api_key
CALDAV_URL=your_caldav_url
CALDAV_EMAIL= your_caldav_email
CALDAV_PASSWORD= your_caldav_password
TASK_API_URL=your_task_api_url
OPENAI_API_KEY=your_openai_api_key
EMAIL_CONFIG=your_email_config
```

4.  使用 Docker 构建镜像：

`docker-compose up -d`

5.  使用 Docker 运行容器：


```css
docker run -d --name daily-report-generator --env-file .env -p 8080:8080 daily-report-generator
```

现在，应用程序将在 [http://localhost:8080](http://localhost:8080) 上运行。

使用说明
----

1.  使用支持 CalDAV 协议的日历应用创建和管理日程。
2.  通过提供的任务 API 管理任务。
3.  在前端可视化界面上查看生成的日报和日志。
4.  配置邮件接收人，系统会自动将生成的日报发送到指定邮箱。

技术栈
---

*   后端：Node.js, Express
*   前端：React
*   部署：Railway, Docker
*   日历同步：CalDAV
*   任务 API：待提供
*   AI 生成日报：OpenAI
*   邮件发送：Nodemailer
