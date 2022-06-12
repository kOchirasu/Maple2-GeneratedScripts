using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001535: 
/// </summary>
public class _11001535 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0319195006000716$ 
                // - Are you here to see me?
                return default;
            case 30:
                // $script:0322171106000719$ 
                // - Looking for quality equipment? I've got stuff you can usually only get in dungeons. Take a look if you're interested.
                switch (selection) {
                    // $script:0322171106000720$
                    // - What are you offering?
                    case 0:
                        return (40, NpcTalkButton.SelectableDistractor);
                    // $script:0322171106000721$
                    // - Where do you get all of this from?
                    case 1:
                        return (50, NpcTalkButton.Next);
                    // $script:0322171106000722$
                    // - Is it really good quality stuff?
                    case 2:
                        return (60, NpcTalkButton.Next);
                }
                return default;
            case 40:
                // $script:0322171106000723$ 
                // - I'm selling boxes with items from different dungeons. If you mainly explore dungeons to find good equipment, you'll definitely like what I sell. Buy from me, and you don't have to risk your neck exploring dungeons.
                switch (selection) {
                    // $script:0322171106000724$
                    // - What exactly is in these boxes?
                    case 0:
                        return (41, NpcTalkButton.Next);
                }
                return default;
            case 41:
                switch (Index++) {
                    case 0:
                        // $script:0322171106000725$ 
                        // - Beats me. They've got everything from highly valuable equipment to useless junk. What you get depends on your luck.
                        return (41, NpcTalkButton.Close);
                    case 1:
                        // $script:0322171106000726$ 
                        // - Oh, I nearly forgot the most important thing. Every time you open a box, your reward count for the corresponding dungeon decreases.
                        return default;
                }
                break;
            case 50:
                switch (Index++) {
                    case 0:
                        // $script:0322171106000727$ 
                        // - What a brazen way to ask for all of my trade secrets! Adventurers have all kinds of reasons to explore dungeons, like discovering the rare treasures they contain. I suppose you could call them treasure hunters, and they're good at what they do.
                        return (50, NpcTalkButton.Close);
                    case 1:
                        // $script:0322171106000728$ 
                        // - Naturally, some of them do business with merchants like me. Beyond that, all you need to know is that I have my own supply routes.
                        return default;
                }
                break;
            case 60:
                switch (Index++) {
                    case 0:
                        // $script:0322171106000729$ 
                        // - Good quality? What do you take me for, a cheat? I swear on my reputation as a businessman, I don't know what's inside these boxes any more than you do. If I did, you can bet I'd have priced each box according to its value. 
                        return (60, NpcTalkButton.Close);
                    case 1:
                        // $script:0322171106000730$ 
                        // - But as you can see, I'm selling them at set low prices. It's not about my capacity for swindling. It's about your luck. So don't blame me if you do get junk from your box.
                        return default;
                }
                break;
        }
        
        return default;
    }
}
