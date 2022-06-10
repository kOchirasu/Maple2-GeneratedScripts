using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001946: Cello Student
/// </summary>
public class _11001946 : NpcScript {
    internal _11001946(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007492$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1208184307007536$ 
                // - Finally, I'm in my element. Don't bother me while I'm in the zone.
                return true;
            default:
                return true;
        }
    }
}
