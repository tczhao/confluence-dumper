import pickle
from multiprocessing.pool import ThreadPool as Pool
import utils


with open('file.pkl', 'rb') as file:
    myvar = pickle.load(file)
    print(len(myvar["GLOBAL_absolute_download_url"]))

with Pool(processes=1000) as pool:
    pool.starmap(utils.http_download_binary_file, zip(
        myvar["GLOBAL_absolute_download_url"],
        myvar["GLOBAL_downloaded_file_path"],
        myvar["GLOBAL_auth"],
        myvar["GLOBAL_headers"],
        myvar["GLOBAL_verify_peer_certificate"],
        myvar["GLOBAL_proxies"]
    ))