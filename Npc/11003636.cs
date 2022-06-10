using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003636: JCH-2YS
/// </summary>
public class _11003636 : NpcScript {
    internal _11003636(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009064$ 
                // - Identity confirmed... $MyPCName$...
                return true;
            case 10:
                // $script:1109121007009065$ 
                // - Initiating light banter protocol. I am just passing through town, stranger.
                switch (selection) {
                    // $script:1109121007009066$
                    // - Aren't you a polite robot?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009067$ 
                // - Rhetorical question detected. Response: Can I help you with something?
                switch (selection) {
                    // $script:1109121007009068$
                    // - No, no, I'm good.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009069$ 
                // - Detecting trace amounts of $npcName:11003535[gender:1]$ pheromones... Special encoders enabled. Message: "Code EK-LOVE."
                switch (selection) {
                    // $script:1109121007009070$
                    // - You're an agent...?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009071$ 
                // - Resuming normal operations. Have a nice day.
                return true;
            default:
                return true;
        }
    }
}
