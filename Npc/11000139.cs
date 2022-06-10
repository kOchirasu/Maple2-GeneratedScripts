using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000139: Lailai
/// </summary>
public class _11000139 : NpcScript {
    internal _11000139(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000565$ 
                // - Bah, what now?
                return true;
            case 40:
                // $script:0831180407000569$ 
                // - Hmph, this used to be a really nice place to live before that gigantic hotel dropped from the sky. It's been attracting all kinds of things and making our lives miserable.
                return true;
            case 50:
                // $script:0831180407000570$ 
                // - Well, I'm not fighting those monsters. It's not that they're too scary... I just don't want to be bothered.
                return true;
            default:
                return true;
        }
    }
}
