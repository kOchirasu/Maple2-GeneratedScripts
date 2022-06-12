using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003335: Barista
/// </summary>
public class _11003335 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0510143807008459$
    // - What do you want?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0510145607008463$
                // - You'll get nothing out of me!
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
