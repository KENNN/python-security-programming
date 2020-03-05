FROM ubuntu:18.04
MAINTAINER kanta <contact.kantamori@gmail.com>

RUN echo 'root:root' | chpasswd && \
    useradd --create-home --shell /bin/bash pysec101 && \
    echo 'pysec101:pysec101' | chpasswd && \
    usermod -aG sudo pysec101 && \
    sed -i 's|http://archive.ubuntu.com/ubuntu/|http://ftp.iij.ad.jp/pub/linux/ubuntu/archive/|g' /etc/apt/sources.list && \
    apt -y update && apt install -y software-properties-common && \
    add-apt-repository -y ppa:kelleyk/emacs && \
    apt -y update && apt install -y \
    auditd \
    bsdmainutils \
    dnsmasq \ 
    emacs26 \
    git \
    hostapd \
    iptables \
    isc-dhcp-server \
    nano \
    net-tools \
    network-manager \
    python3.6 \
    python3-pip \
    sqlite3 \
    sudo \
    tcpdump \
    traceroute \
    usbutils \
    vim \
    wget \
    wireless-tools && \
    ln -s /usr/bin/python3.6 /usr/bin/python && \
    pip3 install bottle numpy requests scapy && \
    echo 'set number\nset encoding=utf-8' >> /etc/vim/vimrc && \
    touch /home/pysec101/.bashrc && \
    git clone https://gitlab.com/pysec101/pysec101.git && \
    git clone https://github.com/fuzzdb-project/fuzzdb.git && \
    git clone https://github.com/oblique/create_ap.git && \
    mv /pysec101 /home/programs && \
    mv /fuzzdb /home/programs/chap6 && \
    gcc /home/programs/chap6/vuln.c -o /home/programs/chap6/a.out && \
    chown -R pysec101:pysec101 /home/programs/ && \
    make install -C /create_ap

WORKDIR /home/pysec101
