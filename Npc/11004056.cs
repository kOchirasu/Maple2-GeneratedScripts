using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004056: Allon
/// </summary>
public class _11004056 : NpcScript {
    internal _11004056(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010085$ 
                // - Losing the leadership of Terrun Calibre was too great a loss.
                return true;
            case 10:
                // $script:0614185307010086$ 
                // - Losing the leadership of Terrun Calibre was too great a loss.
                return true;
            default:
                return true;
        }
    }
}
