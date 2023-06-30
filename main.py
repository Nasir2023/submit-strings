# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting='Hello, <name>!'):
   return greeting.replace('<name>', name)


greet('Bob')
greet('Bob', "What's up, <name>!")



#Part 2: Force

planets= {'mercury': 3.7,
             'sun': 274,
             'jupiter': 23.1,
             'earth' : 9.8,
             'neptune': 11.0,
             'saturn': 9,
             'uranus': 8.9,
             'venus': 8.9,
             'mars': 3.7,
             'moon': 1.6,
             'pluto': 0.7,
             }
def force(mass, body='earth'):
      for planet, gravity in planets.items():
          if planet== body:
              planet_force= mass * gravity
              print(planet_force)
              return planet_force
     
   

force(5.97*10**24)
force(1898*10**24, body= 'jupiter')

#Part 3: Gravity
g=6.674*10**-11
def pull(m1,m2,d):
     pull=g*((m1*m2)/d**2)
     return(pull)


print(pull(800, 1500, 3))
print(pull(0.1, 9972*10**24, 6.371*10**6))