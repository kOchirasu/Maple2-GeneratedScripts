using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000551: Delta
/// </summary>
public class _11000551 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002333$
    // - Ugh... Is anyone there? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002336$
                // - My fellow scouts have been scattered... we're on the brink... 
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
