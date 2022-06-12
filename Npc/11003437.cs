using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003437: Anne
/// </summary>
public class _11003437 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0721140007008685$
    // - My mind is somewhere else today.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0721142007008703$
                // - The work never ends.
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
