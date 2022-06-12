using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000003: Growlie
/// </summary>
public class _11000003 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50;60
    }

    // Select 0:
    // $script:0831180407000015$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000018$
                // - I don't care why the court was canceled anymore. I've heard every rumor under the sun, and now they're saying it was an earthquake? Ridiculous! All I want now is to kick back.
                return -1;
            case (50, 0):
                // $script:0831180407000019$
                // - Bah, everyone acts like they're the busiest person in the world. Everyone here in $map:02000001$ spends their day rushing around like fools. Seriously!
                return -1;
            case (60, 0):
                // $script:1215102407009687$
                // - What do you want?
                switch (selection) {
                    // $script:1215102407009688$
                    // - Have you heard the rumors going around?
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:1215102407009689$
                // - For the last time, I'm not adopted! Mom says its normal for babies to come out giant and furry sometimes. If you want a real rumor, you should hear about the giant demons zipping around the sky.
                switch (selection) {
                    // $script:1215102407009690$
                    // - Giant demons?
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:1215102407009691$
                // - You didn't know? It's all anyone's talking about lately. I've heard talk that they've been kidnapping people.
                switch (selection) {
                    // $script:1215102407009692$
                    // - Do you actually know of any victims?
                    case 0:
                        return 63;
                }
                return 62;
            case (62, 1):
                // $script:1215102407009693$
                // - Yeah, the appear like a flash of lightning. In the blink of an eye, the person next to you is gone. Just like that!
                return -1;
            case (63, 0):
                // $script:1215102407009694$
                // - Err... No. I'm just telling you what I heard!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.SelectableDistractor,
            (62, 1) => NpcTalkButton.Close,
            (63, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
