using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001276: Maccan
/// </summary>
public class _11001276 : NpcScript {
    internal _11001276(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1207124110001298$ 
                // - Ah! Ah! Ah-choo! 
                return true;
            case 40:
                // $script:1223143510001417$ 
                // - Ah-ah-ah-achoo! So much salt in the air! It tickles my nose, but I love the taste. Is there something I can do for you? 
                switch (selection) {
                    // $script:1223143510001418$
                    // - I want to go to Karkar Island.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:1223143510001419$
                    // - ...
                    case 1:
                        Id = 44;
                        return false;
                }
                return true;
            case 41:
                // $script:1223143510001420$ 
                // - In that case, you'll want a ride in my <i>Lumiwind</i>. She's my greatest invention! Her design is inspired by the extinct dragons who once soared the skies, the lumarigons. Do you want to ride? 
                switch (selection) {
                    // $script:1223143510001421$
                    // - Yes.
                    case 0:
                        Id = 42;
                        return false;
                    // $script:1223143510001422$
                    // - I'll come back later.
                    case 1:
                        Id = 43;
                        return false;
                }
                return true;
            case 42:
                // $script:1223143510001423$ functionID=1 
                // - All right, bon voyage! 
                return true;
            case 43:
                // $script:1223143510001424$ 
                // - No rush. The <i>Lumiwind</i> will always be right here. 
                return true;
            case 44:
                // $script:0215134610001837$ 
                // - Here to gawk at an old genius? You're silly, you know that? 
                return true;
            default:
                return true;
        }
    }
}
