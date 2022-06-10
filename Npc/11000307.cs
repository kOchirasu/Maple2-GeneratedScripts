using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000307: Arnold
/// </summary>
public class _11000307 : NpcScript {
    internal _11000307(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000819$ 
                // - Welcome. What brings you?
                return true;
            case 20:
                // $script:1121222006000820$ 
                // - Everyone needs a place to call home.
                return true;
            default:
                return true;
        }
    }
}
