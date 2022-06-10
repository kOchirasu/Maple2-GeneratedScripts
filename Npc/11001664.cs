using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001664: Luanna
/// </summary>
public class _11001664 : NpcScript {
    internal _11001664(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617211107006376$ 
                // - May the empress favor you always.
                return true;
            case 10:
                // $script:0617211107006377$ 
                // - Do not betray our empress's trust. 
                return true;
            default:
                return true;
        }
    }
}
