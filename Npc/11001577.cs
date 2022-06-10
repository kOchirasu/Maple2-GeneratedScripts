using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001577: Luanna
/// </summary>
public class _11001577 : NpcScript {
    internal _11001577(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006065$ 
                // - Welcome.
                return true;
            case 10:
                // $script:0515180307006119$ 
                // - We just need to pray for a miracle... 
                return true;
            default:
                return true;
        }
    }
}
