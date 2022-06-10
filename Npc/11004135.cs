using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004135: Landevian
/// </summary>
public class _11004135 : NpcScript {
    internal _11004135(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010535$ 
                // - So much power...
                return true;
            case 10:
                // $script:0730132107010536$ 
                // - All this power... I want to test it on something...
                return true;
            default:
                return true;
        }
    }
}
