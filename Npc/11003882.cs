using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003882: 
/// </summary>
public class _11003882 : NpcScript {
    internal _11003882(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0430025106000990$ 
                // - Empress's blessing be with you! 
                return true;
            case 30:
                // $script:0601171006000994$ 
                // - SCRIPTNPCSHOP_0601171006000994_NAME 
                return true;
            default:
                return true;
        }
    }
}
