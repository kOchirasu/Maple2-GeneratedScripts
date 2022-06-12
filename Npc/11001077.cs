using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001077: Tantamomi
/// </summary>
public class _11001077 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003675$
    // - A full moon... The Kakas... Aw, please help me. Hah hah, hah hah hah!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003678$
                // - D-don't come near me. No! I need a friend. No, no... L-let's start again... Ha!
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
