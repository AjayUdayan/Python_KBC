questions = ["What is the capital of telangana?","Which is the smallest state in India?","Which is the most populated country in the world?","What is the capital of Himachal Pradesh?","Raipur is the capital of which state of India?"]

first_options = ["Jaipur","Maharastra", "USA","Chandigarh","Chhattisgarh"]
second_options = ["Thiruvananthapuram","Goa","Pakistan","Dharamshala","uttrakhand"]
third_options = ["Chennai","Bihar","China","Shimla","Harayana"]
fourth_options = ["Hydarabad","Rajesthan","India","Delhi","Asam"]
all_options = ["first_options","second_options","third_options","fourth_options"]
ans_key  = [3,1,2,0]  

# part 1
print questions[1]
# part 2
print first_options[0]
print second_options[0]
print third_options[0]
print fourth_options[0]
# part 3
i = 2
while i < len(questions):
	print first_options[i]
	print second_options[i]
	print third_options[i]
	print fourth_options[i]
	break
	i = i + 1

# part 4
questions.pop()
first_options.pop()
second_options.pop()
third_options.pop()
fourth_options.pop() 
# part 5
print len(questions)
# part 6
questions.append("Raipur is the capital of which state of India?")
first_options.append("Chhattisgarh")
second_options.append("uttrakhand")
third_options.append("Harayana")
fourth_options.append("Asam")
# part 7
option2 = second_options[1] 
print option2
# part 8
if option2 in third_options:
    print "option2 third_options me hai."
else:
    print "option2 third_options me nahi hai."

