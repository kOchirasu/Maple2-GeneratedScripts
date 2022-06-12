using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000062: Mimi
/// </summary>
public class _11000062 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000283$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000286$
                // - $MyPCName$, did you hear that? Ordinary people can attend the empress's court this time! I'll be able to meet the $npcName:11000075[gender:1]$ in person. Oh, I'm so nervous!
                return 30;
            case (30, 1):
                // $script:0831180407000287$
                // - $MyPCName$, you're also coming to the court, right? Come on, come with us! Dad said he'd take me with him.
                switch (selection) {
                    // $script:0831180407000288$
                    // - Where will the court be held?
                    case 0:
                        return 31;
                    // $script:0831180407000289$
                    // - Why are you so interested in the court?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000290$
                // - In $map:02000001$! It's the biggest city on the mainland, far across the ocean. We'll have to take a ship to $map:02000062$ first, though.
                switch (selection) {
                    // $script:0831180407000291$
                    // - Where can I board the ship?
                    case 0:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0831180407000292$
                // - Because it's a once-in-a-lifetime chance to see $npcName:11000075[gender:1]$! Oarsman $npcName:11000016[gender:0]$ said that just seeing her would bring honor to my family.
                return -1;
            case (33, 0):
                // $script:0831180407000293$
                // - Go to the dock and talk to the oarsman. Come to think of it, I haven't seen him lately. I wonder where he is...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
