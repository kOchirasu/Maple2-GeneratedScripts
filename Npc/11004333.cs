using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004333: Miel
/// </summary>
public class _11004333 : NpcScript {
    internal _11004333(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011573$ 
                // - Hello. 
                return true;
            case 10:
                // $script:1010140307011574$ 
                // - Hello. 
                // $script:1010140307011575$ 
                // - My friend. It is pleasant to see your face. 
                // $script:1010140307011576$ 
                // - This place is beautiful, is it not? 
                // $script:1010140307011577$ 
                // - I have never before walked such a land, under such a sky... and yet it strikes me as familiar, all the same. 
                // $script:1010140307011578$ 
                // - Perhaps I am drawing nearer to the answers I seek. 
                switch (selection) {
                    // $script:1010140307011579$
                    // - I'm sure you are!
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1010140307011580$ 
                // - Thank you. Your enthusiasm always lifts my spirits. 
                switch (selection) {
                    // $script:1010140307011581$
                    // - Is $npcName:11001431[gender:0]$ with you?
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:1010140307011582$ 
                // - I asked him to accompany me, but I fear our vulpine friend declined my invitation. Oh, what I might have learned if he was here to aid me... 
                // $script:1010140307011583$ 
                // - A lack his cutting insight... 
                return true;
            default:
                return true;
        }
    }
}
