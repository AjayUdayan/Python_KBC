questions = ["What is the capital of telangana?","Which is the smallest state in India?","Which is the most populated country in the world?","What is the capital of Himachal Pradesh?","Raipur is the capital of which state of India?"]

first_options = ["Jaipur","Maharastra", "USA","Chandigarh","Chhattisgarh"]
second_options = ["Thiruvananthapuram","Goa","Pakistan","Dharamshala","uttrakhand"]
third_options = ["Chennai","Bihar","China","Shimla","Harayana"]
fourth_options = ["Hydarabad","Rajesthan","India","Delhi","Asam"]
all_options = ["first_options","second_options","third_options","fourth_options"]
ans_key = [4,2,3,2,1]
index = 0 
money = 0
while index < len(questions):
	print " Q-" + str(1 + index)+" : " + questions[index]
	print "  1) :" + first_options[index]
	print "  2) :" + second_options[index]
	print "  3) :" + third_options[index]
	print "  4) :" + fourth_options[index]
	user_input = int(raw_input("Enter your Answer : " ))
	if user_input == ans_key[index]:
		money = money + 1000000
		print "SAHI JAVAB !!! :) "
	else:
		print "GALAT JAVAB (BETTER LUCK NEXT TIME!!) : "
		break		
	index = index + 1
print "KHELA KHATAM"
print "AAP JEET GAYE HAI " + str(money) + " RUPEE NAGAD!!!!:) "