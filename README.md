# ETL Ekraf

Script sederhana untuk Extract, Transform, dan Load data dari API ekraf.go.id ke CSV lalu upload ke SFTP.

## Cara pakai

1. `python extract.py` — Ambil data dari API ke raw.json
2. `python transform.py` — Transform raw.json ke ekraf_posts.csv
3. `python load.py` — Upload CSV ke SFTP server
