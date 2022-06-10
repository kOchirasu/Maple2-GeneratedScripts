using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000371: NRL-C
/// </summary>
public class _11000371 : NpcScript {
    internal _11000371(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001524$ 
                // - Beep! 
                return true;
            case 10:
                // $script:0831180407001525$ 
                // - Beep! Unauthorized access. 
                return true;
            default:
                return true;
        }
    }
}
