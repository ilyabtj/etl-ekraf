import paramiko


def upload():
    hostname = "5.189.154.248"
    username = "ilya"
    password = "Passwd093"
    local_path = "ekraf_posts.csv"
    remote_path = "uploads/ekraf_posts.csv"  # ← Diubah ke dalam folder uploads

    transport = paramiko.Transport((hostname, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    sftp.close()
    transport.close()
    print("File sukses diupload ke uploads di SFTP!")


if __name__ == "__main__":
    upload()
