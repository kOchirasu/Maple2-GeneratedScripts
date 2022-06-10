using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000037: Lea
/// </summary>
public class _11000037 : NpcScript {
    internal _11000037(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000200$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407000203$ 
                // - One day, I'm going to go out and explore the world! You'll join me when I do, right $MyPCName$? 
                return true;
            case 40:
                // $script:1130105307004657$ 
                // - I see you've brought me some $itemPlural:30000435$. 
                switch (selection) {
                    // $script:1130105307004658$
                    // - Can you purify them?

                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1130105307004659$ 
                // - Well... You see, that needs some special purging magic... $npcName:11000031[gender:0]$ and the fairies think I'm too young to learn that kind of magic. They won't even let me gather $itemPlural:30000435$. 
 
                // $script:1130105307004660$ 
                // - Even if I can't cast neat purifying spells, at least I can collect $itemPlural:30000435$ from adventurers like you. If I get enough flowers, maybe $npc:11000031[gender:0]$ will finally let me do the fun stuff. When he does, bring me more flowers, okay? 
                return true;
            default:
                return true;
        }
    }
}
