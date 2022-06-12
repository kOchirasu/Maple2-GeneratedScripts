using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000667: Lando
/// </summary>
public class _11000667 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002704$
    // - WHAT?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002707$
                // - Mm? What? 
                switch (selection) {
                    // $script:0831180407002708$
                    // - What are you doing?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002709$
                // - You're a curious sort, aren't you? As the old saying goes, ignorance is bliss.
                return 31;
            case (31, 1):
                // $script:0831180407002710$
                // - Don't stick your nose where it doesn't belong.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
