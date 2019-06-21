import requests

archive_url = "https://iqiyi.com-l-iqiyi.com/20190122/21232_b50410af/1000k/hls/5a56cc8d5a500"

def download_video_series(archive_url):
	# for num in range(1,2004):
	# 	if num<10:
	# 		suff = '000'+str(num)
	# 	if 10<num<100:
	# 		suff = '00'+str(num)
	# 	if 100<num<1000:
	# 		suff = '0'+str(num)
	# 	if 1000<num:
	# 		suff = str(num)

	file_name = '0010'+'.ts'
	link = archive_url + file_name;
	print("Downloading file:%s" % file_name)

	r = requests.get(link, stream=True)

    # download started
	with open('/Users/zhanghao/Desktop/nok/'+file_name, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024 * 1024):
			if chunk:
				f.write(chunk)

	print("%s downloaded!\n" % file_name)

	file_name = '0100'+'.ts'
	link = archive_url + file_name;
	print("Downloading file:%s" % file_name)

	r = requests.get(link, stream=True)

    # download started
	with open('/Users/zhanghao/Desktop/nok/'+file_name, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024 * 1024):
			if chunk:
				f.write(chunk)

	print("%s downloaded!\n" % file_name)



	print("All videos downloaded!")
	return

if __name__ == "__main__":
	download_video_series(archive_url)