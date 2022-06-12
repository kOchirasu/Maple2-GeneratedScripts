using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004280: Pillar of Light
/// </summary>
public class _11004280 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011291$
    // - <font color="#909090">(A bright light shines through a crack in the wall.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011292$
                // - <font color="#909090">(A bright light shines through a crack in the wall.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011293$
                // - <font color="#909090">(This passageway was blocked off long ago, but something on the other side still shines brilliantly.)</font>
                return 10;
            case (10, 2):
                // $script:0913151207011306$
                // - <font color="#909090">(You can sense a different sort of power beyond the crack in the wall.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
