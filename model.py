import pandas as pd
from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel 
data = pd.read_csv("anime.csv")
data.genre.fillna(" ", inplace = True)
tfid = TfidfVectorizer()
vector = tfid.fit_transform(data.genre)
index= pd.Series(data = data.index, index = data.name)
def anime_rec(name):
  ind_num = index[name]
  dis = linear_kernel(vector[ind_num],vector)
  val = list((dis))
  d = pd.DataFrame(val)
  d = d.transpose()
  d.columns = ["name"]
  d = d.sort_values(by="name",ascending=False)
  l = []
  gen = []
  rat = []
  for i in range(0,10):
    l.append(data.name[d.index[i]])
    gen.append(data.genre[d.index[i]])
    rat.append(data.rating[d.index[i]])
  return l ,gen ,rat


def checker(name):
  if name in index:
    return "1"

def lister():
  return data.name, data.genre, data.rating
  