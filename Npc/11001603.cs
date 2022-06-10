using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001603: Char
/// </summary>
public class _11001603 : NpcScript {
    internal _11001603(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006091$ 
                // - What brings you here? 
                return true;
            case 10:
                // $script:0515180307006140$ 
                // - Let's hear them out. 
                return true;
            default:
                return true;
        }
    }
}
