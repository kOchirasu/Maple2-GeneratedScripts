using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001071: Damon
/// </summary>
public class _11001071 : NpcScript {
    internal _11001071(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003651$ 
                // - Are you sure you came to see me?
                return true;
            case 30:
                // $script:0831180407003654$ 
                // - The streets here look like a jungle.
                return true;
            default:
                return true;
        }
    }
}
