using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000007: Ellie
/// </summary>
public class _11000007 : NpcScript {
    internal _11000007(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 1:
                // $script:0831180407000026$ 
                // - What's wrong?
                return true;
            case 30:
                // $script:0831180407000029$ 
                // - Platoon leader of the Green Hoods, at your service. $npcName:11000015[gender:1]$ sent me here to watch over $map:02000146$.
                return true;
            case 40:
                // $script:0831180407000030$ 
                // - There's one person whom I admire more than $npc:11000015[gender:1]$, and it's my father. He died of illness when I was young, but the bow he carved for me was my inspiration to join this militia.
                // $script:0831180407000031$ 
                // - I'll do my best to become a good militia member, so I can believe my father would be proud of me.
                return true;
            default:
                return true;
        }
    }
}
