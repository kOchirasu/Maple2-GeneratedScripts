using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001370: Roshimov
/// </summary>
public class _11001370 : NpcScript {
    internal _11001370(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005342$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:1217144507005345$ 
                // - Please check the schedule on the monorail platform. 
                return true;
            default:
                return true;
        }
    }
}
