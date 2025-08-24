#distribute load evenly, and add extra load in first index, return distributed load in list:
def load_distribution(request : int, instance : int):
baseload = request//instance
extra = request % instance

distributed_req = []

for i in range(instance):
  if extra > i:
    distributed_req.append( baseload + 1 )
  else:
    distributed_req.append(baseload)

return (distributed_req)
