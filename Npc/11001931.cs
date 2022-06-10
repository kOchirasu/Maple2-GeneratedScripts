using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001931: Apprentice Ladme
/// </summary>
public class _11001931 : NpcScript {
    internal _11001931(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122150407007454$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:1122214707007472$ 
                // - I can't afford these materials. I'll just have to get some on my own...  
                return true;
            default:
                return true;
        }
    }
}
