using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003336: Dark Wind Agent
/// </summary>
public class _11003336 : NpcScript {
    internal _11003336(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0510143807008460$ 
                // - We've been betrayed... 
                return true;
            case 10:
                // $script:0510145607008464$ 
                // - Who told them...? 
                return true;
            default:
                return true;
        }
    }
}
