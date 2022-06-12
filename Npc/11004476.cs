using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004476: Ludwigia
/// </summary>
public class _11004476 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012167$
    // - Sigh... I'm sick of these ration packs they have us all eating. I miss the gourmet restaurants of Tria!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012168$
                // - They didn't warn us that Kritias doesn't have any proper eateries. What's a foodie supposed to do in a place like this?
                return 10;
            case (10, 1):
                // $script:1227192907012169$
                // - I would kill for a bowl of blue mushroom slime soup in cornelian cherry sauce...
                return 10;
            case (10, 2):
                // $script:1227192907012170$
                // - Ugh, talking about it just makes it worse! I'm going to be too hungry to sleep tonight...
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
