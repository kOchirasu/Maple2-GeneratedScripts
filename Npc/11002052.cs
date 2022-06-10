using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002052: Elina
/// </summary>
public class _11002052 : NpcScript {
    internal _11002052(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1219175006000631$ 
                // - Can I help you? 
                return true;
            case 60:
                // $script:1219175006000634$ 
                // - You don't live here, do you? This shop is locals only. Please shop elsewhere. 
                return true;
            default:
                return true;
        }
    }
}
