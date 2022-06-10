using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003429: Silver Wolf
/// </summary>
public class _11003429 : NpcScript {
    internal _11003429(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0719173007008675$ 
                // - I sense the war chief at the top of the hourglass. And yet... something is amiss.
                return true;
            case 10:
                // $script:0719173007008676$ 
                // - I sense the war chief at the top of the hourglass. And yet... something is amiss.
                return true;
            default:
                return true;
        }
    }
}
