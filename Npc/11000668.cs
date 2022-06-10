using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000668: Niro
/// </summary>
public class _11000668 : NpcScript {
    internal _11000668(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002711$ 
                // - WHAT?!
                return true;
            case 30:
                // $script:0831180407002714$ 
                // - Wait, are you going to go down to the basement?
                switch (selection) {
                    // $script:0831180407002715$
                    // - Yep!
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407002716$ 
                // - Ha! You're funny. I don't know how you got down here, but trust me when I say you NEVER want to go to the 2nd basement. There are some really scary guys down there.
                // $script:0831180407002717$ 
                // - It's just as well, I don't feel like dealing with you myself. Go on, go to the basement. And don't say I didn't warn you. 
                return true;
            default:
                return true;
        }
    }
}
