using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001404: Tuchiela
/// </summary>
public class _11001404 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217025507005332$
    // - Wah! You startled me!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1217025507005336$
                // - You've been on the road a long time. I can tell. Come in and have a glass of water. It's on the house!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
