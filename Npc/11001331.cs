using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001331: Mrs. Arthur
/// </summary>
public class _11001331 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005244$
    // - Oww...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005247$
                // - One moment, I'm shopping on cloud nine. The next moment... I don't know if I ever want to go shopping again!
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
