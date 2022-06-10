using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003533: Veliche
/// </summary>
public class _11003533 : NpcScript {
    internal _11003533(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1126155107011958$ 
                // - The future is in our hands.
                return true;
            case 20:
                // $script:1126155107011959$ 
                // - Speak. I'm listening.
                switch (selection) {
                    // $script:1126155107011960$
                    // - Tell me about Tria's navy.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1126155107011961$ 
                // - After all this time, you haven't seen the famous navy of Tria?
                // $script:1126155107011962$ 
                // - I suppose that's not unreasonable. Tria's navy isn't in Tria at the moment, after all.
                // $script:1126155107011963$ 
                // - A few months before the empress's grand court, the main fleet was dispatched to an island far away. Not even I know where the command came from.
                // $script:1126155107011964$ 
                // - Fa—I mean, Admiral Martini didn't even take the time to tell me about the mission. They simply set sail, leaving myself and a few petty officers to command a skeleton fleet.
                // $script:1126155107011965$ 
                // - They don't appear on Sky Fortress's radar, either. I'm not sure what to make of the bulk of our military vanishing at a time like this...
                // $script:1126155107011966$ 
                // - I wonder if he's even still alive...
                // $script:1126155107011967$ 
                // - I've said too much. You can trust in Tria's naval forces. The entire empire is under my personal protection.
                return true;
            case 40:
                // $script:1126155107011968$ 
                // - Prove yourself to my officers, and I'll consider entrusting you with a mission for the Maple Alliance.
                return true;
            default:
                return true;
        }
    }
}
