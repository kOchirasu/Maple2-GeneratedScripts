using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004349: Bobo
/// </summary>
public class _11004349 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011761$
    // - Ha, you like Bobo's red nose? Remind you of someone?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011762$
                // - Ha, you like Bobo's red nose? Remind you of someone?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
