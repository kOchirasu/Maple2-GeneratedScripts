using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001592: Landevian
/// </summary>
public class _11001592 : NpcScript {
    internal _11001592(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006080$ 
                // - Ah, $MyPCName$!
                return true;
            case 10:
                // $script:0515180307006131$ 
                // - $npcName:11001231[gender:0]$ can't keep this up for long. It's only a matter of time before we have our revenge. 
                return true;
            case 20:
                // $script:0524142307006221$ 
                // - $npcName:11001231[gender:0]$ can't keep this up for long. It's only a matter of time before we have our revenge. 
                return true;
            default:
                return true;
        }
    }
}
