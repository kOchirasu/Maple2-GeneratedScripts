using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000614: Marr
/// </summary>
public class _11000614 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002511$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002513$
                // - I can't return to Maple World until I save these people. I'll never be able to forgive myself if I leave them behind.
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
