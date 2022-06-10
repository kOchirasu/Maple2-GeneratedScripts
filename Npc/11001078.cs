using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001078: Luen
/// </summary>
public class _11001078 : NpcScript {
    internal _11001078(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003679$ 
                // - I'm hungry.
                return true;
            case 30:
                // $script:0831180407003682$ 
                // - How did I never know about this place?
                return true;
            default:
                return true;
        }
    }
}
