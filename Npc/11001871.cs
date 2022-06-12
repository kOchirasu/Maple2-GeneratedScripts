using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001871: Ophelia
/// </summary>
public class _11001871 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1021213710001685$
    // - And... that's another sword fresh off the grinding stone! What a beaut. This will make for one happy customer... Oh hi there, can I help you? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1021213710001689$
                // - And... that's another sword fresh off the grinding stone! What a beaut. This will make for one happy customer... Oh hi there, can I help you?
                return 10;
            case (10, 1):
                // $script:1021213710001690$
                // - Ah now, let me guess... You want to enchant your gear? Let's have a look, then!
                switch (selection) {
                    // $script:1021213710001691$
                    // - Can you enchant my items?
                    case 0:
                        return 31;
                    // $script:1021213710001692$
                    // - How about we change some bonus attributes?
                    case 1:
                        return 30;
                    // $script:1021213710001693$
                    // - Tell me about your work.
                    case 2:
                        return 29;
                }
                return -1;
            case (29, 0):
                // $script:1021213710001694$
                // - Isn't it obvious? I'm a blacksmith! The best one there is, too. Well, on this street.
                return 29;
            case (29, 1):
                // $script:1021213710001695$
                // - The thing is that <font color="#ffd200">$map:2000076$</font> is absolutely lousy with craftsmen and women. This is the heart of the blacksmithing trade for Maple World, and that makes competition fierce. But that competition is inspiring for people like me. I learn a lot from my peers, and I relate to people who are willing to pour their heart and soul into their work.
                return 29;
            case (29, 2):
                // $script:1021213710001696$
                // - You're not here to talk about me though, are you? You need your gear tuned up, I'm your woman. All I need are the right materials, and I'll work my magic. You know what I'm talking about, right? $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$, all produced in $map:2000051$, usually.
                return 29;
            case (29, 3):
                // $script:1021213710001697$
                // - <font color="#ffd200">$itemPlural:40100023$</font> come from <font color="#ffd200">dismantling</font> gear that's level 20 or higher. Just use the <font color="#ffd200">Dismantle</font> button in your inventory window. As for <font color="#ffd200">$itemPlural:40100024$</font>, you'll need to dismantle gear that is rated Epic or better.
                return 29;
            case (29, 4):
                // $script:1021213710001698$
                // - People compete for <font color="#ffd200">$itemPlural:40100023$</font> in the <font color="#ffd200">Personal Arena</font>, so you could go there. If you think you can win, that is...
                return 29;
            case (29, 5):
                // $script:1021213710001699$
                // - By the way, Elliana got ahold of yet another strange weapon, and she's been begging me to enchant it for her. I told her such flashy, impractical weapons like that can't be enchanted, but she doesn't listen. Why can't she just accept that only items marked as "Can be Enchanted" can, well, be enchanted?
                return 29;
            case (29, 6):
                // $script:1021213710001700$
                // - That's not all! Aside from functioning as weaponry or armor, high-grade gear grants special abilities. But there's a catch: These abilities are completely random! If you would prefer gear that better suits your needs, I can help you modify it as you like.
                return 29;
            case (29, 7):
                // $script:1021213710001701$
                // - This is a new service we blacksmiths provide, thanks to a breakthrough out of the research center in $map:02000270$. Those eggheads figured out how to refine meteoric ores into these $itemPlural:40100026$ that I can use to change the chemical properties in your gear.
                return 29;
            case (29, 8):
                // $script:1021213710001702$
                // - Now, don't get your hopes all the way up. $itemPlural:40100026$ are tricky to work with, so I might not be able to get all the bonuses on your item to exactly what you want. I also need $itemPlural:40100001$, $itemPlural:40100002$, $itemPlural:40100003$, or $itemPlural:40100021$ to work with, and that's up to you to get.
                return -1;
            case (30, 0):
                // functionID=1 
                // $script:1021213710001703$
                // - We can do that! Just show me the item you want to retool. Remember, I can only work on Epic or Legendary armor and accessories at Level 50 or above.
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:1021213710001709$
                // - Okay, let's see the gear you want to enchant. I'm warning you now, it has to be marked with "Can be Enchanted."
                return 31;
            case (31, 1):
                // functionID=1 
                // $script:0330144110002047$
                // - Okay, let's see the gear you want to enchant. I'm warning you now, it has to be marked with "Can be Enchanted."
                return -1;
            case (999, 0):
                // $script:1021213710001788$
                // - Ho boy, I'm busy! Busy, busy, busy... If you were hoping for my services, I just don't have the time right now. I'm working on a special order from the palace.
                switch (selection) {
                    // $script:1021213710001789$
                    // - Can you enchant my items?
                    case 0:
                        return 41;
                    // $script:1021213710001790$
                    // - What do you do?
                    case 1:
                        return 39;
                }
                return -1;
            case (39, 0):
                // $script:1021213710001791$
                // - Isn't it obvious? I'm a blacksmith! The best one there is, too. Well, on this street.
                return 39;
            case (39, 1):
                // $script:1021213710001792$
                // - The thing is that <font color="#ffd200">$map:2000076$</font> is absolutely lousy with craftsmen and women. This is the heart of the blacksmithing trade for Maple World, and that makes competition fierce. But that competition is inspiring for people like me. I learn a lot from my peers, and I relate to people who are willing to pour their heart and soul into their work.
                return 39;
            case (39, 2):
                // $script:1021213710001793$
                // - You're not here to talk about me though, are you? You need your gear tuned up, I'm your woman. All I need are the right materials, and I'll work my magic. You know what I'm talking about, right? $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$, all produced in $map:2000051$, usually.
                return 39;
            case (39, 3):
                // $script:1021213710001794$
                // - <font color="#ffd200">$itemPlural:40100023$</font> come from <font color="#ffd200">dismantling</font> gear that's level 20 or higher. Just use the <font color="#ffd200">Dismantle</font> button in your inventory window. As for <font color="#ffd200">$itemPlural:40100024$</font>, you'll need to dismantle gear that is rated Epic or better.
                return 39;
            case (39, 4):
                // $script:1021213710001795$
                // - People compete for <font color="#ffd200">$itemPlural:40100023$</font> in the <font color="#ffd200">Personal Arena</font>, so you could go there. If you think you can win, that is...
                return 39;
            case (39, 5):
                // $script:1021213710001796$
                // - Keep in mind that the only items you can enchant are Top, Bottom, Suit, and Weapon items at level 20 or above. That frustrates some folks, but I need a solid base to work from. Elliana found some weird weapon she wanted to enchant, but she doesn't get that there are rules to these things. I'm good, but even I have my limits!
                return -1;
            case (41, 0):
                // $script:1021213710001797$
                // - I'd love to help you, but right now I have to focus on this special order from the palace.
                //   No exceptions! Absolutely not! 
                //   You wouldn't want me to stop your order to work on someone else's, so why would you expect me to do that to the palace?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (29, 0) => NpcTalkButton.Next,
            (29, 1) => NpcTalkButton.Next,
            (29, 2) => NpcTalkButton.Next,
            (29, 3) => NpcTalkButton.Next,
            (29, 4) => NpcTalkButton.Next,
            (29, 5) => NpcTalkButton.Next,
            (29, 6) => NpcTalkButton.Next,
            (29, 7) => NpcTalkButton.Next,
            (29, 8) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            (999, 0) => NpcTalkButton.SelectableDistractor,
            (39, 0) => NpcTalkButton.Next,
            (39, 1) => NpcTalkButton.Next,
            (39, 2) => NpcTalkButton.Next,
            (39, 3) => NpcTalkButton.Next,
            (39, 4) => NpcTalkButton.Next,
            (39, 5) => NpcTalkButton.Close,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
