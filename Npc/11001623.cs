using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001623: Wei Hong
/// </summary>
public class _11001623 : NpcScript {
    internal _11001623(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006126$ 
                // - You got something to say to me?
                return true;
            case 10:
                // $script:0531170907006281$ 
                // - I'm looking forward to today's match.
                switch (selection) {
                    // $script:0531170907006282$
                    // - What makes you so sure $npcName:11001547[gender:0]$'s going to win?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0531170907006283$ 
                // - I'm not. Anything can happen in the ring. But I know $npcName:11001547[gender:0]$, and I know that he never fails me.
                switch (selection) {
                    // $script:0531170907006284$
                    // - That's because he's never faced me in the ring.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0531170907006285$ 
                // - Is that so? Okay. Let's see if your fists can back up your words.
                return true;
            default:
                return true;
        }
    }
}
