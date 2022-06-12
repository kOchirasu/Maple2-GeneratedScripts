using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000326: Lowen
/// </summary>
public class _11000326 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1121222006000827$
    // - You can buy Souvenirs in Furnish inside your house.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1121222006000828$
                // - Ahhh, what a wonderful world this is!
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
