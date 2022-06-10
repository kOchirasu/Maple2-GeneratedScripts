using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001589: Asimov
/// </summary>
public class _11001589 : NpcScript {
    internal _11001589(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006077$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:0515180307006128$ 
                // - We have gathered here for one cause. Together, we can do anything. 
                return true;
            default:
                return true;
        }
    }
}
