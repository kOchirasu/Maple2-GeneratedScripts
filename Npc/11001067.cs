using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001067: Kumier
/// </summary>
public class _11001067 : NpcScript {
    internal _11001067(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003634$ 
                // - Welcome.
                return true;
            case 40:
                // $script:0831180407003638$ 
                // - Now, now. We should be laughing while we're here.
                return true;
            default:
                return true;
        }
    }
}
