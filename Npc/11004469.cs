using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004469: Indica
/// </summary>
public class _11004469 : NpcScript {
    internal _11004469(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012119$ 
                // - That little cretin wants to go out and play...
                return true;
            case 10:
                // $script:1227192907012120$ 
                // - That little cretin wants to go out and play...
                return true;
            default:
                return true;
        }
    }
}
