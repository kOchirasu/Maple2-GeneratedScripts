using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004273: Meeke
/// </summary>
public class _11004273 : NpcScript {
    internal _11004273(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011253$ 
                // - The moonlight is nice tonight. Very beautiful, very beautiful!
                return true;
            case 10:
                // $script:0911203207011254$ 
                // - The moonlight is nice tonight. Very beautiful, very beautiful!
                // $script:0911203207011255$ 
                // - And what brings you here tonight, human?
                switch (selection) {
                    // $script:0911203207011256$
                    // - I'm just passing through.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011257$ 
                // - Then you must visit our camp in the $map:02010033$! I'm sure they won't mind you dropping by. Probably.
                // $script:0911203207011258$ 
                // - The moonlight in our city is different from the moonlight out here, but no matter what, the moonlight is always beautiful!
                return true;
            default:
                return true;
        }
    }
}
