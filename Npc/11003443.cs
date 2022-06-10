using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003443: Kaitlyn
/// </summary>
public class _11003443 : NpcScript {
    internal _11003443(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008691$ 
                // - What?
                return true;
            case 10:
                // $script:0721142007008709$ 
                // - What?
                return true;
            default:
                return true;
        }
    }
}
