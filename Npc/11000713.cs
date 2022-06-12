using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000713: Torto
/// </summary>
public class _11000713 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002872$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002875$
                // - I have terrapin cousins living in the sea, and one of the most famous terrapins in history is called Byeljubu. Have you heard of him?
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
