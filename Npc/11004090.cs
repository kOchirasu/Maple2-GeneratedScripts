using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004090: Everfrost Star
/// </summary>
public class _11004090 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010321$
    // - <font color='#909090'>(This giant snowflake reflects the brilliant sun. No matter how brightly it shines, it never seems to melt.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010322$
                // - <font color='#909090'>(This giant snowflake reflects the brilliant sun. No matter how brightly it shines, it never seems to melt.)</font>
                return 10;
            case (10, 1):
                // $script:0622133907010323$
                // - <font color='#909090'>(Tourists come from all over the world to see the local "Santa" who makes presents for good boys and girls. Taking your picture in front of the snow crystal is a trendy thing to do.)</font>
                return 10;
            case (10, 2):
                // $script:0622133907010324$
                // - <font color='#909090'>(They say that the snow crystal is a reflection of the goodness and kindness that lives in the hearts of Santas everywhere.)</font>
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
