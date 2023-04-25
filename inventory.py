class Shoe:

    #code to create a constructor method with parameters, self, country, code, product, cost, quantity.

    def __init__(self, country, code, product, cost, quantity):

        # code to  create attributes within our class Shoe.
        

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    #  code to create a method called get_cost.
    # Return self.cost.

    def get_cost(self):
        return self.cost
    
    #  code to create a method called file_updated with parameter self.
    

    def file_updated(self):
        return f'''{self.country},{self.code},{self.product},{self.cost},{self.quantity}'''

    # code to create a method called get_quantity with parameter self.
    

    def get_quantity(self):
        return self.quantity
    
    #  code to create a method 
    # 

    def __str__(self):
        return (f'''\nCountry:{self.country}
Shoe Code: {self.code}
Shoe Name: {self.product}
Shoe Cost: {self.cost}
Quantity: {self.quantity}\n''')

# code to create an open list with the variable shoe_list


shoe_list = []

# code to create a function called read_shoes_data.
# code to open text file and read from the text file inventory.txt


def read_shoes_data():

    try:

        with open('inventory.txt', 'r') as shoe_list_inventory:
            shoe_list_inside_file = shoe_list_inventory.readlines()
        

        # code to create a for loop. 
        
        
        for line in range(1, len(shoe_list_inside_file)):
                
               

                country, code, product, cost, quantity = shoe_list_inside_file[line].strip('\n').split(',')

              

                shoes = Shoe(country,code,product,float(cost),int(quantity))
                shoe_list.append(shoes)
    
    except FileNotFoundError:
        print('inventory file not found. Please check file name correctly')
      

read_shoes_data()
   
# code to create a method called capture_shoes

def capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity):
    shoes_captured = Shoe(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)
    shoe_list.append(shoes_captured)
   


# code to create a new method
# code to update the quantity 

def update():

    # code to Create a variable called obj_data
    

    obj_data = f'Country,Code,Product,Cost,Quantity'

    # ode to create a for loop to iterate over the shoe list
    
    for shoe in shoe_list:
        obj_data += '\n' + shoe.file_updated()

    # code to open our file and write tothe file 

    with open('inventory.txt', 'w') as shoe_list_inventory:
        shoe_list_inventory.write(obj_data)  

# code to create a function called view_all
# This function will print all details of the shoes


def view_all():
    print(*shoe_list)

# code to create a method called re_stock

def re_stock():

    # code to create a variable called qty(quantity) initialse it to shoe_list index 0
    

    qty = shoe_list[0].quantity
    shoe_index = 0

    

    for i, s in enumerate(shoe_list):
        if s.get_quantity() < qty:
          qty = s.quantity
          shoe_index = i

    

    return shoe_index
  

    
# code to create a method called search_shoe
# Pass the parameter s_code, which is our variable below

def search_shoe(s_code):
   
   # code to create a for loop for our shoe_code in the shoe_list
   # code to create an if statement 
   

    for shoe_code in shoe_list:
        if shoe_code.code == s_code:
            return shoe_code 
    
    return f'The shoe code {s_code} is not found\n'
    

# code to create a method called value_per_item.

def value_per_item():

    #  code to create a for loop to iterate through the shoe_list
  

    for s in shoe_list:
        value = s.cost * s.quantity
        print(f'{s}Value: {value}\n')


# code to create a method called highest_qty().
# code to create a counter called shoe_index initialse it to 0
# code to reate a varible called max_quatity. 
# code Which will then take  shoe_list and the counter and call method.get_quantity.

def highest_qty():
    shoe_index = 0
    max_quantity = shoe_list[shoe_index].get_quantity()

    # code to create a for loop 

    for s, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > max_quantity:
            max_quantity = shoe.get_quantity()
            shoe_index = s



    print(f'Sale Sale Sale, This shoe is on sale {shoe_list[shoe_index]}\n')




user_choice = ''' '''

# code to  create a while loop

while user_choice != 'end stock taking':
    user_choice = input('''\nPlease view below and select
    capture = Capture data about a shoe
    view = This will view all the shoes
    restock = Find shoe that needs to be restocked
    find shoe - This will search for a shoe
    value = Calculate the total value
    sale = Shoe on sale \n''').lower()

    # code when users enters 'capture'
    # code for varaibles shoe_country,shoe_code,shoe_name,shoe_cost,shoe_quantity.
   

    if user_choice == 'capture':

        shoe_country = input('Please enter the country of the shoes ')
        shoe_code = input('Please enter the shoe code ')
        shoe_name = input('Please enter product name ')
        shoe_cost = float(input('Please enter the cost of the shoe ')) 
        shoe_quantity = int(input('Please enter the quantity of the shoes '))
        capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity )

    # code when a user enters 'view'
    # code to call upon the zoom method

    elif user_choice == 'view':
        view_all()

    # code when user enters restock
    # code to create an index for the shoes and assign it to the function re_stock()
    

    elif user_choice == 'restock':
        shoe_index = re_stock()

    # code to  print the shoe with the lowest quantity
    # code to create a new variable to if user would like to restock

        print(f' This is the shoe with the lowest quantity from all your stocking {shoe_list[shoe_index]} ')
        restock_choice = input('''Please see the quantity above and advise if you will be restocking
Please choose:
Yes - for the restock
No -  for not restocking \n''')
        

    # code to create an if statement if user selects yes or no
    # code if user enters yes then the program will ask them to enter new quantity 

        if restock_choice == 'yes':
            shoe_list[shoe_index].quantity = int(input('Please enter new quantity number: \n'))
    
    # code if user enters no quantity will be printed the same
        if restock_choice == 'no':
            print('Quantity will remain the same\n')

        # code to call methods update() and re_stock()

        update()
        re_stock()
       
        
    # code for if the user enters 'find shoe' 
   

    elif user_choice == 'find shoe':
        s_code = input('Please enter the shoe code you looking for: ')
        
        print(f'{search_shoe(s_code)}')
        
    # code for if  the user enters 'value'
    

    elif user_choice == 'value':
        value_per_item()
    
    # We the user enters 'sale'
    # Then we call the highest_qty() function

    elif user_choice == 'sale':
        highest_qty()

    # code for if user enters 'end stock taking' then they will exit the program 
    

    elif user_choice == 'end stock taking':
        print('Thank you')
    
    # code for an else statement to execute if user enters wrong
    

    else:
        print('Please select correctly what you would like to do.')

