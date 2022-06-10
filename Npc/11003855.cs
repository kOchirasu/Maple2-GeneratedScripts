using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003855: 
/// </summary>
public class _11003855 : NpcScript {
    internal _11003855(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1130175706001007$ 
                // - I've got everything you need to take on $npc:23000090[gender:0]$.
                return true;
            case 30:
                // $script:1130175706001008$ 
                // - The particle cannon is our last hope. $MyPCName$, I leave it to you!
                // $script:1130175706001009$ 
                // - Look alive! $npc:23000090[gender:0]$ is out there!
                return true;
            default:
                return true;
        }
    }
}
