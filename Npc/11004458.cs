using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004458: Cantata
/// </summary>
public class _11004458 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:1231140707012480$
    // - Hey there! I'm investigating rumors of a ghost dressed in black.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1231140707012481$
                // - Hey there! I'm investigating rumors of a ghost dressed in black.
                switch (selection) {
                    // $script:1231140707012482$
                    // - Did you say gh-gh-gh-ghost?!
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1231140707012483$
                // - Yes! There have been lots of sightings of this so-called black-garbed ghost around here.
                return 11;
            case (11, 1):
                // $script:1231140707012484$
                // - Apparently it wanders around, mumbling something about sacrificing a soul to obtain great power...
                return 11;
            case (11, 2):
                // $script:1231140707012485$
                // - It's right around this time that most of the witnesses run for their lives, so that's all I have to go on. Well, that, and...
                switch (selection) {
                    // $script:1231140707012486$
                    // - There's something else?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1231140707012487$
                // - Yes! I think there was something about... summoning a many-armed god?
                switch (selection) {
                    // $script:1231140707012488$
                    // - It can't be...
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1231140707012489$
                // - You know what that means?
                switch (selection) {
                    // $script:1231140707012490$
                    // - I'm sure it's nothing.
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1231140707012491$
                // - I'll let you know if I learn anything else. This investigation is just getting started!
                return -1;
            case (20, 0):
                // $script:0410153807014589$
                // - Hm...
                return 20;
            case (20, 1):
                // $script:0410153807014590$
                // - Where oh where could it be?
                return 20;
            case (20, 2):
                // $script:0410153807014591$
                // - Was I misled?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
