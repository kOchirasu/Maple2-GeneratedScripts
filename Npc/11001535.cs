using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001535: 
/// </summary>
public class _11001535 : NpcScript {
    internal _11001535(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0319195006000716$ 
                // - Are you here to see me? 
                return true;
            case 30:
                // $script:0322171106000719$ 
                // - Looking for quality equipment? I've got stuff you can usually only get in dungeons. Take a look if you're interested. 
                switch (selection) {
                    // $script:0322171106000720$
                    // - What are you offering?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0322171106000721$
                    // - Where do you get all of this from?
                    case 1:
                        Id = 50;
                        return false;
                    // $script:0322171106000722$
                    // - Is it really good quality stuff?
                    case 2:
                        Id = 60;
                        return false;
                }
                return true;
            case 40:
                // $script:0322171106000723$ 
                // - I'm selling boxes with items from different dungeons. If you mainly explore dungeons to find good equipment, you'll definitely like what I sell. Buy from me, and you don't have to risk your neck exploring dungeons. 
                switch (selection) {
                    // $script:0322171106000724$
                    // - What exactly is in these boxes?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0322171106000725$ 
                // - Beats me. They've got everything from highly valuable equipment to useless junk. What you get depends on your luck. 
                // $script:0322171106000726$ 
                // - Oh, I nearly forgot the most important thing. Every time you open a box, your reward count for the corresponding dungeon decreases. 
                return true;
            case 50:
                // $script:0322171106000727$ 
                // - What a brazen way to ask for all of my trade secrets! Adventurers have all kinds of reasons to explore dungeons, like discovering the rare treasures they contain. I suppose you could call them treasure hunters, and they're good at what they do. 
                // $script:0322171106000728$ 
                // - Naturally, some of them do business with merchants like me. Beyond that, all you need to know is that I have my own supply routes. 
                return true;
            case 60:
                // $script:0322171106000729$ 
                // - Good quality? What do you take me for, a cheat? I swear on my reputation as a businessman, I don't know what's inside these boxes any more than you do. If I did, you can bet I'd have priced each box according to its value.  
                // $script:0322171106000730$ 
                // - But as you can see, I'm selling them at set low prices. It's not about my capacity for swindling. It's about your luck. So don't blame me if you do get junk from your box. 
                return true;
            default:
                return true;
        }
    }
}
