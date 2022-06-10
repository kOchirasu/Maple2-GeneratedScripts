using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004564: Orde
/// </summary>
public class _11004564 : NpcScript {
    internal _11004564(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014526$ 
                // - Hm...
                return true;
            case 10:
                // $script:0220211107014527$ 
                // - Sigh...
                switch (selection) {
                    // $script:0220211107014528$
                    // - You doing okay?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0220211107014529$ 
                // - Uh? Whuh?
                // $script:0220211107014530$ 
                // - What are <i>you</i> doing here?! Oh, no. Don't tell me we're fighting, too...
                // $script:0220211107014531$ 
                // - Listen up. The Pink Beans told me something. They said... they said if I win...
                // $script:0220211107014532$ 
                // - ...then I'll get to interview $npcName:11004568[gender:1]$ herself! Could you imagine? That girl is practically a dragon, thanks to her adopted father!
                // $script:0220211107014533$ 
                // - So if you get matched against me, throw the fight, okay?
                switch (selection) {
                    // $script:0220211107014534$
                    // - Well...
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0220211107014535$ 
                // - Fine, <i>don't</i> throw the fight. But I warn you, I'll give it everything I've got!
                return true;
            default:
                return true;
        }
    }
}
