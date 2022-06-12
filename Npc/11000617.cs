using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000617: Marmut
/// </summary>
public class _11000617 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002520$
    // - This is troublesome...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002522$
                // - Hmph, I can't believe I have to investigate this!
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
