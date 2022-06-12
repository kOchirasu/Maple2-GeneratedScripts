using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000136: Tina
/// </summary>
public class _11000136 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000562$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000563$
                // - This wolf's name is Buka. He's my friend.
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
