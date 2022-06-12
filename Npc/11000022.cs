using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000022: Harry
/// </summary>
public class _11000022 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000111$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000114$
                // - Are you heading to $map:02000001$. You know that the way is blocked, right?
                switch (selection) {
                    // $script:0831180407000115$
                    // - Yeah, I heard.
                    case 0:
                        return 31;
                    // $script:0831180407000116$
                    // - No, I didn't. Really?
                    case 1:
                        return 34;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000117$
                // - Good, I don't have to explain it to you. So... if you can't get to $map:02000001$, what are you going to do?
                switch (selection) {
                    // $script:0831180407000118$
                    // - I'll find another way!
                    case 0:
                        return 32;
                    // $script:0831180407000119$
                    // - Beats me.
                    case 1:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0831180407000120$
                // - What are you gonna do, fly? The road is gone! It has ceased to be! You need to be realistic about this.
                return 32;
            case (32, 1):
                // $script:0831180407000121$
                // - Seriously, have a look at $map:02000115$. Let me know what you think of the terrible, yawning chasm of doom in your way. I'll wait.
                return -1;
            case (33, 0):
                // $script:0831180407000122$
                // - That's understandable. $map:02000001$ has it all, and all we've got is... fish. Might as well head home once you've got your fill of fish, huh?
                return -1;
            case (34, 0):
                // $script:0831180407000123$
                // - It sure is. The Royal Road is the main route from this harbor to $map:02000001$, and it was cracked open by the earthquake that happened the other day. Now no one can get to $map:02000001$.
                return 34;
            case (34, 1):
                // $script:0831180407000124$
                // - If you don't believe me, go to $map:02000115$ and see for yourself.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
