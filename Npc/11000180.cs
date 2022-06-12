using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000180: Konus
/// </summary>
public class _11000180 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000743$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000746$
                // - That stuff you're carrying don't look like junk. Are you going to toss it? People nowadays throw out just any old thing. New, old, doesn't matter. I found boxes of stuff like that. 
                switch (selection) {
                    // $script:0831180407000747$
                    // - What kinds of things did you find?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000748$
                // - Ha! Everything, my friend. Sometimes little baubles, sometimes official palace weapons. Found a lot of those lately, ever since the empress's court was canceled.
                return 31;
            case (31, 1):
                // $script:0831180407000749$
                // - A lot of time and effort went into making those weapons. Why not stockpile them? They'd be more useful than melting them down, surely.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
