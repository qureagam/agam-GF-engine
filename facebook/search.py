from googlesearch import search


def searching(query):
      tick  = []
      results = [ i for i in search(query,num_results=5)]

      return results

