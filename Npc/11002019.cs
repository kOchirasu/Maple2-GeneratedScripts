using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002019: Misha
/// </summary>
public class _11002019 : NpcScript {
    internal _11002019(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000420$ 
                // - Can I help you?
                return true;
            case 60:
                // $script:0831180306000423$ 
                // - You don't live here, do you? This shop is locals only. Please shop elsewhere.
                return true;
            default:
                return true;
        }
    }
}