""" 11001558: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617105607006362$
        # - Mm? Yes?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006819$
        # - What do you need? Maybe I can help.
        if pick == 0:
            # $script:0727223007006820$
            # - I had a strange dream...
            return 40
        elif pick == 1:
            # $script:0727223007006821$
            # - I want to know more about Guidance.
            return 50
        elif pick == 2:
            # $script:0727223007006822$
            # - How long was I out?
            return 60
        elif pick == 3:
            # $script:0727223007006823$
            # - Tell me about the master.
            return 70
        return -1

    def __40(self, pick: int) -> int:
        # $script:0727223007006824$
        # - That would explain all the mumbling. It wasn't... <i>the</i> dream, was it?
        if pick == 0:
            # $script:0727223007006825$
            # - No... It was different this time...
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0727223007006826$
        # - That's a relief! I think I'd go crazy if I kept having nightmares about being chased by some mysterious figure.
        if pick == 0:
            # $script:0727223007006827$
            # - I dreamed about the first time I met the master and $npcName:11001557[gender:0]$.
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0727223007006828$
        # - That's the earliest memory you have, isn't it? It must have made a real impression! And why not? The first time I met you also left an impression.
        if pick == 0:
            # $script:0727223007006829$
            # - Not a bad impression, I hope!
            return 43
        return -1

    def __43(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006830$
            # - No, no, not bad, just... startling. The members of Guidance have always been animal folk, at least until you came along. I never expected to see the master and $npcName:11001557[gender:0]$ return to Halo Mountain with a bloodied human in tow.
            return 43
        elif self.index == 1:
            # $script:0727223007006831$
            # - I was sure the master would boot you back out as soon as you were walking again. Instead, he took you on as his student. $npcName:11001557[gender:0]$ sure wasn't happy about that...
            if pick == 0:
                # $script:0727233607006917$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006832$
            # - For thousands of years, Guidance only ever accepted animal folk into its fold. It was specifically founded by the great Lone Spirit to help us reach enlightenment.
            return 50
        elif self.index == 1:
            # $script:0727223007006833$
            # - But that was long ago, and the Lone Spirit's philosophy has surely evolved over millenia of teaching and study. Besides, Halo Mountain is practically empty now, so I say it's time we started accepting more members... including humans like you.
            return 50
        elif self.index == 2:
            # $script:0727223007006834$
            # - Before you came along, it was just the master, $npcName:11001557[gender:0]$, and me. But with you, we're now a happy family of four.
            if pick == 0:
                # $script:0727223007006835$
                # - Where did all the students go?
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006836$
            # - Some finished their training and left with the master's blessing. Some left to live with the humans. But most of them couldn't handle the training and gave up.
            return 51
        elif self.index == 1:
            # $script:0727223007006837$
            # - Regardless of the reasons, we still consider all of them members of Guidance. Well, almost all of them. Some of them started their own group devoted to money and power, not enlightenment. We're not on good terms.
            if pick == 0:
                # $script:0727233607006918$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006838$
            # - Half a day, maybe? $npcName:11001557[gender:0]$ was pretty moody about it, since it's the second time you've fainted on us. He just needs to have more patience with your human stamina, if you ask me.
            return 60
        elif self.index == 1:
            # $script:0727223007006839$
            # - I don't mind. Taking care of you gives me the chance to relax here and do my antlers. These fairy sparkles take time to get right, y'know. Hey, you want me to do yours? We've got time... if you leave now, then we <i>both</i> have to get back to training...
            if pick == 0:
                # $script:0727223007006840$
                # - I'm ready.
                return 61
            return -1
        return -1

    def __61(self, pick: int) -> int:
        # $script:0727223007006841$
        # - Oh, all right. Guess I can't sit around here <i>all</i> day.
        if pick == 0:
            # $script:0727223007006842$
            # - Why do you think I fainted?
            return 62
        return -1

    def __62(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006843$
            # - It must be the animus that the master breathed into you. I've never heard of a human using animus before you, so it makes sense it would be hard on your squishy, furless body. Besides, the master's animus is potent even for us animal folk.
            return 62
        elif self.index == 1:
            # $script:0727223007006844$
            # - You have a great power inside you, but you're not strong enough to control it. I imagine that feels pretty rough now and then.
            if pick == 0:
                # $script:0727223007006845$
                # - I want to know the secrets of animus.
                return 63
            return -1
        return -1

    def __63(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006846$
            # - There's nothing secret about it, really. All you have to do is reach unity with nature by disciplining your mind and body, and then harness the energy that creates. The trick is actually <i>doing</i> any of that.
            return 63
        elif self.index == 1:
            # $script:0727223007006847$
            # - I'm sure $npcName:11001557[gender:0]$ would be happy to tell you all about it during training.
            if pick == 0:
                # $script:0727233607006919$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:0727223007006848$
        # - Master $npcName:11001556[gender:0]$ is our teacher and the leader of Guidance. He is the fifteenth master to hold the title of Munakra, which means "seeker of knowledge."
        if pick == 0:
            # $script:0727223007006849$
            # - Munakra?
            return 71
        return -1

    def __71(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006850$
            # - The Lone Spirit led Guidance for hundreds of years before he vanished. When the time came, he chose the wisest of his students and bestowed upon them the title of Munakra.
            return 71
        elif self.index == 1:
            # $script:0727223007006851$
            # - Since then, the wisest student of each generation receives the title and becomes Guidance's new leader. Our master is the fifteenth in that line. And even if we're pretty small now, we still stand thanks to his leadership. 
            return 71
        elif self.index == 2:
            # $script:0727223007006852$
            # - The master makes a yearly pilgrimage to the outside world to help the needy and fight evil. He does it all in secret, too. I think he's done more to help Maple World than any of the Munakra who led Guidance before him.
            if pick == 0:
                # $script:0727233607006920$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.NEXT
        elif (self.state, self.index) == (43, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.NEXT
        elif (self.state, self.index) == (62, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (63, 0):
            return Option.NEXT
        elif (self.state, self.index) == (63, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.NEXT
        elif (self.state, self.index) == (71, 1):
            return Option.NEXT
        elif (self.state, self.index) == (71, 2):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
