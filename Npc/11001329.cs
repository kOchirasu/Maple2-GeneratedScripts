using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001329: Dubore
/// </summary>
public class _11001329 : NpcScript {
    internal _11001329(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005235$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:1217012607005238$ 
                // - Yesterday, 2895 guests passed on their way to $map:02010002$. Today, you are the 3527th guest.
                // $script:1227194507005707$ 
                // - Ah... Why can't I simply forget my useless memories? Being able to remember everything is a curse!
                return true;
            default:
                return true;
        }
    }
}
