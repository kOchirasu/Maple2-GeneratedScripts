using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001430: Miel
/// </summary>
public class _11001430 : NpcScript {
    internal _11001430(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005427$ 
                // - Many things shine, not all of them valuable. 
                return true;
            case 40:
                // $script:1222203907005509$ 
                // - It's so close, but I can't reach it. It comes to me in the night and vanishes at dawn. 
                // $script:1222203907005510$ 
                // - The more I lean into the sunlight, the more I hide in the moonlight. But then, it all drifts apart. I can't continue this way...  
                switch (selection) {
                    // $script:1222203907005511$
                    // - What on earth are you talking about?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1222203907005512$ 
                // - Huh...? Shoo! You wouldn't understand. 
                return true;
            case 50:
                // $script:0610174107006339$ 
                // - Hello. 
                switch (selection) {
                    // $script:0610174107006340$
                    // - Did you miss your best friend?
                    case 0:
                        Id = 56;
                        return false;
                    // $script:0610174107006341$
                    // - How are you doing?
                    case 1:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0610174107006342$ 
                // - The desert is always the same—beautiful and desolate. $MyPCName$, how have you been? 
                switch (selection) {
                    // $script:0610174107006343$
                    // - I came running all this way to see you.
                    case 0:
                        Id = 52;
                        return false;
                    // $script:0610174107006344$
                    // - Things have been nice and quiet without you to bother me.
                    case 1:
                        Id = 55;
                        return false;
                }
                return true;
            case 52:
                // $script:0610174107006345$ 
                // - Ha... I see. I thought I saw a bright light coming from afar... It lifted my spirits. 
                switch (selection) {
                    // $script:0610174107006346$
                    // - Do you miss me?
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:0610174107006347$ 
                // - Are you feeling all right? When I mentioned a bright light from afar, I meant the moon. The moon! Not you. 
                switch (selection) {
                    // $script:0610174107006348$
                    // - I'll be sure to visit more often.
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            case 54:
                // $script:0610174107006349$ 
                // - Sure, you do that. Who knows? Maybe next time I'll even be waiting for you.
<font color="#909090">(In spite of his cool words, there's a warm smile on his lips.)</font>  
                return true;
            case 55:
                // $script:0610174107006350$ 
                // - How nice for you. Leave in peace, then.
<font color="#909090">(He sighs and looks away.)</font> 
                return true;
            case 56:
                // $script:0610174107006351$ 
                // - My friend? Who?  
                switch (selection) {
                    // $script:0610174107006352$
                    // - Have you forgotten our friendship?
                    case 0:
                        Id = 57;
                        return false;
                    // $script:0610174107006353$
                    // - Are you feeling okay?
                    case 1:
                        Id = 58;
                        return false;
                }
                return true;
            case 57:
                // $script:0610174107006354$ 
                // - Ah, of course I remember! You and I are friends now. It was just a little joke.  
                switch (selection) {
                    // $script:0610174107006355$
                    // - Keep these jokes up, and I'll stop visiting.
                    case 0:
                        Id = 59;
                        return false;
                }
                return true;
            case 58:
                // $script:0610174107006356$ 
                // - I feel fine. Thank you for your concern, but... I was just playing a little joke on you. Maybe you're too naive for such play... 
                switch (selection) {
                    // $script:0610174107006357$
                    // - Keep these jokes up, and I'll stop visiting.
                    case 0:
                        Id = 59;
                        return false;
                }
                return true;
            case 59:
                // $script:0610174107006358$ 
                // - I thought this was what friends do! Now you're making <i>me</i> confused. If visiting me is such a bother, then you don't have to do it, you know.  
                switch (selection) {
                    // $script:0610174107006359$
                    // - I'll visit you again soon.
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
