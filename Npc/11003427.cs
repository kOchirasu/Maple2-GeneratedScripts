using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003427: Nipa
/// </summary>
public class _11003427 : NpcScript {
    internal _11003427(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008641$ 
                // - Nipa Nipa! 
                return true;
            case 10:
                // $script:0706160807008642$ 
                // - Nipa Nipa! 
                return true;
            default:
                return true;
        }
    }
}
