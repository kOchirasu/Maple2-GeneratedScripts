using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001580: Asimov
/// </summary>
public class _11001580 : NpcScript {
    internal _11001580(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006068$ 
                // - Welcome!
                return true;
            case 10:
                // $script:0515180307006122$ 
                // - This is not going to be easy. 
                return true;
            default:
                return true;
        }
    }
}
