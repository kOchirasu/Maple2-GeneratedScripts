using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004117: Guardsman
/// </summary>
public class _11004117 : NpcScript {
    internal _11004117(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010477$ 
                // - Nothing to report, $male:sir,female:ma'am$.
                return true;
            case 10:
                // $script:0720125407010478$ 
                // - To suddenly appear in a place like this...
                return true;
            default:
                return true;
        }
    }
}
