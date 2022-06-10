using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003424: Nico
/// </summary>
public class _11003424 : NpcScript {
    internal _11003424(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008635$ 
                // - Ugh... 
                return true;
            case 10:
                // $script:0706160807008636$ 
                // - Ugh... 
                return true;
            default:
                return true;
        }
    }
}
