using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004543: Brock
/// </summary>
public class _11004543 : NpcScript {
    internal _11004543(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0110183907012681$ 
                // - ...
                return true;
            case 10:
                // $script:0110183907012682$ 
                // - ...
                // $script:0110183907012683$ 
                // - Can't you see I'm on edge? Leave me alone!
                return true;
            default:
                return true;
        }
    }
}
