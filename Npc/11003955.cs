using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003955: Knight
/// </summary>
public class _11003955 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010001$
    // - Hi there.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010002$
                // - So you're an adventurer? You seem pretty strong. Nice to meet you.
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
