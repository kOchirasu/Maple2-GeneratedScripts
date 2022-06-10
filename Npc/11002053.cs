using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002053: Jyl
/// </summary>
public class _11002053 : NpcScript {
    internal _11002053(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1219175006000635$ 
                // - Can I help you?
                return true;
            case 60:
                // $script:1219175006000638$ 
                // - You don't live here, do you? This shop is locals only. Please shop elsewhere.
                return true;
            default:
                return true;
        }
    }
}
