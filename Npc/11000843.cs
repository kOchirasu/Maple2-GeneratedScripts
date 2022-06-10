using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000843: Mett
/// </summary>
public class _11000843 : NpcScript {
    internal _11000843(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003084$ 
                // - Oh, no...  
                return true;
            case 30:
                // $script:0831180407003087$ 
                // - This is beyond bad! $npcName:22400062$ is trying to manipulate the timeline to his own ends! If he succeeds, the resulting temporal cascade will wipe away all of history as we know it! 
                return true;
            case 40:
                // $script:0831180407003088$ 
                // - This place exists upon the central axis of time for our universe. It is a road to all things. Here all possible timelines coexist simultaneously. $npcName:22400062$ plans to collapse them all into a single eventuality, one where he reigns supreme! 
                return true;
            default:
                return true;
        }
    }
}
