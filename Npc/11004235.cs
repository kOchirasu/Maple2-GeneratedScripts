using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004235: Blackeye
/// </summary>
public class _11004235 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010923$
    // - I cannot fathom how much more powerful you'll grow.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010924$
                // - I cannot fathom how much more powerful you'll grow.
                return 10;
            case (10, 1):
                // $script:0809223207010925$
                // - It's an honor to be working by your side once more, friend.
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
