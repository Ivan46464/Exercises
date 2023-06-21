
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("2018.csv")
# print(df.loc[1])

# Calculate the average score for countries with a happiness score above 7
above_7_df = df[df['Score'] > 7]
total_score = above_7_df['Score'].sum()
count = above_7_df.shape[0]
average_score_above_7 = total_score / count
print(f"Average Score for Countries with a Happiness Score above 7: {average_score_above_7:.2f}.")
freedom_df = df['Freedom to make life choices']
total_Freedom_to_make_life_choices = freedom_df.sum()
count1 = freedom_df.shape[0]
average_total_Freedom_to_make_life_choices = total_Freedom_to_make_life_choices / count1
print(f"Average score for Freedom to make life choices: {average_total_Freedom_to_make_life_choices:.2f}.")
total_Freedom_to_make_life_choices1 = above_7_df['Freedom to make life choices'].sum()
average_total_Freedom_to_make_life_choices1 = total_Freedom_to_make_life_choices1/count
print(f"Average score for Freedom to make life choices in Countries with a Happiness Score above 7: {average_total_Freedom_to_make_life_choices1:.2f}.")
corruption = df['Perceptions of corruption']
total_corruption = corruption.sum()
count2 = corruption.shape[0]
average_corruption = total_corruption/count2
print(f"Average score for Perceptions of corruption: {average_corruption:.2f}.")
total_corruption1 = above_7_df['Perceptions of corruption'].sum()
average_corruption1 = total_corruption1/count
print(f"Average score for Perceptions of corruption with a Happiness Score above 7: {average_corruption1:.2f}.")
gdp_per_capita = df['GDP per capita']
total_gdp = gdp_per_capita.sum()
count3 = gdp_per_capita.shape[0]
average_gdp = total_gdp / count3
print(f"Average GDP per capita: {average_gdp:.2f}.")
gdp_per_capita_above_7 = above_7_df['GDP per capita']
total_gdp_above_7 = gdp_per_capita_above_7.sum()
average_gdp_above_7 = total_gdp_above_7 / count
print(f"Average GDP per capita with a Happiness Score above 7: {average_gdp_above_7:.2f}.")
healthy_life_expectancy = df['Healthy life expectancy']
total_life_expectancy = healthy_life_expectancy.sum()
count4 = healthy_life_expectancy.shape[0]
average_life_expectancy = total_life_expectancy / count4
print(f"Average Healthy life expectancy: {average_life_expectancy:.2f}.")
healthy_life_expectancy_above_7 = above_7_df['Healthy life expectancy']
total_life_expectancy_above_7 = healthy_life_expectancy_above_7.sum()
average_life_expectancy_above_7 = total_life_expectancy_above_7 / count
print(f"Average Healthy life expectancy with a Happiness Score above 7: {average_life_expectancy_above_7:.2f}.")
social_support = df['Social support']
total_social_support = social_support.sum()
count5 = social_support.shape[0]
average_social_support = total_social_support / count5
print(f"Average Social support: {average_social_support:.2f}.")
social_support_above_7 = above_7_df['Social support']
total_social_support_above_7 = social_support_above_7.sum()
average_social_support_above_7 = total_social_support_above_7 / count
print(f"Average Social support with a Happiness Score above 7: {average_social_support_above_7:.2f}.")
print("In conclusion countries with bigger happiness score have more freedom to make life choices as well.")
print("But as you can see some of the countries which are the happiest are also with the highest Perceptions of "
      "corruption in the world. ")

# print(df.to_string())

plt.subplot(3, 1, 1)

list1 = []
list2 = []
for x in range(0, len(df['Score'].values)):
    if df['Score'].values[x] > 7:
        list1.append(int(df['Score'].values[x]))
        list2.append(str(df['Country or region'].values[x]))
# print(df['Score'].values)
x_coordinates = np.array(list2)
y_coordinates = np.array(list1)
plt.title("Most happy countries in the world")
plt.ylabel("Happiness score above 7")
plt.xlabel("Country")
plt.bar(x_coordinates, y_coordinates, color='green')
plt.text(0.5, 0.9, f"Average Score for Countries with a Happiness Score above 7: {average_score_above_7:.2f}",
         transform=plt.gca().transAxes, ha='center')
plt.subplot(3, 1, 2)
list3 = []
list4 = []
for x in range(0, len(df['Freedom to make life choices'].values)):
    # if df['Freedom to make life choices'].values[x] > 0.680:
    #     list3.append(df['Freedom to make life choices'].values[x])
    #     list4.append(str(df['Country or region'].values[x]))
    if df['Score'].values[x] > 7:
        list3.append(df['Perceptions of corruption'].values[x])
        list4.append(str(df['Country or region'].values[x]))
x_coordina = np.array(list4)
y_coordina = np.array(list3)
plt.title("Country with the most freedom")
plt.pie(y_coordina, labels=x_coordina)
plt.subplot(3, 1, 3)
list6 = []
list5 = []
for x in range(0, len(df['Freedom to make life choices'].values)):
    # if df['Perceptions of corruption'].values[x] > 0.34:
    #     list5.append(df['Perceptions of corruption'].values[x])
    #     list6.append(str(df['Country or region'].values[x]))
    if df['Score'].values[x] > 7:
        list5.append(df['Perceptions of corruption'].values[x])
        list6.append(str(df['Country or region'].values[x]))
x_coordinat = np.array(list6)
y_coordinat = np.array(list5)
plt.title("Countries which are with happiness score above 7 - perception of corruption")
plt.xlabel('Country')
plt.ylabel('Perceptions of corruption')
plt.bar(x_coordinat, y_coordinat)
plt.text(0.5, 0.9, f"Average Perceptions of corruption for Countries with a Happiness Score above 7: {average_corruption1:.2f}",
         transform=plt.gca().transAxes, ha='center')
plt.tight_layout()
plt.show()