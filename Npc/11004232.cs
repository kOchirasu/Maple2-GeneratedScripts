using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004232: Beatrice
/// </summary>
public class _11004232 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010913$
    // - I knew you would succeed.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010914$
                // - I knew you would succeed.
                return 10;
            case (10, 1):
                // $script:0809223207010915$
                // - I know you are powerful, but you still need to look after yourself.
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
