using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001843: Eks
/// </summary>
public class _11001843 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1020165907007310$
    // - My head... My shoulders... My spleen...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1020165907007311$
                // - The room's spinning. Who knows when I'll be ready for active duty?
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
