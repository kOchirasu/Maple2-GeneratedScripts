using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003327: Richard
/// </summary>
public class _11003327 : NpcScript {
    internal _11003327(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0424104307008431$ 
                // - Ugh...
                return true;
            case 30:
                // $script:0424104307008432$ 
                // - Ugh...
                return true;
            default:
                return true;
        }
    }
}
