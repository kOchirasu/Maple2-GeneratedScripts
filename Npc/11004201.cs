using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004201: Tourist
/// </summary>
public class _11004201 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010650$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010651$
                // - Out of the way, buddy, you're in my shot.
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
