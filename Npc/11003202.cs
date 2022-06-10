using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003202: Joddy
/// </summary>
public class _11003202 : NpcScript {
    internal _11003202(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008230$ 
                // - Jeez, who knew being a guard would be so tough?
                return true;
            case 10:
                // $script:0404083307008231$ 
                // - I'm learning so much just from standing in the same room as you, $MyPCName$.
                return true;
            case 20:
                // $script:0518141907008519$ 
                // - $MyPCName$! Something terrible has happened!
                return true;
            default:
                return true;
        }
    }
}
