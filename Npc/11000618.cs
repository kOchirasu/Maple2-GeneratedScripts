using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000618: Jerrol
/// </summary>
public class _11000618 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002523$
    // - Could you help me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002524$
                // - How on the world am I supposed to fix these wagons? I can't carry them back to town!
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
