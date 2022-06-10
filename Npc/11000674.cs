using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000674: Altar of Rage
/// </summary>
public class _11000674 : NpcScript {
    internal _11000674(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000464$ 
                // - <font color="#909090">(The altar has faded letters written on it.)</font>
                return true;
            case 10:
                // $script:0831180610000465$ 
                // - <font color="#909090">(Read the message.)</font>
                // $script:0831180610000466$ 
                // - <i>Shadow World is an angry land...
                //   Where no blessing upon anyone can make any difference.</i>
                // $script:0831180610000467$ 
                // - <i>Lo, if you are one who thirsts for blood, will you absorb the wrathful energy and rid yourself of $skill:70000029$?</i>
                switch (selection) {
                    // $script:0831180610000468$
                    // - Lose $skill:70000029$.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000469$
                    // - Retain $skill:70000029$.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180610000470$ functionID=1 
                // - <i>The wrathful shadows have devoured every one of your blessings and taken over your mind.
                //   Now, you see that friendship is a myth, and everyone is your enemy!</i>
                return true;
            case 12:
                // $script:0831180610000471$ 
                // - <i>In the end, nothing can truly shield you from reality.</i>
                return true;
            case 20:
                // $script:0831180610000472$ 
                // - <font color="#909090">(Reading the words on the altar, Turka's anger is almost palpable.)</font>
                return true;
            default:
                return true;
        }
    }
}
