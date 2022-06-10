using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004526: Quiet Soldieretto
/// </summary>
public class _11004526 : NpcScript {
    internal _11004526(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0103163407012509$ 
                // - Beeep... Beeep...
                return true;
            case 10:
                // $script:0103163407012510$ 
                // - ...
                // $script:0103163407012511$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
