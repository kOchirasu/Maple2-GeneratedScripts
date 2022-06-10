using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004284: Demdem
/// </summary>
public class _11004284 : NpcScript {
    internal _11004284(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911214707011299$ 
                // - Welcome! This is $map:02010002$, the heart of Karkar! On behalf of meerkats everywhere, I'd just like to say... Hiya!
                return true;
            case 10:
                // $script:0911214707011300$ 
                // - Welcome! This is $map:02010002$, the heart of Karkar! On behalf of meerkats everywhere, I'd just like to say... Hiya!
                // $script:0911214707011301$ 
                // - Karkar Island is hot and dry. Drink lots of water to stay hydrated, and don't forget to slather on that sunscreen!
                // $script:0913151207011310$ 
                // - Ah, doesn't that balance between the fierce desert and the cityscape here in $map:02010002$ revitalize you? Say, have you ever visited the $npcName:11004264$?
                switch (selection) {
                    // $script:0913151207011311$
                    // - I don't believe I've had the pleasure.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0913151207011312$
                    // - I sure have!
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0913151207011313$ 
                // - That just won't do! The $npcName:11004264$ is <i>the</i> hottest shopping spot in the whole city! Go ahead, run along now!
                return true;
            case 12:
                // $script:0913151207011314$ 
                // - Isn't it so cool? I was thinking of heading over there tonight and treating myself to a new hat!
                return true;
            default:
                return true;
        }
    }
}
