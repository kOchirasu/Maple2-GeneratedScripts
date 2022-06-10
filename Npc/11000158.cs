using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000158: Bruno
/// </summary>
public class _11000158 : NpcScript {
    internal _11000158(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000666$ 
                // - What seems to be the problem? 
                return true;
            case 20:
                // $script:0831180407000668$ 
                // - This is bad. The monsters are growing stronger by the day. 
                return true;
            case 30:
                // $script:0831180407000669$ 
                // - If you're looking for $itemPlural:20000014$, the monsters around here are running around with them. 
                return true;
            case 40:
                // $script:0116162507009777$ 
                // - What brings you here, $MyPCName$? 
                // $script:0116162507009778$ 
                // - Are you really working with $npcName:11003534[gender:0]$? Do you think you could put in a good word? 
                switch (selection) {
                    // $script:0116162507009779$
                    // - Uhh... About what?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0116162507009780$ 
                // - Becoming his apprentice! He says that I'm still a rookie, but in just ten years under his tutelage, I could become one of the greatest guards of all time! 
                switch (selection) {
                    // $script:0116162507009781$
                    // - Ten years?!
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0116162507009782$ 
                // - Anyway, why are you here? 
                switch (selection) {
                    // $script:0116162507009783$
                    // - I'm looking into rumors about places affected by extreme heat.
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:0116162507009784$ 
                // - Extreme heat. I see...  
                // $script:0116170407009790$ 
                // - I don't know anything about that! 
                // $script:0116162507009785$ 
                // - They say $npcName:11000005[gender:1]$ knows just about everything. You could head to $map:02000031$ and ask her. 
                switch (selection) {
                    // $script:0116162507009786$
                    // - Thank you for your time.
                    case 0:
                        Id = 44;
                        return false;
                }
                return true;
            case 44:
                // $script:0116162507009787$ 
                // - It was my pleasure! Please tell $npcName:11003534[gender:0]$ I said hello. 
                return true;
            default:
                return true;
        }
    }
}
