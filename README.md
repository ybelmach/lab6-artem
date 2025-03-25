# lab6-artem

# Скачивание репозитория

1. Создаёшь папку, заходишь в неё через консоль. Например (создаёт папку и заходит в неё через консоль, создаёт папку static для проекта):
```bash
  mkdir lab6; cd ./lab6; mkdir static
```
# Создание гит репозитория и скачивание с github

```bash
    git init; git pull https://github.com/ybelmach/lab6-artem.git main
```

# Установка Docker на пк (Ubuntu)

Код с доки:
1. Set up Docker's apt repository
```bash
    # Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. Set up Docker's apt repository

```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the installation is successful by running the hello-world image (если запускается, то всё ок)

```bash
    sudo docker run hello-world
```

# Запуск проекта

1. Установка Make (для использования Makefile):

```bash
    sudo apt update && sudo apt install make
```

2. Создаёшь в проекте файл .env и копируешь туда содержимое файла .env.example (можно одной командой)

```bash
    cp .env.example .env
```

3. Запуск проекта:

```bash
    make run
```

# Посмотреть проект

Заходишь в браузере на http://127.0.0.1:8000/

# Остановка проекта

Сразу Ctrl+C, чтобы остановить процесс, потом:

```bash
make down
```
