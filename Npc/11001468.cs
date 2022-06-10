using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001468: Gurio
/// </summary>
public class _11001468 : NpcScript {
    internal _11001468(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1223035407005532$ 
                // - Stop bothering me.
                return true;
            case 30:
                // $script:1223035407005535$ 
                // - You like my safety helmet? Two stripes from front to back is the latest fashion.
                return true;
            default:
                return true;
        }
    }
}
