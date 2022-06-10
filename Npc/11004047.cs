using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004047: Surmany
/// </summary>
public class _11004047 : NpcScript {
    internal _11004047(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010067$ 
                // - I'll do my best to help the queen.
                return true;
            case 10:
                // $script:0614185307010068$ 
                // - I'll do my best to help the queen.
                return true;
            default:
                return true;
        }
    }
}
