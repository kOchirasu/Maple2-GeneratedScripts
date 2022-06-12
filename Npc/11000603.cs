using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000603: Degan
/// </summary>
public class _11000603 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002482$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002484$
                // - I'll see you soon... my friend...
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
