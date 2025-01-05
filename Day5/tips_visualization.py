import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

print(tips.head())
print(tips.shape)

plt.figure(figsize=(11,8))


#1.Proportion of Female And Male ustomers

plt.subplot(2,3,1)
female_count = tips[tips["sex"]=="Female"].count().iloc[0]
print("females:",female_count)
male_count = tips[tips["sex"]=="Male"].count().iloc[0]
print("males:",male_count)

plt.pie([male_count,female_count],labels=["Male", "Female"], autopct='%.1f%%')
plt.title("Male & Female customer Proportion")

#2.most used table size
plt.subplot(2,3,2)
sns.countplot(data=tips,y=tips["size"],hue=tips["size"],legend=False, palette='pastel')
plt.title("Frequency of table sizes")
plt.xlabel("Customers")
plt.ylabel("Table Size")

#3.Relation between table tip and total bill
plt.subplot(2,3,4)
sns.scatterplot(data=tips,x="tip",y="total_bill", alpha=0.8)
plt.title("Tip & Total Bill correlation ")

#4 income
plt.subplot(2,3,5)
sun_abg_bill = tips[tips["day"]=="Sun"]["total_bill"].mean()
print(sun_abg_bill)
sat_avg_bill = tips[tips["day"]=="Sat"]["total_bill"].mean()
print(sat_avg_bill)
fri_avg_bill = tips[tips["day"]=="Fri"]["total_bill"].mean()
print(fri_avg_bill)
Thur_avg_bill = tips[tips["day"]=="Thur"]["total_bill"].mean()
print(Thur_avg_bill)
plt.bar(["Sun","Thur","Fri","Sat"],[sun_abg_bill,Thur_avg_bill,fri_avg_bill,sat_avg_bill], color="skyblue")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill per Day")

#Male & Female average tip Comparision
plt.subplot(2,3,3)
male_tip=tips[tips["sex"]=="Male"]["tip"].mean()
female_tip=tips[tips["sex"]=="Female"]["tip"].mean()
print(male_tip)
print(female_tip)
plt.bar(["Male tip", "Female tip"],[male_tip,female_tip], color="purple")
plt.title("Average Tip by Male & Female customers")

#Smoker & non Smoker tip
plt.subplot(2,3,6)
sns.histplot(data=tips,x="tip",hue="smoker", bins=10, kde=True,palette="Set1")
plt.ylabel("Number of Customers")

plt.suptitle("Visualization of tips dataset", color="purple")
plt.tight_layout()
plt.show()
