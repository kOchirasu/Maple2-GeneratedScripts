using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000213: Anonymous Bum
/// </summary>
public class _11000213 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000904$
    // - Wh-what? What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000907$
                // - Leave me alone! I-I don't know anything!
                switch (selection) {
                    // $script:0831180407000908$
                    // - Uh, what?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000909$
                // - O-oh, you... I thought you were going to ask me something. Nevermind, then.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
