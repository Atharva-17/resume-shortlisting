import pandas as pd
def calculate(data , skills):
  ans = []
  for i in data.index:
    high = 0
    mid = 0
    low = 0
    high_skills = data["high_priority_skills"][i].split(",")
    mid_skills = data["medium_priority_skills"][i].split(",")
    low_skills = data["high_priority_skills"][i].split(",")
    for skill in skills:
      if skill in high_skills:
        high += 1
      elif skill in mid_skills:
        mid += 1
      elif skill in low_skills:
        low += 1
    score = 3*high + 2 * mid + low
    ans.append([data["position"][i] , high , mid , low , score])
  return ans