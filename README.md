# Git 版本管理实践报告（基于 Linux 系统加 VSCode）

## 学习资料来源以及相关链接

- [Git 官方文档](https://git-scm.com/docs)
- [Github git 基础教程](https://guides.github.com/activities/using-git-with-github/)
- [AI 交互]

## 实践流程

### Git 环境配置与本地仓库创建

1. **安装 Git**
   - 在 Linux 终端中使用 `sudo apt install git` 安装 Git

2. **配置 Git 身份信息**
   - 在 Linux 终端中使用 `git config --global user.name "user_name"` 配置用户名称
   - 在 Linux 终端中使用 `git config --global user.email "user_email"` 配置用户邮箱

3. **创建本地仓库**
   - 在 Linux 终端中使用 `mkdir` 命令创建文件夹，进入该文件夹，执行 `git init` 创建本地仓库

### 远程仓库创建与关联

1. **注册并创建远程仓库**
   - 在 Github 上注册账号并创建新仓库
   - 复制远程仓库的 SSH 地址（不是 HTTPS 地址，后续可以知道原因）

2. **关联本地仓库与远程仓库**
   - 修改连接端口为 443：执行 `git remote set-url origin ssh://git@github.com:443/user_name/repository_name.git`，也可以修改 `~/.ssh/config` 文件避免每次连接都修改端口
   - 实现 Git SSH 连接：
     - 生成 SSH 密钥对：执行 `ssh-keygen -t ed25519 -C "user_email"` 生成密钥对，生成后密码可输可不输
     - 启用 SSH 代理：执行 `ssh-add ~/.ssh/id_ed25519` 将密钥添加到 SSH 代理中
     - 查看并复制公钥到 Github：执行 `cat ~/.ssh/id_ed25519.pub` 查看公钥，复制公钥到 Github 账号的 SSH keys 中，最后添加即可
     - 测试连接：执行 `ssh -T git@github.com` 测试连接，如果返回 "Hi, user_name! You've successfully authenticated, but GitHub does not provide shell access." 则连接成功
   - 关联文件夹和远程仓库：执行 `git remote add origin "先前复制的 SSH 地址"`，可以执行 `git remote -v` 查看关联结果

3. **推送本地到远程仓库**
   - 使用 VSCode 进行文件编写，在左栏添加说明点击推送即可
   - 执行 `git push -u origin "branch_name"` 推送本地到远程仓库，不知道 branch_name 可以执行 `git branch` 查看
   - 返回 Github 刷新页面，即可看到推送的文件

## 本次实践提交主要内容

- 第 1~3 次提交主要是创建简单 Python 文件，用于练习 Git 的基本操作
- 第 4 次提交主要是添加 README.md 文件，用于记录实践过程

## 实践遇到的问题以及解决方法

1. **端口 22 无法连接到 github.com**：修改连接端口为 443，具体操作参照上面"关联本地仓库与远程仓库"中的修改连接端口为 443

2. **关联超时**：使用 SSH 代理，具体操作参照上面"关联本地仓库与远程仓库"中的启用 SSH 代理

3. **仓库的 HTTPS 地址关联失败**：改用 SSH 地址关联即可

## Git 实践心得

通过本次实践，我掌握了 Git 的基本操作，包括创建本地仓库、关联远程仓库、推送本地到远程仓库等。体会到了 Git 在团队合作中的重要性，以及在项目管理中的优势。学习到了在使用 Git 时需要注意的事项，比如修改连接端口、使用 SSH 代理、关联 HTTPS 地址等。