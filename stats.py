def get_num_words(text: str)->int:
    return len(text.split())

def character_count(text: str)-> dict[str, int]:
   d = dict()
   text = text.lower()
   for c in text:
       if c not in d:
           d[c] = 1
       else:
          d[c] +=1
    
   return d
