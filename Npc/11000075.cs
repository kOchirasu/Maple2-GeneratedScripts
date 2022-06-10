using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000075: Ereve
/// </summary>
public class _11000075 : NpcScript {
    internal _11000075(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000349$ 
                // - $MyPCName$, what brings you to me? 
                return true;
            case 10:
                // $script:0831180407000350$ 
                // - We must gather the $itemPlural:30000181$ as soon as possible. They are all that stand between our world and utter darkness. 
                return true;
            case 20:
                // $script:0831180407000351$ 
                // - I've asked much of you, but there is still so much more left to do. 
                return true;
            case 30:
                // $script:0831180407000352$ 
                // - I owe a debt of gratitude to the minister. I hope he returns soon. 
                return true;
            case 40:
                // $script:0831180407000353$ 
                // - It was $npcName:11000044[gender:0]$ who suggested I hold an open court for the people. I suppose it was part of his plan all along... 
                return true;
            default:
                return true;
        }
    }
}
