using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000340: Zobek
/// </summary>
public class _11000340 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407001360$
    // - What can I do for you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001363$
                // - I've been by $npcName:11000341[gender:1]$'s side since she was born. It's the least I could do to repay her grandfather, who took me under his wing when I had no place to go.
                return -1;
            case (40, 0):
                // $script:0831180407001364$
                // - If the Andreas hadn't fallen so easily, this $map:02000178$ would not be here today. 
                switch (selection) {
                    // $script:0831180407001365$
                    // - What happened to the Andreas?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001366$
                // - T-that's... Ah, let's not stir up old, painful memories.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
