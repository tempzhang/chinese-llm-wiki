---
title: "Docker 速查"
type: "concept"
status: "active"
tags: ["Docker", "容器", "自建服务", "NAS", "运维"]
created: "2026-05-29"
updated: "2026-05-29"
sources: []
related:
  - "NAS与自建服务"
  - "建站"
---

# 🐳 Docker 速查

Docker 是容器化部署的事实标准，NAS 和服务器上几乎所有自建服务都通过 Docker 运行。

## 一句话定义

Docker 把应用及其依赖打包成轻量容器，实现「一次构建，到处运行」。

## 核心概念

- **镜像（Image）**：应用的只读模板
- **容器（Container）**：镜像的运行实例
- **Docker Compose**：多容器编排，一个 YAML 定义整个应用栈
- **Docker Hub**：公共镜像仓库

## 常用管理工具

- **Portainer** — Web 可视化管理界面
- **Dockge** — 轻量 Compose 管理器

## 常用 Compose 服务

- WordPress + MySQL 建站
- Jellyfin + qBittorrent + Jellyseerr 影音套件
- Nginx Proxy Manager 反向代理
- AList 网盘聚合
- Home Assistant 智能家居

## 常用命令

```bash
docker ps              # 查看运行中的容器
docker-compose up -d   # 后台启动 Compose 服务栈
docker-compose down    # 停止并删除 Compose 服务栈
docker logs -f <容器>  # 查看容器日志
docker exec -it <容器> sh  # 进入容器 shell
```

## 关联页面

- [[NAS 与自建服务]] — Docker 在 NAS 上的应用
- [[建站]] — Docker 部署网站
