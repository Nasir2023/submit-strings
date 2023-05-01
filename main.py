# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1='Ruud Gullit'
player2='Marco van Basten'
goal_0= 32
goal_1= 54
scorers= player1 + ' ' + str(goal_0) +', '  + player2 +' '+ str( goal_1)
print(scorers)
report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'
print(report)
#part 2
player= "Ruud Gullit"
spatie= player.find(' ')
first_name= player[:spatie]
last_name= player[spatie:]
last_name_len= len(last_name)
name_short=player [0:1] +'.' + last_name
print(name_short)
print(first_name)
chant= (first_name + '!')* len(first_name)
chantzonderspatie= chant[0:-1]
good_chant=(chant !=' ')
print(chant)
print(chantzonderspatie)
print(last_name)
print(name_short)
print(good_chant)
print(last_name_len)