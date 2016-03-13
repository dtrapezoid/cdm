import urllib2
from base64 import b64encode
import os.path

class Context(object):
    root = None
    session = None
    cache_dir = None
    dataset = None
    keyspace = None

    def __init__(self, root, dataset, session, cache_dir):
        self.root = root
        self.dataset = dataset
        self.session = session
        # add trailing slash
        if not cache_dir.endswith("/"):
            cache_dir = cache_dir + "/"

        self.cache_dir = cache_dir
        if not os.path.exists(self.cache_dir):
            raise Exception("Cache dir does not exist")


    def download(self, url):
        """
        downloads a single file to the cache
        returns a file pointer
        auto caches download

        :param url:
        :param cache:
        :return:
        """
        encoded = b64encode(url)
        cache = self.cache_dir + encoded

        self.feedback("Downloading {}".format(url))
        if not os.path.exists(cache):
            with open(cache, 'w') as fp:
                data = urllib2.urlopen(url)
                fp.write(data.read())
            print "Download finished"
        else:
            self.feedback("Found in cache, skipping")

        fp = open(cache, 'r')
        return fp


    def clean_cache(self):
        """
        removes all data from this cache directory
        :return: None
        """
        for file in os.listdir(self.cache_dir):
            print os.remove(self.cache_dir + file)


    def feedback(self, msg):
        print msg


    def install(self):
        pass

