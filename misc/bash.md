# Bash 指令总结

## 常用filesystem

### 压缩/打包

**zip**

```bash
# zip
zip -r filename.zip /path/to/directory

# unzip
unzip filename.zip #to current directory
unzip filename.zip -d /path/to/directory #to specified directory
```

**tar**
```bash
 # extract
 tar -xvzf XXX.tar.gz .

 # compress
 tar -cvzf FILE XXX.tar.gz
```

### 查看folder大小

[ref](https://unix.stackexchange.com/questions/67806/how-to-recursively-find-the-amount-stored-in-directory)

```bash
du -sh /path/to/directory
```



## ssh

```bash
# connect
ssh -i ~/.ssh/id_rsa_gcp jinyijia@34.125.200.143

# generate ssh key
ssh-keygen -t rsa -f ~/.ssh/[KEY_FILENAME] -C [USERNAME]

# scp
scp -i ~/.ssh/id_rsa_gcp jinyijia@34.125.200.143:/server/path/to/directory ./local/path/to/directory
```



## git

[note](https://lfool.github.io/LFool-Notes/git/Git%E6%80%BB%E7%BB%93.html)





## gcp

```bash
# start instance
gcloud compute instances start instance-1

# stop instance
gcloud compute instances stop instance-1

# list all instances
gcloud compute instances list
```



## jupyter

**autoreload**

```python
%load_ext autoreload
%autoreload 2
```

