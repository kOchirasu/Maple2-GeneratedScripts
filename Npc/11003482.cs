using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003482: Einos
/// </summary>
public class _11003482 : NpcScript {
    internal _11003482(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008695$ 
                // - I sense change in the wind.
                return true;
            case 10:
                // $script:0721142007008713$ 
                // - I sense change in the wind.
                return true;
            default:
                return true;
        }
    }
}
