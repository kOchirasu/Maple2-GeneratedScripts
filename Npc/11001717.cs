using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001717: Junta
/// </summary>
public class _11001717 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006968$
    // - You'd better have a good reason for interrupting my training.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0805021607007093$
                // - I've given it some thought, but I still don't understand why some of us would leave the master's guidance to live in human cities like $map:02000001$. $MyPCName$, do you like this place?
                switch (selection) {
                    // $script:0805021607007094$
                    // - It's not too bad. 
                    case 0:
                        return 31;
                    // $script:0805021607007095$
                    // - It's too loud for me!
                    case 1:
                        return 40;
                }
                return -1;
            case (31, 0):
                // $script:0805021607007096$
                // - Hmph. If you have time to enjoy the sights, then you have time to train!
                switch (selection) {
                    // $script:0805021607007097$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (40, 0):
                // $script:0805021607007098$
                // - Yes... Yes, it is, isn't it? It hasn't escaped my notice that you've been training hard lately. Don't strain yourself.
                switch (selection) {
                    // $script:0805021607007099$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
