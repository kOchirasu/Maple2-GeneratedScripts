""" 11001985: Cathy Catalina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0109143707007702$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0109143707007705$
        # - You're here for work? Great! Let's get started.
        if pick == 0:
            # $script:0109143707007706$
            # - What's this new business of yours?
            return 40
        elif pick == 1:
            # $script:0109143707007707$
            # - What should I be doing?
            return 50
        elif pick == 2:
            # $script:0109143707007708$
            # - What are the job requirements?
            return 60
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0109143707007709$
            # - Hehe. It really is a novel business model, isn't it? I guess I can tell you, if you're going to be working here.
            return 40
        elif self.index == 1:
            # $script:0109143707007710$
            # - Maple World's a pretty big place, but as we've developed newer, faster ways to travel, our systems of trade haven't really kept up.
            return 40
        elif self.index == 2:
            # $script:0109143707007711$
            # - People want things they can't get locally. Some people in $map:02000023$ might be starved for electronics from $map:02000100$, or others in $map:02010002$  might want handicrafts from Nerman artists.
            return 40
        elif self.index == 3:
            # $script:0109143707007712$
            # - The thing is, not everybody can afford to trot around the globe shopping for things they want. That's where my shop comes in.
            return 40
        elif self.index == 4:
            # $script:0109143707007713$
            # - Customers place their orders online for an item, and I acquire it for them. Then all they have to do is come in and pick up their merchandise. No muss, no fuss!
            return 40
        elif self.index == 5:
            # $script:0109143707007714$
            # - I've spent a long time building this business, and I've pretty much cornered the market. To do what I do, you need all kinds of connections and a shrewd business acumen. Luckily, I've got that in spades!
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0109143707007715$
            # - You will be working as a team with your three friends. One of you will work the cash register, the rest of you will work in the warehouse.
            return 50
        elif self.index == 1:
            # $script:0109143707007716$
            # - Customers come to the store to pick up their orders. All you have to do is find their items in the warehouse and ring them up at the counter. Easy, right?
            return 50
        elif self.index == 2:
            # $script:0109143707007717$
            # - When a customer comes to the counter, the cashier must greet them. The customer will tell you which item they've come to pick up, and the cashier relays that information to the warehouse workers.
            return 50
        elif self.index == 3:
            # $script:0109143707007718$
            # - The warehouse workers will need to find and bring the item to the cashier. Cathy Mart prides itself in its service, so the faster the better.
            return 50
        elif self.index == 4:
            # $script:0109143707007719$
            # - Also, keep in mind that the store has an automatic cleaning system to keep the place nice and tidy.
            return 50
        elif self.index == 5:
            # $script:0109143707007720$
            # - That means that any item from the warehouse you leave lying around will be removed very soon after. That's why it's crucial you give the item to the customer directly.
            return -1
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0109143707007721$
            # - Do you have two or more grasping appendages? Can you lift things? You're hired! I don't care about your age, job, level, or any of that nonsense. All I need you to do is work together to fulfill customers' orders with blinding speed.
            return 60
        elif self.index == 1:
            # $script:0109143707007722$
            # - The four of you must work together from the moment the store opens until it closes. No quitting, and no breaks!
            if pick == 0:
                # $script:0109143707007723$
                # - Wait, what happens if someone quits?
                return 61
            return -1
        return -1

    def __61(self, pick: int) -> int:
        # $script:0109143707007724$
        # - For your own sake, let's hope that doesn't happen.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.NEXT
        elif (self.state, self.index) == (40, 4):
            return Option.NEXT
        elif (self.state, self.index) == (40, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.NEXT
        elif (self.state, self.index) == (50, 3):
            return Option.NEXT
        elif (self.state, self.index) == (50, 4):
            return Option.NEXT
        elif (self.state, self.index) == (50, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.CLOSE
        return Option.NONE
