using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001129: Greenman
/// </summary>
public class _11001129 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0911192907003854$
    // - What? What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0911192907003857$
                // - What? Can't you see I'm working? Leave me alone.
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
