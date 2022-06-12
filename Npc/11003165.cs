using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003165: Frey
/// </summary>
public class _11003165 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0314104907008094$
    // - How do you fare?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0314104907008097$
                // - $npc:11001853[gender:0]$ says there's nothing wrong with you, but I need to be sure. How do you feel?
                switch (selection) {
                    // $script:0314104907008098$
                    // - I'm fine.
                    case 0:
                        return 31;
                    // $script:0314104907008099$
                    // - I'm a bit sore...
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0314104907008100$
                // - Good.
                return -1;
            case (32, 0):
                // $script:0314104907008101$
                // - Really? We should look into that. I'll have $npc:11001853[gender:0]$ schedule you for some exploratory surgery.
                switch (selection) {
                    // $script:0314104907008102$
                    // - Th-that really isn't necessary!
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0314104907008103$
                // - It's no trouble. After all you did out on the field, this is the least we can do.
                return -1;
            case (40, 0):
                // $script:0314104907008104$
                // - You were glowing when we found you. How did you do that?
                switch (selection) {
                    // $script:0314104907008105$
                    // - I really don't remember.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0314104907008106$
                // - I see. So it wasn't intentional.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
