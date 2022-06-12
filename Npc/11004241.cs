using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004241: Landevian
/// </summary>
public class _11004241 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010943$
    // - I'm ashamed of myself.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010944$
                // - I'm ashamed of myself.
                return 10;
            case (10, 1):
                // $script:0809223207010945$
                // - What you saw back there, that wasn't me.
                return 10;
            case (10, 2):
                // $script:0809223207010946$
                // - You better not tell anyone else about this! Especially not $npcName:11004054[gender:1]$!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
