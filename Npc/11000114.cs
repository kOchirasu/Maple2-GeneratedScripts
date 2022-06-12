using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000114: JJ
/// </summary>
public class _11000114 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000477$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000478$
                // - What if $map:02000062$ and $map:02000001$ and everything else in the world collapses?
                switch (selection) {
                    // $script:0831180407000479$
                    // - Don't worry.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831180407000480$
                // - Really, $MyPCName$? Looking into this giant pit of doom doesn't fill you with the least little bit of doubt?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
