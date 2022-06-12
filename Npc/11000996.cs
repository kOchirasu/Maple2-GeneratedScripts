using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000996: Yodano
/// </summary>
public class _11000996 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003421$
    // - Speak up. I can't hear you over the alarm. Cluck!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003424$
                // - Someone, please turn off that alarm clock. Cluck!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
