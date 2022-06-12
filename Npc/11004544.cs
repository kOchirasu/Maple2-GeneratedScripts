using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004544: Soldieretto Guide
/// </summary>
public class _11004544 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0108105807012638$
    // - This is the soldieretto lab. Are you a robot researcher?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0108105807012639$
                // - This is the soldieretto lab. Are you a robot researcher?
                return 10;
            case (10, 1):
                // $script:0108105807012640$
                // - If you do not have any particular business with us, leave. Humans who come here tend to give us more work.
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
