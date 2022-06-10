using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000370: NRL-B
/// </summary>
public class _11000370 : NpcScript {
    internal _11000370(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001522$ 
                // - Beep! 
                return true;
            case 10:
                // $script:0831180407001523$ 
                // - Beep! Unauthorized access. 
                return true;
            default:
                return true;
        }
    }
}
