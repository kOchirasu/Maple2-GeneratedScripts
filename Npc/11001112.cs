using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001112: Bella's Soul
/// </summary>
public class _11001112 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003738$
    // - Do you know me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003739$
                // - I... I can't go back like this... No... 
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
