using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001623: Wei Hong
/// </summary>
public class _11001623 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0516130207006126$
    // - You got something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0531170907006281$
                // - I'm looking forward to today's match.
                switch (selection) {
                    // $script:0531170907006282$
                    // - What makes you so sure $npcName:11001547[gender:0]$'s going to win?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0531170907006283$
                // - I'm not. Anything can happen in the ring. But I know $npcName:11001547[gender:0]$, and I know that he never fails me.
                switch (selection) {
                    // $script:0531170907006284$
                    // - That's because he's never faced me in the ring.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0531170907006285$
                // - Is that so? Okay. Let's see if your fists can back up your words.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
