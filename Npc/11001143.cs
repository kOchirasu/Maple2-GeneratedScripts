using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001143: Valgor
/// </summary>
public class _11001143 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0915171007003945$
    // - Hello!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915171007003948$
                // - Plenty of archaeologists would kill for the chance to see Ellin Ruins with their own eyes. Are you here to see the ruins yourself?
                switch (selection) {
                    // $script:0915171007003949$
                    // - I'm not that interested in this old junk.
                    case 0:
                        return 31;
                    // $script:0915171007003950$
                    // - Oh yeah, I'm super into this stuff.
                    case 1:
                        return 32;
                    // $script:0915171007003951$
                    // - Not really. I was just wandering aimlessly.
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:0915171007003952$
                // - Really? Not interested in all this history? Oh... Then maybe you've come to hunt monsters? Just look around, this place is teeming with them.
                return -1;
            case (32, 0):
                // $script:0915171007003953$
                // - Really? You don't look like an archaeologist. Well, it's just nice to see someone interested in history. Stay as long as you like!
                return -1;
            case (33, 0):
                // $script:0915171007003954$
                // - Ah! A classic case of wanderlust, have we? Well, regardless, please be careful not to damage the ruins... And also, try not to get horribly mauled by monsters.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
