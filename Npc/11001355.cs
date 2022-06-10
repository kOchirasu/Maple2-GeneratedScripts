using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001355: Lele
/// </summary>
public class _11001355 : NpcScript {
    internal _11001355(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1216233107005221$ 
                // - Ah! A human!
                return true;
            case 40:
                // $script:1216233107005225$ 
                // - We're not supposed to talk to strangers without the captain's approval.
                switch (selection) {
                    // $script:1216233107005226$
                    // - I'm not a stranger. I'm just a friend you haven't met.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1216233107005227$ 
                // - Beat it! I'm not gonna get in trouble again!
                return true;
            default:
                return true;
        }
    }
}
