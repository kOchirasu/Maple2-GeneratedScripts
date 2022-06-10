using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001912: Assistant Investigator
/// </summary>
public class _11001912 : NpcScript {
    internal _11001912(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1116181807007409$ 
                // - Hello. 
                return true;
            case 20:
                // $script:1116181807007411$ 
                // - We need to track down Katvan's accomplices before they do any more damage.
                return true;
            default:
                return true;
        }
    }
}
