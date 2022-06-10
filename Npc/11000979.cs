using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000979: Greemon
/// </summary>
public class _11000979 : NpcScript {
    internal _11000979(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003383$ 
                // - Huh? M-me?
                return true;
            case 30:
                // $script:0831180407003386$ 
                // - What do you have to tell me?
                return true;
            default:
                return true;
        }
    }
}
