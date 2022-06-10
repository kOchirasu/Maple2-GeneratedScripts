using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000151: Cecilia
/// </summary>
public class _11000151 : NpcScript {
    internal _11000151(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000644$ 
                // - What?
                return true;
            case 10:
                // $script:0831180407000645$ 
                // - Out of my way.
                return true;
            case 21:
                // $script:0831180407000646$ 
                // - Go ask yourself.
                return true;
            default:
                return true;
        }
    }
}
