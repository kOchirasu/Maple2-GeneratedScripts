using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004284: Demdem
/// </summary>
public class _11004284 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911214707011299$
    // - Welcome! This is $map:02010002$, the heart of Karkar! On behalf of meerkats everywhere, I'd just like to say... Hiya!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911214707011300$
                // - Welcome! This is $map:02010002$, the heart of Karkar! On behalf of meerkats everywhere, I'd just like to say... Hiya!
                return 10;
            case (10, 1):
                // $script:0911214707011301$
                // - Karkar Island is hot and dry. Drink lots of water to stay hydrated, and don't forget to slather on that sunscreen!
                return 10;
            case (10, 2):
                // $script:0913151207011310$
                // - Ah, doesn't that balance between the fierce desert and the cityscape here in $map:02010002$ revitalize you? Say, have you ever visited the $npcName:11004264$?
                switch (selection) {
                    // $script:0913151207011311$
                    // - I don't believe I've had the pleasure.
                    case 0:
                        return 11;
                    // $script:0913151207011312$
                    // - I sure have!
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:0913151207011313$
                // - That just won't do! The $npcName:11004264$ is <i>the</i> hottest shopping spot in the whole city! Go ahead, run along now!
                return -1;
            case (12, 0):
                // $script:0913151207011314$
                // - Isn't it so cool? I was thinking of heading over there tonight and treating myself to a new hat!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
