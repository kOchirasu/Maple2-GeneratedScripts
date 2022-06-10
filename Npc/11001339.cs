using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001339: Potler
/// </summary>
public class _11001339 : NpcScript {
    internal _11001339(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005275$ 
                // - Skateboarding is harder than it looks.
                return true;
            case 30:
                // $script:1217012607005278$ 
                // - Why is this so hard?! I can <i>visualize</i> myself doing these tricks, so why can't I actually <i>do</i> them?!
                return true;
            default:
                return true;
        }
    }
}
