using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004179: Karl
/// </summary>
public class _11004179 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010620$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010621$
                // - My greatest joy is seeing my daughter smile. I would have visited this place sooner if I had known it would make $npcName:11004180[gender:1]$ so happy.
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
