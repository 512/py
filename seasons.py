tc = 0
dc = 0
for p1 in range(4):
  for p2 in range(4):
    for p3 in range(4):
      for p4 in range(4):
        tc += 1
        l = [p1,p2,p3,p4]
        if len(set(l)) == 4:
          dc += 1
          a = [str(i) for i in l]
          print(",".join(a))
print("%s/%s" % (dc,tc))