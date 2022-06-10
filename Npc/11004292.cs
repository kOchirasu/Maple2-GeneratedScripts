using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004292: Stuki
/// </summary>
public class _11004292 : NpcScript {
    internal _11004292(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011360$ 
                // - Welcome, welcome, to Mon Bloody Chouchou Hotel!
                return true;
            case 30:
                // $script:1002141907011363$ 
                // - Do you have a thirst for adventure? Then come to the Mon Bloody Chouchou Hotel and celebrate Halloween with us!
                switch (selection) {
                    // $script:1002141907011364$
                    // - Sounds fun!
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011365$ 
                // - Please take the portal here to the $map:63000065$. And enjoy your stay... Mwahahaha! 
                return true;
            default:
                return true;
        }
    }
}
