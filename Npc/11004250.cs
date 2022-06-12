using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004250: Mysterious Wisp
/// </summary>
public class _11004250 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010960$
    // - It's been a while since I last met a stranger. Hey, adventurer, does darkness still exist in the world?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010961$
                // - It's been a while since I last met a stranger. Hey, adventurer, does darkness still exist in the world?
                switch (selection) {
                    // $script:0830160907010980$
                    // - You realize this IS the land of darkness, right?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0830160907010981$
                // - I see... I guess our efforts haven't paid off yet...
                switch (selection) {
                    // $script:0830160907010982$
                    // - What do you mean?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0830160907010983$
                // - After this world was created, my kind studied magic here for a long time. We sought to stand against the darkness that everyone else thought had disappeared.
                switch (selection) {
                    // $script:0830160907010984$
                    // - What kind of magic did you study?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0830160907010985$
                // - Powerful magic! Magic that could drive away darkness! Magic of light, hot and bright! Magic that is not easily accessible, not even to us...
                switch (selection) {
                    // $script:0830160907010986$
                    // - Wow. You're really passionate about this, huh?
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:0830160907010987$
                // - We are oathbound to banish the darkness. It is our mortal enemy, and it has tried to destroy us again and again, ever since learning of our existence.
                return 14;
            case (14, 1):
                // $script:0830160907010988$
                // - We pushed and pushed to master ever more powerful magic as our enemy, the darkness, grew stronger. But we grew too greedy. Our effort to put the darkness to sleep before the power of the goddess of light ran out... wasted!
                return 14;
            case (14, 2):
                // $script:0830160907010989$
                // - Though we failed, we watch over this world still, ever mindful of our pledge to drive out the darkness.
                return 14;
            case (14, 3):
                // $script:0830160907010990$
                // - Only when the darkness disappears from this world will I be able to rest in peace...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Next,
            (14, 1) => NpcTalkButton.Next,
            (14, 2) => NpcTalkButton.Next,
            (14, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
