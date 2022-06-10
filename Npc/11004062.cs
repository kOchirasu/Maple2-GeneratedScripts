using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004062: Tinchai
/// </summary>
public class _11004062 : NpcScript {
    internal _11004062(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010097$ 
                // - Just let us know if there's anything we can do to help.
                return true;
            case 10:
                // $script:0614185307010098$ 
                // - Just let us know if there's anything we can do to help.
                return true;
            default:
                return true;
        }
    }
}
