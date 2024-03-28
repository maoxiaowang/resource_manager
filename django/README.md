# Django后端

## 开发环境搭建
### 1. 进入目录
```shell
$ cd django
```
### 2. 创建虚拟环境
```shell
$ python -m venv venv
```
> Python版本>=3.10

### 3. 激活虚拟环境
#### Windows
```shell
$ .\venv\Scripts\activate.bat
```
#### Linux/MacOS
```shell
$ source venv/bin/activate
```

### 4. 安装依赖库
```shell
$ pip install -r app/requirements.txt
```

### 5. 生成环境变量
```shell
$ python generate_env.py
```

### 6. 运行开发服务
```shell
$ python runserver localhost:8000
```