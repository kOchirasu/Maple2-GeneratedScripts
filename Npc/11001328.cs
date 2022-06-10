using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001328: Lakachi
/// </summary>
public class _11001328 : NpcScript {
    internal _11001328(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005231$ 
                // - What?
                return true;
            case 30:
                // $script:1217012607005234$ 
                // - Just keep walking. I don't have time for wimps like you!
                return true;
            default:
                return true;
        }
    }
}
