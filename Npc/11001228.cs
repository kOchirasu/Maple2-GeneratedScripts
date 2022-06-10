using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001228: Puri
/// </summary>
public class _11001228 : NpcScript {
    internal _11001228(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1118145206000544$ 
                // - Do you have any $itemPlural:90000014$? I'll trade you some amazing fairy treasures for them!
                return true;
            case 30:
                // $script:1118145206000547$ 
                // - There's not much to talk about. You got $itemPlural:90000014$, I've got treasures to trade. It's pretty simple, 'cause I just LOVE those fruits!
                switch (selection) {
                    // $script:1118145206000548$
                    // - What are $itemPlural:90000014$?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1118145206000549$
                    // - Why do you need $itemPlural:90000014$?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1118145206000550$
                    // - Can you really exchange fairy treasure for $itemPlural:90000014$?
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:1118145206000551$ 
                // - They're fruits that grow in the $map:2000350$. They also call them the Fruit of Darkness, since they grow rich off the intense darkness of the Shadow World. That's what makes 'em tasty!
                return true;
            case 32:
                // $script:1118145206000552$ 
                // - Well, $npcName:11000031[gender:0]$ and the guard fairies have been battling back the darkness pouring out of the $map:2000350$. Some of them got poisoned from $itemPlural:90000014$, and $npc:11000031[gender:0]$ said they need the same poison to recover.
                // $script:1118145206000553$ 
                // - I'm collecting $item:90000014$ extract to make antidotes from. It, uh, also happens to be super tasty... so I need a lot. A LOT.
                return true;
            case 33:
                // $script:1118145206000554$ 
                // - Sure! No treasure is worth more than a life. My friends were hurt while protecting our forest, so I'll do whatever it takes to make them better!
                return true;
            default:
                return true;
        }
    }
}
