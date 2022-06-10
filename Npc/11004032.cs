using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004032: Lanemone
/// </summary>
public class _11004032 : NpcScript {
    internal _11004032(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010049$ 
                // - What is it, kid? You want to know about lapenshards?
                return true;
            case 20:
                // $script:0614185307010050$ 
                // - What is it, kid? You want to know about lapenshards?
                return true;
            default:
                return true;
        }
    }
}
