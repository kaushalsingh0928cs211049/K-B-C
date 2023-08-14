#Kaushal
print("_______________________Welcome to Kaun Banega Crorepati_______________________\n\n ")
#QUESTIONS
que=["Question1: Which actor's son is Tiger who made his debut as a hero in the film 'Heropanti'?",
  "Question2: Who among the following is one of the main characters of Ramayana who also appears in Mahabharata?",
  "Question3: What is the name of the campaign launched by the Government of India to promote the use of toilets?",
  "Question4: Which city is known as Pink City in India?",
   "Question5: How many states are there in India?"]
#OPTIONS
opt=[[" Sunil Shetty",   
" Jackie Shroff", 
" Sunny Deol",
" Anil Kapoor"],
[" Hanuman",
" Vedvyas", 
" Dasaratha",
" Duryodhana"],
[ "Curtain is curtain ",
" door closed ",
" Open minded ",
"you don't see us"],
["Banglore",
" Maysore ",
" Jaipur ",
" Kochi"],
[" 28 ",
" 29 ",
" 31",
" 31"]]
#ANSWER
ans=[2,1,2,3,2]
#REWARD
reward=[1000,3000,5000,7000,9000]
def fifty(i,money):
        a=opt[i][ans[i]-1]
        print(opt[i].index(a)+1,a)
        import random
        l=list(opt[i])
        l.remove(a)
        b=random.choice(l)
        print(opt[i].index(b)+1,b)
        c=int(input("Choose Correct Option: "))
        if c==ans[i]:
            money=money+reward[i]
            print(" Yeah you won :",reward[i],"Rupees.\n")
            return money 
        else:
            print("You Choose Incorrect option.\n")
            print( "Correct answer is: ",ans[i])
            return 0              
n=5
money=0
for i in range(n):
    print(que[i],"\n")
    for j in range(4):
        print(j+1,opt[i][j],"\n")
    B=int(input("Choose Correct Option or press 5 for lifeline: "))
    if ans[i]==B:
        money=money+reward[i]
        print(" Yeah you won :",reward[i],"Rupees.\n")
    elif B==5:
        M= fifty(i,money)
        if M==0:
            break
        else:
            money=money+M
    else:
        print("You Choose Incorrect option.\n")
        print( "Correct answer is: ",ans[i])
        break
print("Match Over\n")
print("Your Total Reward :",money)