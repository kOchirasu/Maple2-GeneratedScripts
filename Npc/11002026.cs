using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002026: Christina
/// </summary>
public class _11002026 : NpcScript {
    internal _11002026(INpcScriptContext context) : base(context) {
        Id = 60;
        // TODO: RandomPick 60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000448$ 
                // - Can I help you?
                return true;
            case 60:
                // $script:0831180306000451$ 
                // - You don't live here, do you? This shop is locals only. Please shop elsewhere.
                return true;
            default:
                return true;
        }
    }
}
