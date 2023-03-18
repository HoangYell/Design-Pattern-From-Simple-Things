class ATMState:
    def __init__(self, atm_machine):
        self.atm_machine = atm_machine

    def insert_card(self):
        pass

    def eject_card(self):
        pass

    def enter_pin(self, pin):
        pass

    def request_cash(self):
        pass


class NoCardState(ATMState):
    def insert_card(self):
        print("🏧 Card inserted")
        self.atm_machine.state = self.atm_machine.has_card_state

    def eject_card(self):
        print("🏧 No card to eject")

    def enter_pin(self, pin):
        print("🏧 Insert a card first")

    def request_cash(self):
        print("🏧 Insert a card first")


class HasCardState(ATMState):
    def insert_card(self):
        print("🏧 You cannot insert more than one card")

    def eject_card(self):
        print("🏧 Card ejected")
        self.atm_machine.state = self.atm_machine.no_card_state

    def enter_pin(self, pin):
        if pin:
            print(f"🏧 Pin entered correctly: {pin}")
            self.atm_machine.state = self.atm_machine.has_correct_pin_state
        else:
            print("🏧 Wrong pin")
            self.atm_machine.wrong_pin_count += 1
            if self.atm_machine.wrong_pin_count >= 2:
                print("🏧 Too many wrong attempts")
                self.eject_card()

    def request_cash(self):
        print("🏧 Please enter your pin first")


class HasCorrectPinState(ATMState):
    def insert_card(self):
        print("🏧 You cannot insert more than one card")

    def eject_card(self):
        print("🏧 Card ejected\n")
        self.atm_machine.state = self.atm_machine.no_card_state

    def enter_pin(self, pin):
        print("🏧 You already entered your pin")

    def request_cash(self):
        print("🏧 Cash dispensed 💵")


class ATMMachine:
    def __init__(self):
        self.no_card_state = NoCardState(self)
        self.has_card_state = HasCardState(self)
        self.has_correct_pin_state = HasCorrectPinState(self)

        self.state = self.no_card_state
        self.wrong_pin_count = 0

    def insert_card(self):
        print("🤑 Insert card")
        self.state.insert_card()

    def eject_card(self):
        print("🤑 Eject card")
        self.state.eject_card()

    def enter_pin(self, pin):
        print("🤑 Enter pin")
        self.state.enter_pin(pin)

    def request_cash(self):
        print("🤑 Request cash")
        self.state.request_cash()


if __name__ == "__main__":
    atm = ATMMachine()
    atm.request_cash()
    atm.insert_card()
    atm.enter_pin(123456)
    atm.request_cash()
    atm.eject_card()
    atm.insert_card()
    atm.enter_pin(None)
    atm.enter_pin(None)
