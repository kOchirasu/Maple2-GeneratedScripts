using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004477: Soran
/// </summary>
public class _11004477 : NpcScript {
    internal _11004477(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012173$ 
                // - Eee! It's him! It's really him!
                return true;
            case 10:
                // $script:1227192907012174$ 
                // - Eee! It's him! It's really him!
                // $script:1227192907012175$ 
                // - Ugh! What are you?
                // $script:1227192907012176$ 
                // - Don't jump out at me like that. When I saw your ugly mug, I thought you were some kind of freaky monster.
                switch (selection) {
                    // $script:1227192907012177$
                    // - Rude!
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012178$ 
                // - Don't take it personally, uggo. Everyone is hideous compared to Blake!
                switch (selection) {
                    // $script:1227192907012179$
                    // - You need to get your eyes checked.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012180$ 
                // - A normie like you will never understand! Blake is beauty. Blake is the future!
                // $script:1227192907012181$ 
                // - Just wait. Soon, everyone in Kritias will bow before Blake's handsomeness!
                return true;
            default:
                return true;
        }
    }
}
