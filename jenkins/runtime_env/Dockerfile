FROM tomcat

RUN apt update && apt install  openssh-server sudo -y

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 ssh_user

RUN  echo 'ssh_user:test' | chpasswd

RUN  echo 'ssh_user ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
