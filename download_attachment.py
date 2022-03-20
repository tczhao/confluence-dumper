import pickle
from multiprocessing.pool import ThreadPool as Pool
import utils


with open('file.pkl', 'rb') as file:
    myvar = pickle.load(file)
    print(len(myvar["GLOBAL_absolute_download_url"]))

def download(absolute_download_url, downloaded_file_path, auth, headers, verify_peer_certificate, proxies):
    try:
        utils.http_download_binary_file(absolute_download_url, downloaded_file_path, auth, headers, verify_peer_certificate, proxies)
    except utils.ConfluenceException as e:
        if error_output:
            error_print('%sERROR: %s' % ('\t'*(depth+2), e))
        else:
            print('%sWARNING: %s' % ('\t'*(depth+2), e))

with Pool(processes=1000) as pool:
    pool.starmap(utils.http_download_binary_file, zip(
        myvar["GLOBAL_absolute_download_url"],
        myvar["GLOBAL_downloaded_file_path"],
        myvar["GLOBAL_auth"],
        myvar["GLOBAL_headers"],
        myvar["GLOBAL_verify_peer_certificate"],
        myvar["GLOBAL_proxies"]
    ))