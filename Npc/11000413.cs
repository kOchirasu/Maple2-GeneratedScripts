using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000413: Jean Pierre
/// </summary>
public class _11000413 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1121222006000829$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1121222006000830$
                // - Please don't ask about my past.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
