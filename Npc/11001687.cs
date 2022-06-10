using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001687: Zabeth
/// </summary>
public class _11001687 : NpcScript {
    internal _11001687(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006488$ 
                // - What're you staring at? You want a piece of me?
                return true;
            case 30:
                // $script:0629000607006491$ 
                // - Whatever you want from me, it can wait.
                switch (selection) {
                    // $script:0706173707006648$
                    // - Were you worried about $npcName:11001679[gender:0]$?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0706173707006649$ 
                // - Wh-who's worried? Stop talking nonsense, or I'll beat the stuffing outta you!
                return true;
            default:
                return true;
        }
    }
}
