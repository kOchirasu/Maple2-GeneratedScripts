using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000062: Mimi
/// </summary>
public class _11000062 : NpcScript {
    internal _11000062(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000283$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000286$ 
                // - $MyPCName$, did you hear that? Ordinary people can attend the empress's court this time! I'll be able to meet the $npcName:11000075[gender:1]$ in person. Oh, I'm so nervous!
                // $script:0831180407000287$ 
                // - $MyPCName$, you're also coming to the court, right? Come on, come with us! Dad said he'd take me with him.
                switch (selection) {
                    // $script:0831180407000288$
                    // - Where will the court be held?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000289$
                    // - Why are you so interested in the court?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000290$ 
                // - In $map:02000001$! It's the biggest city on the mainland, far across the ocean. We'll have to take a ship to $map:02000062$ first, though.
                switch (selection) {
                    // $script:0831180407000291$
                    // - Where can I board the ship?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407000292$ 
                // - Because it's a once-in-a-lifetime chance to see $npcName:11000075[gender:1]$! Oarsman $npcName:11000016[gender:0]$ said that just seeing her would bring honor to my family.
                return true;
            case 33:
                // $script:0831180407000293$ 
                // - Go to the dock and talk to the oarsman. Come to think of it, I haven't seen him lately. I wonder where he is...
                return true;
            default:
                return true;
        }
    }
}
