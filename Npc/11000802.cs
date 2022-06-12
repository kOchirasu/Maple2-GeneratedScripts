using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000802: Shadow Tombstone
/// </summary>
public class _11000802 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180610000986$
    // - <font color="#909090">(Someone left a message.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180610000991$
                // - <font color="#909090">(There's dark energy billowing and swirling all around this tombstone! It's making it impossible to read the message.)</font>
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
