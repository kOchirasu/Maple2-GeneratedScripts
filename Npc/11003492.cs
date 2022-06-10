using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003492: Tina
/// </summary>
public class _11003492 : NpcScript {
    internal _11003492(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0724200407008724$ 
                // - Sigh...
                return true;
            case 10:
                // $script:0724200407008725$ 
                // - Sigh...
                return true;
            default:
                return true;
        }
    }
}
