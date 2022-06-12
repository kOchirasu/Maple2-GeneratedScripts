using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001891: Blackeye
/// </summary>
public class _11001891 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1101100307007368$
    // - Hm... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1101100307007369$
                // - Thank you for coming here.
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
