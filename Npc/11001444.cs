using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001444: Vellinder
/// </summary>
public class _11001444 : NpcScript {
    internal _11001444(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1220201207005444$ 
                // - Hello. 
                return true;
            case 30:
                // $script:1220201207005447$ 
                // - There's nothing like a quick swim to beat the heat. 
                return true;
            default:
                return true;
        }
    }
}
