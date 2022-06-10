using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003534: Condor
/// </summary>
public class _11003534 : NpcScript {
    internal _11003534(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1126150707011919$ 
                // - Back in my day, we knew a thing or two about duty!
                return true;
            case 20:
                // $script:1126150707011920$ 
                // - What's the matter? Don't have enough to do?
                switch (selection) {
                    // $script:1126150707011921$
                    // - Uh...
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1126150707011922$ 
                // - If you've got time for chit-chat, you've got time for a mission!
                return true;
            case 40:
                // $script:1126150707011923$ 
                // - If you think you've got what it takes to serve the Imperial Vanguard, then prove it.
                return true;
            default:
                return true;
        }
    }
}
