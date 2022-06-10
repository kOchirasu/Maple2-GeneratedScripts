using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000454: Teo
/// </summary>
public class _11000454 : NpcScript {
    internal _11000454(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002006$ 
                // - I'm a seasoned sailor!
                return true;
            case 30:
                // $script:0831180407002009$ 
                // - Ahoy there! Have you ever seen a whale?
                switch (selection) {
                    // $script:0831180407002010$
                    // - Yes.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407002011$
                    // - Nope.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407002012$ 
                // - Bah, nonsense! I've been a fisherman my whole life, and only seen a whale once. And it was a teeny one at that! Me dream is to see the great blue whale just once before the sea takes me.
                return true;
            case 32:
                // $script:0831180407002013$ 
                // - Aye, they're an elusive catch. I've always wanted to see a blue whale myself.
                return true;
            default:
                return true;
        }
    }
}
