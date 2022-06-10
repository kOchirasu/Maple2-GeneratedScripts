using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000220: Victor
/// </summary>
public class _11000220 : NpcScript {
    internal _11000220(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000962$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407000964$ 
                // - Fellowstone Tower will be the greatest building in all of Maple World when it's finished. The blueprints alone took years to perfect. 
                return true;
            case 30:
                // $script:0831180407000965$ 
                // - When it's complete, people will flock from all over to see Fellowstone Tower. It'll be the crown jewel of Victoria Island!
                return true;
            default:
                return true;
        }
    }
}
