using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004181: Red Cape
/// </summary>
public class _11004181 : NpcScript {
    internal _11004181(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010624$ 
                // - What do <i>you</i> want?
                return true;
            case 10:
                // $script:0806025707010625$ 
                // - None of this makes any sense.
                return true;
            default:
                return true;
        }
    }
}
