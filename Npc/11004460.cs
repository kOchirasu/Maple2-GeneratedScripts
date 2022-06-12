using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004460: Safehold Guardsman
/// </summary>
public class _11004460 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012067$
    // - All clear!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012068$
                // - All clear!
                return 10;
            case (10, 1):
                // $script:1227192907012069$
                // - I'm a little nervous about this place, but this is a chance to set myself apart from the other guards!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
