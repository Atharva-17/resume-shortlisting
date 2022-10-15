import pandas as pd

def roleNames():
  roles_dataframe = pd.read_csv("skills.csv")
  ans = []
  for i in range(len(roles_dataframe)):
    ans.append(roles_dataframe.loc[i,"role_name"])
  return ans
def calculate(skills):
  ans = []
  skills_dataframe = pd.read_csv("skills.csv")
  for i in range(len(skills_dataframe)):
    #print("HI")
    high = 0
    mid = 0
    low = 0
    high_skills = skills_dataframe.loc[i,"high_priority_skills"].split(",")
    mid_skills = skills_dataframe.loc[i,"mid_priority_skills"].split(",")
    low_skills = skills_dataframe.loc[i,"low_priority_skills"].split(",")
    for skill in skills:
      if skill in high_skills:
        high += 1
      elif skill in mid_skills:
        mid += 1
      elif skill in low_skills:
        low += 1
    score = 3*high + 2 * mid + low
    ans.append(score)
  return ans