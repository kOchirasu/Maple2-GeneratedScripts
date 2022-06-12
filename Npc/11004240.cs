using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004240: Ishura
/// </summary>
public class _11004240 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010940$
    // - I still feel out of sorts.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010941$
                // - I still feel out of sorts.
                return 10;
            case (10, 1):
                // $script:0809223207010942$
                // - I am truly in your debt. Thank you. I'm sorry about everything.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
