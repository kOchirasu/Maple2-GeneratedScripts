using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003393: Muphaza
/// </summary>
public class _11003393 : NpcScript {
    internal _11003393(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0724101007008722$ 
                // - I'm worried. 
                return true;
            case 10:
                // $script:0724101007008723$ 
                // - I'm worried. 
                return true;
            default:
                return true;
        }
    }
}
