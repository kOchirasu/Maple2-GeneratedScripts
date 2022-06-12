using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000042: Orde
/// </summary>
public class _11000042 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10;20;30;40;50;60;70;80;90;100;110;120
    }

    // Select 0:
    // $script:0831180610000107$
    // - Ugh... I hate being bothered. What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610000108$
                // - Honestly, I don't care about politics or the court. My time is much better spent reading books in $map:02000031$.
                return 1;
            case (1, 1):
                // functionID=1 
                // $script:0831180610000109$
                // - People don't understand the value to be found in dusty tomes and conversing with the fairies in $map:02000023$. But you have a certain inquisitiveness in your eyes, an intellectual spark. You might make a good Wizard. I'm not going to push, but if you're the arcane arts, I'd be willing to assist you.
                return -1;
            case (10, 0):
                // $script:0831180610000110$
                // - Honestly, I don't care about politics or the court, and you shouldn't waste your time on things like that either. Come see me if you ever want to discuss what actually matters in this world. I've got plenty of wisdom to share.
                switch (selection) {
                    // $script:0831180610000111$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000112$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:0831180610000113$
                // - It seems the simple minds of ordinary folk can't understand us Wizards. We're more interested in scholarly matters, like understanding the origin of this world and what caused the earthquake, than we are in whether the empress holds her court.
                return -1;
            case (12, 0):
                // $script:0831180610000114$
                // - Some people think the earthquake was not a naturally occurring phenomenon, and I'm inclined to agree with them. There's evidence to support such a theory...
                return 12;
            case (12, 1):
                // $script:0831180610000115$
                // - And you have to admit, it's suspicious that the palace canceled court, which would have been the first one in quite a long time, just because of a simple earthquake. Very suspicious indeed...
                return -1;
            case (13, 0):
                // $script:0607163510001504$
                // - What could I possibly have to discuss with you? You and I have nothing in common. Are you looking for magical body-building tips or something? We of the arcane arts don't waste our time trying to enhance our physical forms, as we know that the font of our power lies within.
                switch (selection) {
                    // $script:0607163510001505$
                    // - I'm simply pursuing my fullest potential, just like you're doing.
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:0607163510001506$
                // - Ultimate potential? <i>Suuuure</i>, I can help. Unleash your "ultimate potential" with my patented brew of enchanted smoothies! They can be yours for the low, low price of 1,200 mesos! Pffft. You sound like you've been roped into some kind of scam.
                switch (selection) {
                    // $script:0607181410001555$
                    // - Let's talk about something else.
                    case 0:
                        return 110;
                }
                return -1;
            case (15, 0):
                // $script:0806014810001601$
                // - Are you still here? I'd suggest you stop wasting my time, before I make you a guinea pig for my magical studies.
                switch (selection) {
                    // $script:0806014810001602$
                    // - Do you know who I am?
                    case 0:
                        return 16;
                }
                return -1;
            case (16, 0):
                // $script:0806014810001603$
                // - What, are you some kind of celebrity to the common-folk? Why would I know anything about— Woah... what's up with your aura?
                return 16;
            case (16, 1):
                // $script:0806014810001604$
                // - I didn't notice it while I was busy trying to ignore you, but your aura is like nothing I've ever seen. I sense two opposing forces swirling within you.
                //   It's like watching two stupid salamanders trying to swallow each others' tails.
                return 16;
            case (16, 2):
                // $script:0806014810001605$
                // - The first energy unlike anything ever described within the <i>Encyclopedia Arcana</i>... It almost resembles the energy of nature, but... it's so condensed. Incredible. I would never have believed a mortal could accumulate so much power in a single lifetime.
                return 16;
            case (16, 3):
                // $script:0806014810001606$
                // - And the second is something darker. It's almost feels like... No, that's not possible.
                switch (selection) {
                    // $script:0806014810001607$
                    // - I don't know what you're talking about.
                    case 0:
                        return 17;
                }
                return -1;
            case (17, 0):
                // $script:0806014810001608$
                // - Just what in the world are you?
                switch (selection) {
                    // $script:0806014810001609$
                    // - I have no memory of my past.
                    case 0:
                        return 18;
                }
                return -1;
            case (18, 0):
                // $script:0806014810001610$
                // - Huh? Really? Were you in some kind of accident...? Come closer. I know just the spell for reading memories.
                switch (selection) {
                    // $script:0806014810001611$
                    // - (Move closer.)
                    case 0:
                        return 19;
                }
                return -1;
            case (19, 0):
                // $script:0806014810001612$
                // - Stay perfectly still.
                //   <font color="#909090">(She places her hand on your head and begins to recite an incantation. A spark leaps from her finger tips, and your head starts to feel fuzzy.)</font>
                return 19;
            case (19, 1):
                // $script:0806014810001613$
                // - I can't see anything... There's a thick purple haze swirling around inside your head, it's obstructing my view.
                return 19;
            case (19, 2):
                // $script:0806014810001614$
                // - I don't believe it. Could you really be...!? No, it's better not to rush to any conclusions. I've got to consult with my colleagues. In the mean time, I'll be keeping an eye on you. Please leave now.
                switch (selection) {
                    // $script:0806014810001615$
                    // - Change the subject.
                    case 0:
                        return 120;
                }
                return -1;
            case (20, 0):
                // $script:0831180610000116$
                // - A Wizard's life is lonely and difficult. We can never stop studying until we reach the very zenith of magical knowledge. You've got quite a road ahead of you. Is there anything you want to ask a fellow scholar?
                switch (selection) {
                    // $script:0831180610000117$
                    // - What should I do now?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180610000120$
                // - Before begin your journey, you should see that you're properly equipped. $npc:11000004[gender:0]$ is a purveyor of fine equipment, and probably has some adequate Wizard gear for sale. Buy whatever supplies are necessary, and venture out into that great, wide world to expand your knowledge!
                return 21;
            case (21, 1):
                // $script:0831180610000121$
                // - As your studies progress, you will attain new levels. This will allow you to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
                return -1;
            case (22, 0):
                // $script:0831180610000122$
                // - When you're ready to <font color="#ffd200">upgrade a skill</font>, just press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
                return 22;
            case (22, 1):
                // $script:0831180610000123$
                // - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
                return -1;
            case (23, 0):
                // $script:0831180610000124$
                // - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>. 
                return 23;
            case (23, 1):
                // $script:0831180610000125$
                // - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
                return 23;
            case (23, 2):
                // $script:0831180610000126$
                // - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently. It would be best to hunt such foes with a party.
                return 23;
            case (23, 3):
                // $script:0831180610000127$
                // - And as for $itemPlural:40100022$—well, you can learn about those on your own.
                return -1;
            case (30, 0):
                // $script:0831180610000128$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Knight.
                switch (selection) {
                    // $script:0831180610000129$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000130$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (40, 0):
                // $script:0831180610000131$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Berserker.
                switch (selection) {
                    // $script:0831180610000132$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000133$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (50, 0):
                // $script:0831180610000134$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Priest.
                switch (selection) {
                    // $script:0831180610000135$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000136$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (60, 0):
                // $script:0831180610000137$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Archer.
                switch (selection) {
                    // $script:0831180610000138$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000139$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (70, 0):
                // $script:0831180610000140$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Heavy Gunner.
                switch (selection) {
                    // $script:0831180610000141$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000142$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (80, 0):
                // $script:0831180610000143$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Thief.
                switch (selection) {
                    // $script:0831180610000144$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000145$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (90, 0):
                // $script:0831180610000146$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Assassin.
                switch (selection) {
                    // $script:0831180610000147$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0831180610000148$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (100, 0):
                // $script:1216124310001325$
                // - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Runeblade.
                switch (selection) {
                    // $script:1216124310001326$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:1216124310001327$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                }
                return -1;
            case (110, 0):
                // $script:0607163510001507$
                // - Honestly, we don't care about politics or the empress's court... nor do we care who you are. Our interests lie in more scholarly pursuits.
                switch (selection) {
                    // $script:0607163510001508$
                    // - What do you care about, then?
                    case 0:
                        return 11;
                    // $script:0607163510001509$
                    // - Do you know what caused the earthquake?
                    case 1:
                        return 12;
                    // $script:0607163510001510$
                    // - There's another subject I'd like to ask you about.
                    case 2:
                        return 13;
                }
                return -1;
            case (120, 0):
                // $script:0806014810001616$
                // - Honestly, we don't care about politics or the empress's court... nor do we care who you are. Our interests lie in more scholarly pursuits.
                switch (selection) {
                    // $script:0806014810001617$
                    // - What do you care about?
                    case 0:
                        return 11;
                    // $script:0806014810001618$
                    // - What caused the earthquake?
                    case 1:
                        return 12;
                    // $script:0806014810001619$
                    // - There's another subject I'd like to ask you about.
                    case 2:
                        return 15;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Close,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.SelectableDistractor,
            (16, 0) => NpcTalkButton.Next,
            (16, 1) => NpcTalkButton.Next,
            (16, 2) => NpcTalkButton.Next,
            (16, 3) => NpcTalkButton.SelectableDistractor,
            (17, 0) => NpcTalkButton.SelectableDistractor,
            (18, 0) => NpcTalkButton.SelectableDistractor,
            (19, 0) => NpcTalkButton.Next,
            (19, 1) => NpcTalkButton.Next,
            (19, 2) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Next,
            (22, 1) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Next,
            (23, 1) => NpcTalkButton.Next,
            (23, 2) => NpcTalkButton.Next,
            (23, 3) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (80, 0) => NpcTalkButton.SelectableDistractor,
            (90, 0) => NpcTalkButton.SelectableDistractor,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (110, 0) => NpcTalkButton.SelectableDistractor,
            (120, 0) => NpcTalkButton.SelectableDistractor,
            (1, 0) => NpcTalkButton.Next,
            (1, 1) => NpcTalkButton.ChangeJob,
            _ => NpcTalkButton.None,
        };
    }
}
