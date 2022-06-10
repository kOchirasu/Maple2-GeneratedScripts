using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001166: Merin
/// </summary>
public class _11001166 : NpcScript {
    internal _11001166(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1008163207004068$ 
                // - What should I do?
                return true;
            case 30:
                // $script:1008163207004071$ 
                // - Shh! Please, keep your voice down! <i>That mage</i> can't know I'm here!
                return true;
            default:
                return true;
        }
    }
}
