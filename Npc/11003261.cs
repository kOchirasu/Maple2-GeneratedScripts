using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003261: Kaitlyn
/// </summary>
public class _11003261 : NpcScript {
    internal _11003261(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008198$ 
                // - Professor $npcName:11003251[gender:0]$...
                return true;
            case 30:
                // $script:0403155707008201$ 
                // - I've never seen Professor $npc:11003251[gender:0]$ in such a state before. I can't believe this has happened... 
                return true;
            default:
                return true;
        }
    }
}
