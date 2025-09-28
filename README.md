创建虚拟环境  
py -3 -m venv .venv

进入虚拟环境  
.venv\Scripts\activate

安装 Flask  
pip install Flask

安装 mysql 驱动  
pip install Flask Flask-SQLAlchemy pymysql

加载静态文件，static/js/index.js  
`<script src="{{ url_for('static', filename='js/index.js') }}"></script>`
