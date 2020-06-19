class CoffeeMachine:
    status = 'on'
    actions = ['buy', 'fill', 'take', 'remaining', 'exit']

    action_buy_msg = 'What do you want to buy? ' \
                     '1 - espresso, ' \
                     '2 - latte, ' \
                     '3 - cappuccino, ' \
                     'back - to main menu:'

    def __init__(self):
        self.drinks = {
            'espresso': {
                'water': 250,
                'milk': 0,
                'coffee': 16,
                'cups': 1,
                'cost': 4
            },
            'latte': {
                'water': 350,
                'milk': 75,
                'coffee': 20,
                'cups': 1,
                'cost': 7
            },
            'cappuccino': {
                'water': 200,
                'milk': 100,
                'coffee': 12,
                'cups': 1,
                'cost': 6
            }
        }
        self.elements = {
            'water': {
                'name': 'water',
                'measure': 'ml',
                'qty': 400
            },
            'milk': {
                'name': 'milk',
                'measure': 'ml',
                'qty': 540
            },
            'coffee': {
                'name': 'coffee beans',
                'measure': 'gr',
                'qty': 120
            },
            'cups': {
                'name': 'disposable cups of coffee',
                'measure': '',
                'qty': 9
            }
        }
        self.total = 550

        self.print_action()

        while self.status == 'on':
            self.handle_action(input())

    def print_stats(self):
        print('The coffee machine has:')
        for element in self.elements:
            print(f"{self.elements[element]['qty']} of {self.elements[element]['name']}")
        print(f'${self.total} of money')  # if total else total, 'of money')

    def print_action(self):
        print('Write action (' + ', '.join(self.actions) + '):')

    def handle_action(self, what):
        if what == 'exit':
            self.status = 'off'
        elif what == 'buy':
            print(self.action_buy_msg)

            pick = input()
            if pick == 'back':
                return self.print_action()

            self.process(int(pick))
            print()
            self.print_action()
            # self.handle_buy()

        elif what == 'fill':
            self.handle_fill()
        elif what == 'remaining':
            self.handle_remaining()
        elif what == 'take':
            self.handle_take()

    def process(self, pick):
        drink_picked = list(self.drinks)[pick-1]  # e.g. 'cappuccino'
        drink_elements = self.drinks[drink_picked].copy()  # cappuccino dict
        drink_cost = drink_elements.pop('cost')

        # check if we have enough qty before operation
        for element in drink_elements:
            if self.elements[element]['qty'] < drink_elements[element]:
                print(f"Sorry, not enough {self.elements[element]['name']}!")
                return False

        # subtract quantities from total
        for element in drink_elements:
            self.elements[element]['qty'] -= drink_elements[element]

        # self-evident
        self.total += drink_cost
        print('I have enough resources, making you a coffee!')
        return True

    def handle_fill(self):
        for element in self.elements:
            measure = ''
            if self.elements[element]['measure']:
                measure = f"{self.elements[element]['measure']} of "
            name = self.elements[element]['name']

            print(f"Write how many {measure + name} do you want to add:")
            self.elements[element]['qty'] += int(input())

        print()
        self.print_action()

    def handle_remaining(self):
        print()
        self.print_stats()
        print()
        self.print_action()

    def handle_take(self):
        print(f'I gave you ${self.total}')
        print()
        self.print_action()
        self.total = 0


CoffeeMachine()

