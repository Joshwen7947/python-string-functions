search_fun = 'fun'
search_exciting = 'exciting'
search_enter = 'entertainment'
feedback = input('Review the hotel:')
feedback = feedback.lower()
res1 = feedback.find('fun')
res2 = feedback.find('exciting')
res3 = feedback.find('entertainment')
print('Analysis results:', res1, res2, res3)

# 
# 
# 
feedback1 = input('Write a detailed comment:')
feedback2 = input('What you liked:')
feedback3 = input('What you disliked:')
length1 = len(feedback1)
length2 = len(feedback2)
length3 = len(feedback3)
sale_price = (length1 + length2 + length3)*0.1
print('Discount rate:', sale_price)
# 
# 
# 
id_code = 111786426
surname = 'Doe'
tour = 'Nepal'
client_data = str(id_code) + '/' + surname + '/' + tour
print('Client information:',client_data)
# 
# 
# 
feedback = 'What I liked most about Nepal is the amazing people!'
finish = len(feedback)
begin = end - len('amazing people')
review = feedback[start:end]
print(review)