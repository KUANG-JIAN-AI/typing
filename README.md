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


CREATE TABLE `typ_users` (  
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,  
  `nickname` varchar(255) NOT NULL DEFAULT '' COMMENT '昵称',  
  `created_at` int(10) unsigned NOT NULL DEFAULT 0,  
  `updated_at` int(10) unsigned NOT NULL DEFAULT 0,  
  `deleted_at` int(10) unsigned DEFAULT NULL,  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4  COLLATE=utf8mb4_general_ci;