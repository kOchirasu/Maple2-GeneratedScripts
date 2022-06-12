using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000081: Yoyo
/// </summary>
public class _11000081 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000372$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000374$
                // - I like making shoes for my friends. Be my friend, and I'll give you a pair of shoes.
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
