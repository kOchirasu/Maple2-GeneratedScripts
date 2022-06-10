using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001576: Eupheria
/// </summary>
public class _11001576 : NpcScript {
    internal _11001576(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006064$ 
                // - Don't worry too much. 
                return true;
            case 10:
                // $script:0515180307006118$ 
                // - I think everyone... will be all right... 
                return true;
            default:
                return true;
        }
    }
}
