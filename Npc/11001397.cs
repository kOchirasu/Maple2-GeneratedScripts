using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001397: Akamorro
/// </summary>
public class _11001397 : NpcScript {
    internal _11001397(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005397$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:1226235907005601$ 
                // - I like quiet places. Real quiet places. 
                switch (selection) {
                    // $script:1226235907005602$
                    // - Why's that?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1226235907005603$ 
                // - I've got my reasons. 
                switch (selection) {
                    // $script:1226235907005604$
                    // - Such as...?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1226235907005605$ 
                // - I like quiet places because then I don't have to deal with nosy people like you. But I guess it's time for me to look for a new quiet place. 
                return true;
            case 40:
                // $script:1227015507005609$ 
                // - Hm? Who are you? 
                switch (selection) {
                    // $script:1227015507005610$
                    // - $npcName:11001396[gender:1]$ wants this slab translated.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1227015507005611$ 
                // - Oh, yes, I remember her. Clever girl. It didn't even occur to her that I might not be able to translate this. 
                switch (selection) {
                    // $script:1227015507005612$
                    // - You can't do it?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1227015507005613$ 
                // - I didn't say that! Child's play, mere child's play. Now be quiet while I work... 
                // $script:1227015507005614$ 
                // - Yes... Mm-hmm... Now, that is interesting. 
                switch (selection) {
                    // $script:1227015507005615$
                    // - What is?!
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:1227015507005616$ 
                // - Be quiet, you! Your jabbering is distracting. 
                switch (selection) {
                    // $script:1227015507005617$
                    // - (Make an exaggerated lip-zipping motion.)
                    case 0:
                        Id = 44;
                        return false;
                }
                return true;
            case 44:
                // $script:1227015507005618$ 
                // - Yes, I see. This will be quite helpful... I've got something for you. Wait just a while longer.  
                switch (selection) {
                    // $script:1227015507005619$
                    // - (Wait several moments.)
                    case 0:
                        Id = 45;
                        return false;
                }
                return true;
            case 45:
                // $script:1227015507005620$ 
                // - If I do this, then... Is the formula off? Then I should try this, and... 
                // $script:1227015507005621$ 
                // - It is done! I don't know who made this slab, but it contained the answer to a new formula I've been trying to perfect. 
                // $script:1227015507005622$ 
                // - This record describes a method for stimulating the nerves and triggering a transformation in the body. I reverse-engineered the method to create a restorative tincture! 
                switch (selection) {
                    // $script:1227015507005623$
                    // - Yes, and?
                    case 0:
                        Id = 46;
                        return false;
                }
                return true;
            case 46:
                // $script:1227015507005624$ 
                // - So impertinent! I was just getting to the good part. In short... 
                // $script:1227015507005625$ 
                // - I've created a potion that can alleviate the ailments that $npcName:11001396[gender:1]$ told me about. Note that I am being most humble here. When I say alleviate, I mean completely cure. 
                switch (selection) {
                    // $script:1227015507005626$
                    // - Thank you.
                    case 0:
                        Id = 0; // TODO: 47 | 48
                        return false;
                }
                return true;
            case 47:
                // $script:1227015507005627$ functionID=1 
                // - Take this to $npcName:11001396[gender:1]$. And tell her she's welcome. 
                return true;
            case 48:
                // $script:1230110007005751$ 
                // - I don't think you have enough space in your bag. Lighten your load first. 
                return true;
            case 50:
                // $script:1227033507005628$ 
                // - Is there anything else you need? 
                switch (selection) {
                    // $script:1227033507005629$
                    // - No.
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1227033507005630$ 
                // - Good, good. You may leave. 
                return true;
            default:
                return true;
        }
    }
}
