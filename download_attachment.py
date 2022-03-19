import pickle
from pathos.multiprocessing import ThreadingPool as Pool
import utils


with open('file.pkl', 'rb') as file:
    myvar = pickle.load(file)
    #print(myvar)
  
Pool(processes=100).map(utils.http_download_binary_file,
        myvar["GLOBAL_absolute_download_url"],
        myvar["GLOBAL_downloaded_file_path"],
        myvar["GLOBAL_auth"],
        myvar["GLOBAL_headers"],
        myvar["GLOBAL_verify_peer_certificate"],
        myvar["GLOBAL_proxies"]
    )