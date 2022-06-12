using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004510: Mannstad Patrolman
/// </summary>
public class _11004510 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012457$
    // - What're you, a tourist? You wanna get tombstoned? This is a warzone! Not that $map:02020030$ is any better...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012458$
                // - What're you, a tourist? You wanna get tombstoned? This is a warzone! Not that $map:02020030$ is any better...
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
