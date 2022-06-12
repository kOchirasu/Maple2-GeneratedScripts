using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004474: Wentid
/// </summary>
public class _11004474 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012151$
    // - Hey, do you see that huge ship? I'm not imagining it, am I?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012152$
                // - Hey, do you see that huge ship? I'm not imagining it, am I?
                return 10;
            case (10, 1):
                // $script:1227192907012153$
                // - It's so big... How can something that big float up in the sky like that?
                switch (selection) {
                    // $script:1227192907012154$
                    // - Didn't you ride Sky Fortress to get here?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012155$
                // - Sure, but I couldn't exactly tell how big it is from the inside. Seeing it now, away from the buildings in Tria... It's unreal!
                return 11;
            case (11, 1):
                // $script:1227192907012156$
                // - Do you know? How does it fly like that?
                switch (selection) {
                    // $script:1227192907012157$
                    // - $npcName:24100101$ would tell you it's the power of science.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012158$
                // - $npcName:24100101$? Is that the name of one of the Sky Fortress big wigs? She sounds intimidating...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
