using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000533: Camton
/// </summary>
public class _11000533 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002298$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002300$
                // - Unless you've worked a day here, you can't truly appreciate what we're doing.
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
