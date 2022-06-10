using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002028: Rose
/// </summary>
public class _11002028 : NpcScript {
    internal _11002028(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000456$ 
                // - Can I help you? 
                return true;
            case 60:
                // $script:0831180306000459$ 
                // - You don't live here, do you? This shop is locals only. Please shop elsewhere. 
                return true;
            default:
                return true;
        }
    }
}
