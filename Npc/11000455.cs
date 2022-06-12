using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000455: Pason
/// </summary>
public class _11000455 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002014$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002017$
                // - Everyone's all freaked out about the storm and the earthquake, but so what? We need some excitement around here!
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
