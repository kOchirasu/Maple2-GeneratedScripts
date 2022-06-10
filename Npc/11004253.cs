using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004253: Bill
/// </summary>
public class _11004253 : NpcScript {
    internal _11004253(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0829171107010966$ 
                // - Everything seems fine today, but if those monsters dare to return... I'll show them!
                return true;
            case 10:
                // $script:0829171107010967$ 
                // - Everything seems fine today, but if those monsters dare to return... I'll show them!
                // $script:0831140807011005$ 
                // - I've never seen you around these parts before. You're not up to any funny business, are you?
                switch (selection) {
                    // $script:0831140807011006$
                    // - Nah, just passing through. What's up with this place anyway?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0831140807011007$ 
                // - This place, $map:03000165$, used to be infested with monsters. But it wasn't the castle who cleaned it up, oh no! Let me tell you, it was us folks from the Lumina Liberation Army! And to think, this place didn't even have any roads!
                // $script:0831140807011008$ 
                // - We keep the peace here now. Can't rely on those castle folk, you know?
                switch (selection) {
                    // $script:0831140807011009$
                    // - ...You realize this place is totally infested with violent pig-folk right?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0831140807011010$ 
                // - Compared to before, this is nothing! I admit it's still a work in progress, but one day soon we'll be rid of all those monsters!
                return true;
            default:
                return true;
        }
    }
}
