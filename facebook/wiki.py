import wikipedia

def wiks(v):
    try:
        ans = wikipedia.summary(str(v))
        return ans
    except Exception as e:
        return "Could not find the result"

