import nltk
nltk.set_proxy('http://www.nltk.org/nltk_data',user=None)
dl=nltk.downloader.Downloader("http://www.nltk.org/nltk_data")
dl.download()
