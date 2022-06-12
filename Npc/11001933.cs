using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001933: Apprentice Vava
/// </summary>
public class _11001933 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1122150407007456$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1122214707007478$
                // - I'm <i>trying</i> to focus here!
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
