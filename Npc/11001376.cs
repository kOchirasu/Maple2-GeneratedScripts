using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001376: Pallard
/// </summary>
public class _11001376 : NpcScript {
    internal _11001376(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005361$ 
                // - You called?
                return true;
            case 30:
                // $script:1217144507005364$ 
                // - Mwahaha! This scene is... perfect! The height of drama, eclipsing any movie or show I've ever seen! And <i>I'm</i> the guy who gets to film it. This is probably going to be the greatest film of my entire career!
                return true;
            default:
                return true;
        }
    }
}
