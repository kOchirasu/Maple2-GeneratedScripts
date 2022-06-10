using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001926: Fisher
/// </summary>
public class _11001926 : NpcScript {
    internal _11001926(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121140707007427$ 
                // - I caught a prize fish! 
                return true;
            case 30:
                // $script:1121184207007442$ 
                // - Another one got away...! This is ticking me off! 
                return true;
            default:
                return true;
        }
    }
}
